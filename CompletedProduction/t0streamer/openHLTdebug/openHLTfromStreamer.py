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
    fileNames = cms.untracked.vstring('root://eoscms.cern.ch//_inputfileflag_'
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
# process.load('Configuration.StandardSequences.MagneticField_38T_cff')
# process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
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
process.hltobject.processName = cms.string('HiForest')
process.hltobject.treeName = cms.string("JetTriggers")  #change this if you want a different tree name
# process.hltbitanalysis.l1GtReadoutRecord = cms.InputTag("hltL1GtObjectMap","","TEST")
process.hltobject.triggerNames = cms.vstring(  "HLT_AK4CaloJet100_Eta5p1_v1",
  "HLT_AK4CaloJet100_Jet35_Eta0p7_v1",
  "HLT_AK4CaloJet100_Jet35_Eta1p1_v1",
  "HLT_AK4CaloJet110_Eta5p1_v1",
  "HLT_AK4CaloJet120_Eta5p1_v1",
  "HLT_AK4CaloJet150_v1",
  "HLT_AK4CaloJet40_Eta5p1_v1",
  "HLT_AK4CaloJet60_Eta5p1_v1",
  "HLT_AK4CaloJet80_45_45_Eta2p1_v1",
  "HLT_AK4CaloJet80_Eta5p1_v1",
  "HLT_AK4CaloJet80_Jet35_Eta0p7_v1",
  "HLT_AK4CaloJet80_Jet35_Eta1p1_v1",
  "HLT_AK4PFBJetBCSV60_Eta2p1_v1",
  "HLT_AK4PFBJetBCSV80_Eta2p1_v1",
  "HLT_AK4PFBJetBSSV60_Eta2p1_v1",
  "HLT_AK4PFBJetBSSV80_Eta2p1_v1",
  "HLT_AK4PFDJet60_Eta2p1_v1",
  "HLT_AK4PFDJet80_Eta2p1_v1",
  "HLT_AK4PFJet100_Eta5p1_v1",
  "HLT_AK4PFJet110_Eta5p1_v1",
  "HLT_AK4PFJet120_Eta5p1_v1",
  "HLT_AK4PFJet40_Eta5p1_v1",
  "HLT_AK4PFJet60_Eta5p1_v1",
  "HLT_AK4PFJet80_Eta5p1_v1",
  "HLT_Activity_Ecal_SC7_v2",
  "HLT_DmesonPPTrackingGlobal_Dpt15_v1",
  "HLT_DmesonPPTrackingGlobal_Dpt20_v1",
  "HLT_DmesonPPTrackingGlobal_Dpt30_v1",
  "HLT_DmesonPPTrackingGlobal_Dpt40_v1",
  "HLT_DmesonPPTrackingGlobal_Dpt50_v1",
  "HLT_DmesonPPTrackingGlobal_Dpt60_v1",
  "HLT_EcalCalibration_v1",
  "HLT_FullTrack12ForEndOfFill_v1",
  "HLT_FullTrack12ForPPRef_v1",
  "HLT_FullTrack18ForPPRef_v1",
  "HLT_FullTrack20_v2",
  "HLT_FullTrack24ForPPRef_v1",
  "HLT_FullTrack34ForPPRef_v1",
  "HLT_FullTrack45ForPPRef_v1",
  "HLT_FullTrack50_v2",
  "HLT_GlobalRunHPDNoise_v2",
  "HLT_HICastorMediumJetPixel_SingleTrack_v1",
  "HLT_HIDoublePhoton15_Eta1p5_Mass50_1000_R9HECut_v1",
  "HLT_HIDoublePhoton15_Eta1p5_Mass50_1000_v1",
  "HLT_HIDoublePhoton15_Eta2p1_Mass50_1000_R9Cut_v1",
  "HLT_HIDoublePhoton15_Eta2p5_Mass50_1000_R9SigmaHECut_v1",
  "HLT_HIL1CastorMediumJet_v1",
  "HLT_HIL1DoubleMu0_v1",
  "HLT_HIL1DoubleMu10_v1",
  "HLT_HIL2DoubleMu0_NHitQ_v1",
  "HLT_HIL2Mu15_v1",
  "HLT_HIL2Mu20_v1",
  "HLT_HIL2Mu3Eta2p5_AK4CaloJet100Eta2p1_v1",
  "HLT_HIL2Mu3Eta2p5_AK4CaloJet40Eta2p1_v1",
  "HLT_HIL2Mu3Eta2p5_AK4CaloJet60Eta2p1_v1",
  "HLT_HIL2Mu3Eta2p5_AK4CaloJet80Eta2p1_v1",
  "HLT_HIL2Mu3Eta2p5_HIPhoton10Eta1p5_v1",
  "HLT_HIL2Mu3Eta2p5_HIPhoton15Eta1p5_v1",
  "HLT_HIL2Mu3Eta2p5_HIPhoton20Eta1p5_v1",
  "HLT_HIL2Mu3Eta2p5_HIPhoton30Eta1p5_v1",
  "HLT_HIL2Mu3Eta2p5_HIPhoton40Eta1p5_v1",
  "HLT_HIL2Mu3_NHitQ10_v1",
  "HLT_HIL2Mu5_NHitQ10_v1",
  "HLT_HIL2Mu7_NHitQ10_v1",
  "HLT_HIL3DoubleMu0_OS_m2p5to4p5_v1",
  "HLT_HIL3DoubleMu0_OS_m7to14_v1",
  "HLT_HIL3Mu15_v1",
  "HLT_HIL3Mu20_v1",
  "HLT_HIL3Mu3_NHitQ15_v1",
  "HLT_HIL3Mu5_NHitQ15_v1",
  "HLT_HIL3Mu7_NHitQ15_v1",
  "HLT_HISinglePhoton10_Eta1p5_v1",
  "HLT_HISinglePhoton10_Eta3p1_v1",
  "HLT_HISinglePhoton15_Eta1p5_v1",
  "HLT_HISinglePhoton15_Eta3p1_v1",
  "HLT_HISinglePhoton20_Eta1p5_v1",
  "HLT_HISinglePhoton20_Eta3p1_v1",
  "HLT_HISinglePhoton30_Eta1p5_v1",
  "HLT_HISinglePhoton30_Eta3p1_v1",
  "HLT_HISinglePhoton40_Eta1p5_v1",
  "HLT_HISinglePhoton40_Eta3p1_v1",
  "HLT_HISinglePhoton50_Eta1p5_v1",
  "HLT_HISinglePhoton50_Eta3p1_v1",
  "HLT_HISinglePhoton60_Eta1p5_v1",
  "HLT_HISinglePhoton60_Eta3p1_v1",
  "HLT_HIUPCDoubleMuNotHF2Pixel_SingleTrack_v1",
  "HLT_HIUPCL1DoubleMuOpenNotHF2_v1",
  "HLT_HIUPCL1MuOpen_NotMinimumBiasHF2_AND_v1",
  "HLT_HIUPCL1NotMinimumBiasHF2_AND_v1",
  "HLT_HIUPCL1NotZdcOR_BptxAND_v1",
  "HLT_HIUPCL1ZdcOR_BptxAND_v1",
  "HLT_HIUPCL1ZdcXOR_BptxAND_v1",
  "HLT_HIUPCMuOpen_NotMinimumBiasHF2_ANDPixel_SingleTrack_v1",
  "HLT_HIUPCNotMinimumBiasHF2_ANDPixel_SingleTrack_v1",
  "HLT_HIUPCNotZdcOR_BptxANDPixel_SingleTrack_v1",
  "HLT_HIUPCZdcOR_BptxANDPixel_SingleTrack_v1",
  "HLT_HIUPCZdcXOR_BptxANDPixel_SingleTrack_v1",
  "HLT_HcalCalibration_v1",
  "HLT_HcalNZS_v2",
  "HLT_HcalPhiSym_v2",
  "HLT_HcalUTCA_v2",
  "HLT_IsoTrackHB_v1",
  "HLT_IsoTrackHE_v1",
  "HLT_L1CastorHighJet_v1",
  "HLT_L1CastorMediumJet_v1",
  "HLT_L1MinimumBiasHF1AND_v1",
  "HLT_L1MinimumBiasHF1OR_part0_v1",
  "HLT_L1MinimumBiasHF1OR_part10_v1",
  "HLT_L1MinimumBiasHF1OR_part11_v1",
  "HLT_L1MinimumBiasHF1OR_part12_v1",
  "HLT_L1MinimumBiasHF1OR_part13_v1",
  "HLT_L1MinimumBiasHF1OR_part14_v1",
  "HLT_L1MinimumBiasHF1OR_part15_v1",
  "HLT_L1MinimumBiasHF1OR_part16_v1",
  "HLT_L1MinimumBiasHF1OR_part17_v1",
  "HLT_L1MinimumBiasHF1OR_part18_v1",
  "HLT_L1MinimumBiasHF1OR_part19_v1",
  "HLT_L1MinimumBiasHF1OR_part1_v1",
  "HLT_L1MinimumBiasHF1OR_part2_v1",
  "HLT_L1MinimumBiasHF1OR_part3_v1",
  "HLT_L1MinimumBiasHF1OR_part4_v1",
  "HLT_L1MinimumBiasHF1OR_part5_v1",
  "HLT_L1MinimumBiasHF1OR_part6_v1",
  "HLT_L1MinimumBiasHF1OR_part7_v1",
  "HLT_L1MinimumBiasHF1OR_part8_v1",
  "HLT_L1MinimumBiasHF1OR_part9_v1",
  "HLT_L1MinimumBiasHF2AND_v1",
  "HLT_L1MinimumBiasHF2ORNoBptxGating_v1",
  "HLT_L1MinimumBiasHF2OR_v1",
  "HLT_L1SingleEG5_OR_EG20_v2",
  "HLT_L1SingleMuOpen_DT_v2",
  "HLT_L1SingleMuOpen_v2",
  "HLT_L1TOTEM0_RomanPotsAND_v1",
  "HLT_L1TOTEM1_MinBias_v1",
  "HLT_L1TOTEM2_ZeroBias_v1",
  "HLT_L1Tech5_BPTX_PlusOnly_v2",
  "HLT_L1Tech6_BPTX_MinusOnly_v1",
  "HLT_L1Tech7_NoBPTX_v1",
  "HLT_L1Tech_DT_GlobalOR_v2",
  "HLT_Physics_v2",
  "HLT_PixelTracks_Multiplicity110_v2",
  "HLT_PixelTracks_Multiplicity135_v2",
  "HLT_PixelTracks_Multiplicity160_v2",
  "HLT_PixelTracks_Multiplicity60_v2",
  "HLT_PixelTracks_Multiplicity85_v2")
process.hltobject.triggerResults = process.hltbitanalysis.hltresults
process.hltobject.triggerEvent = cms.InputTag("TriggerResults","",'HiForest')
process.hltbitanalysis.l1GtReadoutRecord = cms.InputTag("gtDigis","","HiForest")

process.hltBitAnalysis = cms.EndPath(process.RawToDigi*process.L1Reco*process.hltbitanalysis*process.hltobject)


