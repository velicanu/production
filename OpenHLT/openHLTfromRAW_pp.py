import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')
process.options = cms.untracked.PSet(
)

#####################################################################################
# Input source
#####################################################################################
                            
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                "file:/afs/cern.ch/work/v/velicanu/public/forest/data/Run2015E-HighPtJet80-RAW-262328-9A8A376B-1893-E511-8CC7-02163E014143.root"
                                # "file:/afs/cern.ch/work/v/velicanu/public/forest/data/HIRun2015-HIEWQExo-RAW-263379-F235E44E-AF9F-E511-B693-02163E0124FA.root"
                            )
)


# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10))



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
# process.load('Configuration.StandardSequences.RawToDigi_Repacked_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

# PbPb 53X MC

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#fixme
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_dataRun2_Prompt_ppAt5TeV_v1', '')
# process.GlobalTag = GlobalTag(process.GlobalTag, '75X_dataRun2_PromptHI_v3', '')


process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("HiForestAOD.root"))
process.p = cms.Path(
    process.gtDigis +
    process.hltanalysis
)
#process.this_is_the_end = cms.EndPath(
#  process.hltanalysis
#)
