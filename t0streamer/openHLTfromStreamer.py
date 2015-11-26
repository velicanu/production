import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')
process.options = cms.untracked.PSet(
)

#####################################################################################
# Input source
#####################################################################################
                            
process.source = cms.Source("NewEventStreamFileReader",
    fileNames = cms.untracked.vstring('root://eoscms.cern.ch///store/t0streamer/Data/Express/000/261/396/run261396_ls0001_streamExpress_StorageManager.dat'
  )
)


# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1))



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
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_dataRun2_ExpressHI_v2', '')


process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')
process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("HiForestAOD.root"))
process.this_is_the_end = cms.EndPath(
  process.hltanalysis
)
