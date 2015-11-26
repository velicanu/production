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



##########################################JEC##########################################
from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import overrideJEC_PbPb5020
process = overrideJEC_PbPb5020(process)
##########################################JEC##########################################


##########################################UE##########################################
from CondCore.DBCommon.CondDBSetup_cfi import *
process.uetable = cms.ESSource("PoolDBESSource",
      DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0)
        ),
      timetype = cms.string('runnumber'),
      toGet = cms.VPSet(
          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("UETableCompatibilityFormat_Calo_v00_express"),
                   label = cms.untracked.string("UETable_PF")
          ),
          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("UETableCompatibilityFormat_PF_v00_express"),
                   label = cms.untracked.string("UETable_Calo")
          )
      ), 
      connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
)
process.es_prefer_uetable = cms.ESPrefer('PoolDBESSource','uetable')
##########################################UE##########################################



process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")

# process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
# process.GlobalTag.toGet.extend([
  # cms.PSet(record = cms.string("HeavyIonRcd"),
     # tag = cms.string("CentralityTable_HFtowers200_Glauber2015A_v750x01_offline"),
     # connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
     # label = cms.untracked.string("HFtowers")
  # ),
# ])

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                  fileName=cms.string("blah.root"))                                   
# fileName=cms.string("HiForest_test_pp_Express.root"))

#####################################################################################
# Additional Reconstruction and Analysis: Main Body
#####################################################################################



process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu3CaloJetSequence_PbPb_data_bTag_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs3CaloJetSequence_PbPb_data_bTag_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_PbPb_data_bTag_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs3PFJetSequence_PbPb_data_bTag_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_PbPb_data_bTag_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs4CaloJetSequence_PbPb_data_bTag_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_PbPb_data_bTag_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs4PFJetSequence_PbPb_data_bTag_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu5CaloJetSequence_PbPb_data_bTag_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs5CaloJetSequence_PbPb_data_bTag_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu5PFJetSequence_PbPb_data_bTag_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs5PFJetSequence_PbPb_data_bTag_cff')


process.jetSequences = cms.Sequence(
# process.ak3CaloJetSequence +
                                    # process.ak3PFJetSequence +
                                    process.akVs3CaloJetSequence +
                                    process.akPu3CaloJetSequence +
                                    process.akVs3PFJetSequence +
                                    process.akPu3PFJetSequence +
                                    process.akVs4CaloJetSequence +
                                    process.akPu4CaloJetSequence +
                                    process.akVs4PFJetSequence +
                                    process.akPu4PFJetSequence +
                                    process.akVs5CaloJetSequence +
                                    process.akPu5CaloJetSequence +
                                    process.akVs5PFJetSequence +
                                    process.akPu5PFJetSequence
                                    # process.ak4CaloJetSequence +
                                    # process.ak4PFJetSequence

                                    # process.akPu5CaloJetSequence +
                                    # process.akVs5CaloJetSequence +
                                    # process.akVs5PFJetSequence +
                                    # process.akPu5PFJetSequence

                                    )
                                    
                                    
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')
############ hlt oject
process.load("HeavyIonsAnalysis.EventAnalysis.hltobject_cfi")
process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")
process.hltbitanalysis.l1GtReadoutRecord = cms.InputTag("gtDigis","","HLT")

#####################################################################################
# To be cleaned

process.load('HeavyIonsAnalysis.JetAnalysis.ExtraTrackReco_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_cff')
process.load("HeavyIonsAnalysis.TrackAnalysis.METAnalyzer_cff")
process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzer_cfi")
process.pfcandAnalyzer.skipCharged = False
process.pfcandAnalyzer.pfPtMin = 0

#####################################################################################
#########################
# HLTMuTree Analyzer
#########################
process.load('HeavyIonsAnalysis.MuonAnalysis.hltMuTree_cfi')
# process.hltMuTree.vertices = cms.InputTag("offlinePrimaryVertices")
process.hltMuTree.vertices = cms.InputTag("hiSelectedVertex")

#########################
# Track Analyzer
#########################
process.anaTrack.qualityStrings = cms.untracked.vstring(['highPurity','tight','loose'])

process.pixelTrack.qualityStrings = cms.untracked.vstring('highPurity')
process.hiTracks.cut = cms.string('quality("highPurity")')

# set track collection to iterative tracking
process.anaTrack.trackSrc = cms.InputTag("hiGeneralTracks")


#####################
# L1 Digis
#####################

process.load('L1Trigger.L1TCalorimeter.caloConfigStage1HI_cfi')
process.load('L1Trigger.L1TCalorimeter.L1TCaloStage1_cff')
process.load('L1Trigger.L1TCalorimeter.caloStage1Params_HI_cfi')
process.caloStage1Params.minimumBiasThresholds = cms.vint32(1,1,2,2)

process.simRctUpgradeFormatDigis.emTag = cms.InputTag("caloStage1Digis")
process.simRctUpgradeFormatDigis.regionTag = cms.InputTag("caloStage1Digis")

process.load('EventFilter.L1TRawToDigi.caloStage1Digis_cfi')
process.caloStage1Digis.InputLabel = cms.InputTag("rawDataRepacker")

process.L1Sequence = cms.Sequence(
    process.caloStage1Digis +
    process.simRctUpgradeFormatDigis +
    process.simCaloStage1Digis +
    process.simCaloStage1FinalDigis
    )



process.EmulatorResults = cms.EDAnalyzer('l1t::L1UpgradeAnalyzer',
                                         InputLayer2Collection = cms.InputTag("simCaloStage1FinalDigis"),
                                         InputLayer2TauCollection = cms.InputTag("simCaloStage1FinalDigis:rlxTaus"),
                                         InputLayer2IsoTauCollection = cms.InputTag("simCaloStage1FinalDigis:isoTaus"),
                                         InputLayer2CaloSpareCollection = cms.InputTag("simCaloStage1FinalDigis:HFRingSums"),
                                         InputLayer2HFBitCountCollection = cms.InputTag("simCaloStage1FinalDigis:HFBitCounts"),
                                         InputLayer1Collection = cms.InputTag("None"),
                                         legacyRCTDigis = cms.InputTag("None")
)

process.UnpackerResults = cms.EDAnalyzer('l1t::L1UpgradeAnalyzer',
                                         InputLayer2Collection = cms.InputTag("caloStage1Digis"),
                                         InputLayer2TauCollection = cms.InputTag("caloStage1Digis:rlxTaus"),
                                         InputLayer2IsoTauCollection = cms.InputTag("caloStage1Digis:isoTaus"),
                                         InputLayer2CaloSpareCollection = cms.InputTag("caloStage1Digis:HFRingSums"),
                                         InputLayer2HFBitCountCollection = cms.InputTag("caloStage1Digis:HFBitCounts"),
                                         InputLayer1Collection = cms.InputTag("simRctUpgradeFormatDigis"),
                                         legacyRCTDigis = cms.InputTag("caloStage1Digis")
)


process.L1EmulatorUnpacker = cms.Sequence(process.UnpackerResults + process.EmulatorResults)

AddCaloMuon = False
runOnMC = False
HIFormat = False
UseGenPlusSim = False
VtxLabel = "hiSelectedVertex"
TrkLabel = "hiGeneralTracks"
from Bfinder.finderMaker.finderMaker_75X_cff import finderMaker_75X
finderMaker_75X(process, AddCaloMuon, runOnMC, HIFormat, UseGenPlusSim, VtxLabel, TrkLabel)


process.load('HeavyIonsAnalysis.JetAnalysis.rechitanalyzer_cfi')
process.rechitanalyzer.doVS = cms.untracked.bool(True)
process.rechitanalyzer.useJets = cms.untracked.bool(False)
process.rechitanalyzer.EBTreePtMin = -9999
process.rechitanalyzer.EETreePtMin = -9999
process.rechitanalyzer.HBHETreePtMin = -9999
process.rechitanalyzer.HFTreePtMin = -9999
process.rechitanalyzer.HFlongMin = -9999
process.rechitanalyzer.HFshortMin = -9999
process.rechitanalyzer.HFtowerMin = -9999

import HLTrigger.HLTfilters.hltHighLevel_cfi

process.hltMinBias = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltMinBias.HLTPaths = ["HLT_HIL1MinimumBiasHF1AND_v1"]



process.write_FEVT = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('FEVT'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('ana_step')),
    fileName = cms.untracked.string(options.outputFile),
    outputCommands = cms.untracked.vstring( ('drop *', 
        'drop *', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'keep  FEDRawDataCollection_rawDataCollector_*_*', 
        'keep  FEDRawDataCollection_source_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep FEDRawDataCollection_rawDataCollector_*_*', 
        'keep FEDRawDataCollection_source_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hbheprereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_*Digis_*_*', 
        'keep ZDCRecHitsSorted_*_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_*_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep recoCaloClusters_islandBasicClusters_*_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_rsWithMaterialTracks_*_*', 
        'keep recoTrackExtras_rsWithMaterialTracks_*_*', 
        'keep TrackingRecHitsOwned_rsWithMaterialTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep floatedmValueMap_generalTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRho*_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep *HaloData_*_*_*', 
        'keep *BeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_SETMuonSeed_*_*', 
        'keep recoTracks_standAloneSETMuons_*_*', 
        'keep recoTrackExtras_standAloneSETMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneSETMuons_*_*', 
        'keep recoTracks_globalSETMuons_*_*', 
        'keep recoTrackExtras_globalSETMuons_*_*', 
        'keep TrackingRecHitsOwned_globalSETMuons_*_*', 
        'keep recoMuons_muonsWithSET_*_*', 
        'keep *_muons_*_*', 
        'keep *_*_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_impactParameterTagInfos_*_*', 
        'keep *_trackCountingHighEffBJetTags_*_*', 
        'keep *_trackCountingHighPurBJetTags_*_*', 
        'keep *_jetProbabilityBJetTags_*_*', 
        'keep *_jetBProbabilityBJetTags_*_*', 
        'keep *_secondaryVertexTagInfos_*_*', 
        'keep *_inclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_ghostTrackVertexTagInfos_*_*', 
        'keep *_simpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_simpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_combinedSecondaryVertexBJetTags_*_*', 
        'keep *_combinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_ghostTrackBJetTags_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_softMuonTagInfos_*_*', 
        'keep *_softMuonBJetTags_*_*', 
        'keep *_softMuonByIP3dBJetTags_*_*', 
        'keep *_softMuonByPtBJetTags_*_*', 
        'keep *_combinedMVABJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfTrackCountingHighPurBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleSecondaryVertexHighPurBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedMVABJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexSoftLeptonBJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_ak4PFJetsRecoTauPiZeros_*_*', 
        'keep *_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscrimination*_*_*', 
        'keep *_hpsPFTau*PtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep  *_offlinePrimaryVerticesWithBS_*_*', 
        'keep  *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep  *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'drop *_egmGsfElectronIDs_*_*', 
        'drop *_egmPhotonIDs_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTracks_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFrom*Conversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFrom*Conversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFrom*Conversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep *_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep recoHIPhotonIsolationedmValueMap_photonIsolationHIProducerppGED_*_*', 
        'keep recoHIPhotonIsolationedmValueMap_photonIsolationHIProducerpp_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFEM_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHFHAD_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'drop *_hlt*_*_*', 
        'keep *_hltL1GtObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1TriggerScalerss_*_*_*', 
        'keep Level1TriggerScalerss_*_*_*', 
        'keep LumiScalerss_*_*_*', 
        'keep BeamSpotOnlines_*_*_*', 
        'keep DcsStatuss_*_*_*', 
        'keep *_tcdsDigis_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfJetTrackAssociatorEI_*_*', 
        'keep *_impactParameterTagInfosEI_*_*', 
        'keep *_secondaryVertexTagInfosEI_*_*', 
        'keep *_combinedSecondaryVertexBJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscrimination*_*_*', 
        'keep *_pfMetEI_*_*', 
        'keep int_bunchSpacingProducer_*_*', 
        'keep *_hiGeneralTracks_*_*', 
        'keep *_hiGeneralAndPixelTracks_*_*', 
        'keep *_hiPixel3PrimTracks_*_*', 
        'keep *_hiPixel3ProtoTracks_*_*', 
        'keep *_hiSelectedProtoTracks_*_*', 
        'keep recoVertexs_hiPixelMedianVertex_*_*', 
        'keep recoVertexs_hiPixelAdaptiveVertex_*_*', 
        'keep recoVertexs_hiSelectedVertex_*_*', 
        'keep recoVertexs_hiPixelClusterVertex_*_*', 
        'keep *_*_APVCM_*', 
        'keep *_siStripZeroSuppression_BADAPVBASELINE_*', 
        'keep SiStripRawDigiedmDetSetVector_siStripZeroSuppression_VirginRaw_*', 
        'keep *_*CaloJets_*_*', 
        'keep *_*PFJets_*_*', 
        'keep *_*HiGenJets_*_*', 
        'keep *_*voronoiBackground*_*_*', 
        'keep *_*PFTowers_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep EcalRecHitsSorted_*_*_*', 
        'keep floatedmValueMap_*_*_*', 
        'keep recoPFCandidates_*_*_*', 
        'drop recoPFClusters_*_*_*', 
        'keep recoElectronSeeds_*_*_*', 
        'keep recoGsfElectrons_*_*_*', 
        'keep recoHIPhotonIsolationedmValueMap_photonIsolationHIProducer_*_*', 
        'keep recoPhotons_gedPhotonsTmp_*_*', 
        'keep recoHIPhotonIsolationedmValueMap_photonIsolationHIProducerGED_*_*', 
        'keep recoElectronSeeds_ecalDrivenElectronSeeds_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep recoEvtPlanes_hiEvtPlane_*_*', 
        'keep recoCentrality*_hiCentrality_*_*', 
        'keep *_centralityBin_*_*', 
        'keep recoClusterCompatibility*_hiClusterCompatibility_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_mergedStandAloneMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_reglobalMuons_*_*', 
        'keep TrackingRecHitsOwned_retevMuons_*_*', 
        'keep recoCaloMuons_recalomuons_*_*', 
        'keep *_remuons_*_*', 
        'keep *_*_remuons_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_reglobalMuons_*_*', 
        'keep recoTrackExtras_reglobalMuons_*_*', 
        'keep recoTracks_retevMuons_*_*', 
        'keep recoTrackExtras_retevMuons_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_retevMuons_*_*', 
        'keep FEDRawDataCollection_rawDataRepacker_*_*', 
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*' ) ),
    splitLevel = cms.untracked.int32(0)
)



#####################

# photons
process.load('HeavyIonsAnalysis.PhotonAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.doGenParticles = False
process.ggHiNtuplizerGED = process.ggHiNtuplizer.clone(recoPhotonSrc = cms.InputTag('gedPhotonsTmp'),
                                                       recoPhotonHiIsolationMap = cms.InputTag('photonIsolationHIProducerGED')
                                                       )



process.ana_step = cms.Path(
                            process.hltanalysis *
                            # process.hltobject +
                            # process.centralityBin * 
                            # process.hiEvtAnalyzer*
                            # process.jetSequences +
                            # process.ggHiNtuplizer +
                            # process.ggHiNtuplizerGED +
                            # process.pfcandAnalyzer +
                            # process.L1Sequence +
                            # process.L1EmulatorUnpacker +
                            # process.finderSequence +
                            # process.rechitanalyzer +
                            # process.hltMuTree + 
                            process.HiForest
                            # process.anaTrack
                            )


process.pAna = cms.EndPath(process.write_FEVT)
# process.pAna = cms.Path(process.skimanalysis)

# Customization

# filter all path with the production filter sequence
for path in process.paths:
    getattr(process,path)._seq = process.hltMinBias * getattr(process,path)._seq

    
    
