import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')
process.options = cms.untracked.PSet(
    # wantSummary = cms.untracked.bool(True)
    #SkipEvent = cms.untracked.vstring('ProductNotFound')
)

#####################################################################################
# HiForest labelling info
#####################################################################################

process.load("HeavyIonsAnalysis.JetAnalysis.HiForest_cff")
process.HiForest.inputLines = cms.vstring("HiForest V3",)
import subprocess
version = subprocess.Popen(["(cd $CMSSW_BASE/src && git describe --tags)"], stdout=subprocess.PIPE, shell=True).stdout.read()
if version == '':
    version = 'no git info'
process.HiForest.HiForestVersion = cms.untracked.string(version)

#####################################################################################
# Input source
#####################################################################################
                            
process.source = cms.Source("NewEventStreamFileReader",
    fileNames = cms.untracked.vstring('root://eoscms.cern.ch///store/t0streamer/Data/Express/000/261/445/_inputfileflag_'
  )
)


# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000))



#####################################################################################
# Load Global Tag, Geometry, etc.
#####################################################################################

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

# PbPb 53X MC

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
# set snapshot to future to allow centrality table payload.
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")

process.GlobalTag.toGet.extend([
 cms.PSet(record = cms.string("HeavyIonRcd"),
 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
 ## 5.02 TeV Centrality Tables
 #tag = cms.string("CentralityTable_HFtowers200_HydjetDrum5_v740x01_mc"),
 #label = cms.untracked.string("HFtowersHydjetDrum5")
 ## 2.76 TeV Centrality Tables for data
 tag = cms.string("CentralityTable_HFtowers200_Glauber2010A_eff99_run1v750x01_offline"),
 label = cms.untracked.string("HFtowers")
 ),
])


process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')
process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("_outputfileflag_"))
# process.this_is_the_end = cms.EndPath(
  # process.hltanalysis
# )



process.load("HeavyIonsAnalysis.EventAnalysis.hltobject_cfi")
# process.TFileService = cms.Service("TFileService", fileName=cms.string("trgObject.root"))
process.hltobject.processName = cms.string('TEST')
process.hltobject.treeName = cms.string("JetTriggers")  #change this if you want a different tree name
process.hltbitanalysis.l1GtReadoutRecord = cms.InputTag("hltL1GtObjectMap","","TEST")
process.hltobject.triggerEvent = cms.InputTag("TriggerResults","",'TEST')

process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis*process.hltobject)


