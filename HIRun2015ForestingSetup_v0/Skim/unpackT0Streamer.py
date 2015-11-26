import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')
process.options = cms.untracked.PSet(
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
                 
                 
process.source = cms.Source("NewEventStreamFileReader",
    fileNames = cms.untracked.vstring(options.inputFiles[0])
)

# Other statements

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_dataRun2_ExpressHI_v2', '')



process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents))



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


# process.load("HLTrigger.HLTfilters.hltHighLevel_cfi")
# process.hltMinBiasUPC          = process.hltHighLevel.clone()
# process.hltMinBiasUPC.HLTPaths = ["HLT_HIL1Centralityext70100HFplusANDminusTH0_v1"
                                  # ]

# process.GoodEventFilterSequence       = cms.Sequence(process.hltMinBiasUPC)

# filter all path with the good event filter sequence
# for path in process.paths:
	# getattr(process,path)._seq = process.GoodEventFilterSequence * getattr(process,path)._seq 


process.makeEdm = cms.OutputModule("PoolOutputModule",
                                         dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('USER')),
          outputCommands = cms.untracked.vstring('keep *'),
          SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring(
            'HLT_HIL1Centralityext70100HFplusANDminusTH0_v1' ) ),
          fileName = cms.untracked.string(options.outputFile))



process.this_is_the_end = cms.EndPath( process.makeEdm )
  
  
  