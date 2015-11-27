import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')
process.options = cms.untracked.PSet(
    # wantSummary = cms.untracked.bool(True)
    #SkipEvent = cms.untracked.vstring('ProductNotFound')
)

#parse command line arguments
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing('analysis')
options.register ('isPP',
                  False,
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.bool,
                  "Flag if this is a pp simulation")
options.parseArguments()

#####################################################################################
# HiForest labelling info
#####################################################################################


#####################################################################################
# Input source
#####################################################################################

process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                           fileNames = cms.untracked.vstring(options.inputFiles[0])                            
# fileNames = cms.untracked.vstring("file:/mnt/hadoop/cms/store/user/dgulhan/HIHighPt/HIHighPt_photon20and30_HIRun2011-v1_RECO_753_patch1/fd44351629dd155a25de2b4c109c824c/RECO_100_1_Uk0.root")                        )
                            # fileNames = cms.untracked.vstring("/store/express/Run2015E/ExpressPhysics/FEVT/Express-v1/000/261/544/00000//22D08F8A-2E8D-E511-BF87-02163E011965.root")                        
)


# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents))

import FWCore.PythonUtilities.LumiList as LumiList
# process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/DCSOnly/json_DCSONLY.txt').getVLuminosityBlockRange()
# process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSPHYS/PHYS_HEAVYIONS/cms/CMSSW_7_5_5_patch4/src/production/HIRun2015ForestingSetup_v0/ls100.txt').getVLuminosityBlockRange()

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

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_dataRun2_ExpressHI_v2', '')


#####################################################################################
# Define tree output
#####################################################################################



process.write_RAW = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    # SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('pass_hHLT_HIL1MinimumBiasHF1AND_v1')),
    fileName = cms.untracked.string('RAW_%s_.root' % options.outputFile),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*' ,
        'keep L1GlobalTriggerObjectMapRecord_hltL1GtObjectMap_*_*', 
        'keep edmTriggerResults_TriggerResults_*_HLT',
        'keep triggerTriggerEvent_hltTriggerSummaryAOD_*_*') ),
    splitLevel = cms.untracked.int32(0)
)


process.pAna = cms.EndPath(   
                              process.write_RAW
)


    
    
