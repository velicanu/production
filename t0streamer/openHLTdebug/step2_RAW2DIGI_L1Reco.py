# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions run2_data -n 2 --eventcontent FEVTDEBUGHLT -s RAW2DIGI,L1Reco --filein file:step1.root --fileout file:step2.root --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('L1Reco')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryRecoDB_cff')
# process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2)
)

# Input source
process.source = cms.Source("NewEventStreamFileReader",
    fileNames = cms.untracked.vstring('root://eoscms.cern.ch///store/t0streamer/Data/Express/000/261/445/run261445_ls0001_streamExpress_StorageManager.dat'
  )
)

process.options = cms.untracked.PSet(

)

process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')
process.TFileService = cms.Service("TFileService", fileName=cms.string("openhlt.root"))


# process.load("HeavyIonsAnalysis.EventAnalysis.hltobject_cfi")
# process.hltobject.processName = cms.string('TEST')
# process.hltobject.treeName = cms.string("JetTriggers")  #change this if you want a different tree name
# process.hltobject.triggerNames = cms.vstring("HLT_PAJet20_NoJetID_v1","HLT_PAJet40_NoJetID_v1","HLT_PAJet60_NoJetID_v1","HLT_PAJet80_NoJetID_v1","HLT_PAJet100_NoJetID_v1") #change these if you want also
# process.hltobject.triggerResults = process.hltbitanalysis.hltresults
# process.hltbitanalysis.l1GtReadoutRecord = cms.InputTag("gtDigis","","TEST")
# process.hltobject.triggerEvent = cms.InputTag("TriggerResults","",'TEST')
# process.hltbitanalysis.l1GtReadoutRecord = cms.InputTag("gtDigis","","TEST")

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:2'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)



process.hltbitanalysis.HLTProcessName = cms.string("TEST")
process.hltbitanalysis.hltresults = cms.InputTag( "TriggerResults","","TEST" )
process.hltbitanalysis.l1GtReadoutRecord = cms.InputTag("gtDigis","","TEST")
process.hltbitanalysis.l1GctHFBitCounts = cms.InputTag("gctDigis","","TEST")
process.hltbitanalysis.l1GctHFRingSums = cms.InputTag("gctDigis","","TEST")
process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)
# process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)
# process.TFileService = cms.Service("TFileService",
                                   # fileName=cms.string("openHLT_JET.root"))


# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(1048576),
    fileName = cms.untracked.string('file:step2.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)
process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.hltBitAnalysis,process.endjob_step,process.FEVTDEBUGHLToutput_step)
# process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.endjob_step,process.FEVTDEBUGHLToutput_step)


