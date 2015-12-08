import FWCore.ParameterSet.Config as cms

process = cms.Process('hiForestAna2011')

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

#####################################################################################
# Input source
#####################################################################################

process.source = cms.Source("PoolSource",
 duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    fileNames = cms.untracked.vstring(
    '/store/hidata/HIRun2011/HIHighPt/RECO/PromptReco-v1/000/181/611/7C1B26DC-0E10-E111-9CEF-003048F117F6.root'
#    'file:rereco/EED77885-BAF8-E011-B6B7-001D09F2532F.root'
    ))

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
            input = cms.untracked.int32(-1))


#####################################################################################
# Load some general stuff
#####################################################################################

process.load("HLTrigger.HLTfilters.hltHighLevel_cfi")
process.photonFilter = process.hltHighLevel.clone()
process.photonFilter.HLTPaths = ["HLT_HISinglePhoton30_v*"]


process.singlePhotonPt35Filter = cms.EDFilter("PhotonSelector",
                                             src = cms.InputTag("photons"),
                                             cut = cms.string('pt > 35 && abs(eta) < 1.48 && sigmaIetaIeta > 0.002' ),
                                             filter = cms.bool(True)
                                             )
                                             
process.superFilterSequence = cms.Sequence(process.photonFilter*process.singlePhotonPt35Filter)
process.superFilterPath = cms.Path(process.superFilterSequence)

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryExtended_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('RecoLocalTracker.SiPixelRecHits.PixelCPEESProducers_cff')
# Data Global Tag 44x 
process.GlobalTag.globaltag = 'GR_P_V27A::All'

# MC Global Tag 44x 
#process.GlobalTag.globaltag = 'STARTHI44_V4::All'

# load centrality
from CmsHi.Analysis2010.CommonFunctions_cff import *
overrideCentrality(process)
process.HeavyIonGlobalParameters = cms.PSet(
	centralityVariable = cms.string("HFtowers"),
	nonDefaultGlauberModel = cms.string(""),
	centralitySrc = cms.InputTag("hiCentrality")
	)

process.load('RecoHI.HiCentralityAlgos.HiCentrality_cfi')

# EcalSeverityLevel ES Producer
process.load("RecoLocalCalo/EcalRecAlgos/EcalSeverityLevelESProducer_cfi")
process.load("RecoEcal.EgammaCoreTools.EcalNextToDeadChannelESProducer_cff")


#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                  fileName=cms.string("HiForest.root"))

#####################################################################################
# Jet energy correction
#####################################################################################

#####################################################################################
# Additional Reconstruction and Analysis
#####################################################################################

# MET: Calorimeter based MET
process.load("RecoMET.METProducers.CaloMET_cfi") 

# Define Analysis sequencues
process.load('CmsHi.JetAnalysis.EventSelection_cff')
#process.load('CmsHi.JetAnalysis.ExtraGenReco_cff')
#process.load('CmsHi.JetAnalysis.ExtraTrackReco_cff')
process.load('CmsHi.JetAnalysis.ExtraPfReco_cff')
process.load('CmsHi.JetAnalysis.ExtraJetReco_cff')
process.load('CmsHi.JetAnalysis.ExtraEGammaReco_cff')
process.load('CmsHi.JetAnalysis.PatAna_cff')
process.load('CmsHi.JetAnalysis.JetAnalyzers_cff')
process.load('CmsHi.JetAnalysis.EGammaAnalyzers_cff')
process.load("MitHig.PixelTrackletAnalyzer.trackAnalyzer_cff")
process.anaTrack.trackPtMin = 0
process.anaTrack.useQuality = True
process.anaTrack.doPFMatching = True
process.anaTrack.trackSrc = cms.InputTag("hiSelectedTracks")
process.load("MitHig.PixelTrackletAnalyzer.METAnalyzer_cff")
process.load("CmsHi.JetAnalysis.pfcandAnalyzer_cfi")
process.pfcandAnalyzer.skipCharged = False
process.pfcandAnalyzer.pfPtMin = 0
process.interestingTrackEcalDetIds.TrackCollection = cms.InputTag("hiSelectedTracks")
process.akPu3CaloJetAnalyzer.isMC = False
process.akPu5CaloJetAnalyzer.isMC = False
process.akPu3PFJetAnalyzer.isMC = False
process.akPu5PFJetAnalyzer.isMC = False
# Muons 
process.load("MuTrig.HLTMuTree.hltMuTree_cfi")
process.muonTree = process.hltMuTree.clone()
process.muonTree.doGen = cms.untracked.bool(False)

# Event tree
process.load("CmsHi/HiHLTAlgos.hievtanalyzer_cfi")
# Not working for the moment..
process.hiEvtAnalyzer.doMC = cms.bool(False)
process.hiEvtAnalyzer.doEvtPlane = cms.bool(True)

process.ak5CaloJets = process.akPu5CaloJets.clone(doPUOffsetCorr = False)
process.ak5corr = process.icPu5corr.clone(
        src = cms.InputTag("ak5CaloJets"),
            payload = cms.string('AK5Calo')
            )
process.ak5patJets = process.akPu5PFpatJets.clone(
        jetSource = cms.InputTag("ak5CaloJets"),
            jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak5corr"))
            )
	    
#process.icPu5JetAnalyzer.hltTrgResults = cms.untracked.string('TriggerResults::RECO')
#process.akPu3PFJetAnalyzer.hltTrgResults = cms.untracked.string('TriggerResults::RECO')
process.icPu5JetAnalyzer.useCentrality   = cms.untracked.bool(False) # doesn't fill cent info
process.akPu3PFJetAnalyzer.useCentrality = cms.untracked.bool(False) # doesn't fill cent info

process.ak5CaloJetAnalyzer = process.icPu5JetAnalyzer.clone(
    jetTag = 'ak5patJets',
    genjetTag = 'ak5HiGenJets',
    isMC = False
    )

process.ak3PFJetsX = process.akPu3PFJets.clone(doPUOffsetCorr = False)
process.ak3corrX = process.icPu5corr.clone(
    src = cms.InputTag("ak3PFJetsX"),
    payload = cms.string('AK3PF')
    )
process.ak3patJetsX = process.akPu5PFpatJets.clone(
    jetSource = cms.InputTag("ak3PFJetsX"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak3corrX"))
    )
process.ak3PFJetAnalyzer = process.icPu5JetAnalyzer.clone(
    jetTag = 'ak3patJetsX',
    genjetTag = 'ak3HiGenJets',
    isMC = False
    )

process.ak5extra = cms.Sequence(process.ak5CaloJets*process.ak5corr*process.ak5patJets*process.ak5CaloJetAnalyzer)
process.ak3extra = cms.Sequence(process.ak3PFJetsX*process.ak3corrX*process.ak3patJetsX*process.ak3PFJetAnalyzer)

#process.load("edwenger.Skims.EventFilter_cff")
#from edwenger.Skims.customise_cfi import *
#run2760GeVmode(process)

# Filtering
process.hltJetHI.HLTPaths = ['HLT_HIJet35U','HLT_HIPhoton20']
#process.hltJetHI.TriggerResultsTag = cms.InputTag("TriggerResults::RECO")

print "Add cleaning to analysis"
process.event_filter_seq = cms.Sequence(
  process.hltJetHI * 
  process.siPixelRecHits *
  process.collisionEventSelection *
  process.HBHENoiseFilter *
  process.hiEcalRecHitSpikeFilter 

#  process.preTrgTest *
#  process.minBiasBscFilter *
#  process.postTrgTest *
#  process.hfCoincFilter *
#  process.purityFractionFilter

  )

#Commented by Yen-Jie
#process.hiPixelAdaptiveVertex.useBeamConstraint = False

process.load("RecoHI.HiMuonAlgos.HiRecoMuon_cff")
process.muons.JetExtractorPSet.JetCollectionLabel = cms.InputTag("iterativeConePu5CaloJets")

process.load("UserCode.L1TriggerDPG.l1NtupleProducer_cfi")

#process.hiGoodTightTracks.src = cms.InputTag("hiGlobalPrimTracks")
#process.hiGoodTightTracksDirect = process.hiGoodTightTracks.clone(keepAllTracks = True)
#process.hiGoodTracks = process.hiGoodTightTracks.clone()
process.akPu5PFJets.doAreaFastjet = False
process.akPu3PFJets.doAreaFastjet = False
process.iterativeConePu5CaloJets.doAreaFastjet = False
process.akPu5PFJets.doRhoFastjet = False
process.akPu3PFJets.doRhoFastjet = False
# process.iterativeCONEPu5CaloJets.doRhoFastjet = False

#process.hiSelectedTrackHighPurity = cms.EDProducer("QualityFilter",
#      TrackQuality = cms.string('highPurity'),
#      recTracks = cms.InputTag("hiSelectedTracks")
#)

process.hiSelectedTrackHighPurity = cms.EDFilter("TrackSelector",
   src = cms.InputTag("hiSelectedTracks"),
   cut = cms.string(
   'quality("highPurity")')
)

process.particleFlowClusterPS.thresh_Pt_Seed_Endcap = cms.double(99999.)
process.reco_extra        = cms.Path( process.siPixelRecHits * process.siStripMatchedRecHits *
                                      process.hiPixel3PrimTracks *
                                      process.hiPixelTrackSeeds *
                                      process.hiSelectedTrackHighPurity *
                                      process.electronGsfTrackingHi *
                                      process.hiElectronSequence *
                                      process.HiParticleFlowReco *
                                      process.iterativeConePu5CaloJets *
                                      process.PFTowers 
                                      )

process.reco_extra_jet    = cms.Path( process.iterativeConePu5CaloJets *
                                      process.akPu3PFJets * process.akPu5PFJets *
                                      process.akPu3CaloJets * process.akPu5CaloJets *
                                      process.photon_extra_reco)
#process.gen_step          = cms.Path( process.hiGenParticles * process.hiGenParticlesForJets * process.genPartons * process.hiPartons * process.hiRecoGenJets)
process.pat_step          = cms.Path(process.icPu5patSequence_data +
                                     process.akPu3PFpatSequence_data + process.akPu5PFpatSequence_data +
                                     process.akPu3patSequence_data + process.akPu5patSequence_data +
                                     process.makeHeavyIonPhotons)
process.pat_step.remove(process.interestingTrackEcalDetIds)
process.pat_step.remove(process.photonMatch)
#+ process.patPhotons)

process.patPhotons.addPhotonID = cms.bool(False)
#process.makeHeavyIonPhotons)
process.extrapatstep = cms.Path(process.selectedPatPhotons)
process.load("CmsHi.JetAnalysis.hcalNoise_cff")
process.load("CmsHi.JetAnalysis.RandomCones_cff")
process.akPu3PFConesAna.doMC = cms.untracked.bool(False)
process.akPu5PFConesAna.doMC = cms.untracked.bool(False)
process.akPu3CaloConesAna.doMC = cms.untracked.bool(False)
process.akPu5CaloConesAna.doMC = cms.untracked.bool(False)
process.icPu5CaloConesAna.doMC = cms.untracked.bool(False)

process.multiPhotonAnalyzer.GammaEtaMax = cms.untracked.double(100)
process.multiPhotonAnalyzer.GammaPtMin = cms.untracked.double(0)
process.multiPhotonAnalyzer.gsfElectronCollection = cms.untracked.InputTag("ecalDrivenGsfElectrons")
process.ana_step          = cms.Path( process.jetana_seq +
                                      process.multiPhotonAnalyzer + process.anaTrack + process.pfcandAnalyzer +
                                      process.met * process.anaMET +
                                      process.muonTree +
                                      process.hcalNoise +
                                      process.hiEvtAnalyzer +
                                      process.randomCones
                                      )

process.phltJetHI = cms.Path( process.hltJetHI )
process.pcollisionEventSelection = cms.Path(process.collisionEventSelection)
process.pHBHENoiseFilter = cms.Path( process.HBHENoiseFilter )
process.phiEcalRecHitSpikeFilter = cms.Path(process.hiEcalRecHitSpikeFilter )
#process.ppreTrgTest = cms.Path(process.preTrgTest )
#process.pminBiasBscFilter = cms.Path(process.minBiasBscFilter )
#process.ppostTrgTest = cms.Path(process.postTrgTest )
#process.phfCoincFilter = cms.Path(process.hfCoincFilter )
#process.ppurityFractionFilter = cms.Path(process.purityFractionFilter )

# Customization
from CmsHi.JetAnalysis.customise_cfi import *
enableDataPat(process)
setPhotonObject(process,"cleanPhotons")
enableDataAnalyzers(process)

# process.load('HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi')
# process.hltbitanalysis.UseTFileService                  = cms.untracked.bool(True)
# process.hltanalysis = process.hltbitanalysis.clone(
   # l1GtReadoutRecord            = cms.InputTag("gtDigis"),
   # l1GctHFBitCounts     = cms.InputTag("gctDigis"),
   # l1GctHFRingSums      = cms.InputTag("gctDigis"),
   # l1extramu            = cms.string('l1extraParticles'),
   # l1extramc            = cms.string('l1extraParticles'),
   # hltresults           = cms.InputTag("TriggerResults","","HLT"),
   # HLTProcessName       = cms.string("HLT")
  # )
  
process.load('HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi')
process.hltbitanalysis.UseTFileService                  = cms.untracked.bool(True)
process.hltanalysis = process.hltbitanalysis.clone(
  dummyBranches = cms.untracked.vstring(),
  l1GtReadoutRecord    = cms.InputTag("gtDigis"),
  l1GctHFBitCounts     = cms.InputTag("gctDigis"),
  l1GctHFRingSums      = cms.InputTag("gctDigis"),
  l1extramu            = cms.string('l1extraParticles'),
  l1extramc            = cms.string('l1extraParticles'),
  hltresults           = cms.InputTag("TriggerResults","","HLT"),
  HLTProcessName       = cms.string("HLT")
 )
process.hltanalysis.dummyBranches.extend( [
  "HLT_HIL1DoubleMu0_HighQ_v1",
  "HLT_HIL1DoubleMuOpen_v1",
  "HLT_HIL2DoubleMu0_L1HighQL2NHitQ_v1",
  "HLT_HIL2DoubleMu0_NHitQ_v1",
  "HLT_HIL2DoubleMu0_v1",
  "HLT_HIL2DoubleMu3_v1",
  "HLT_HIL2Mu15_v1",
  "HLT_HIL2Mu3_NHitQ_v1",
  "HLT_HIL2Mu3_v1",
  "HLT_HIL2Mu7_v1",
  "HLT_HIL3DoubleMuOpen_Mgt2_OS_NoCowboy_v1",
  "HLT_HIL3DoubleMuOpen_Mgt2_OS_v1",
  "HLT_HIL3DoubleMuOpen_Mgt2_SS_v1",
  "HLT_HIL3DoubleMuOpen_Mgt2_v1",
  "HLT_HIL3DoubleMuOpen_v1",
  "HLT_HIL3Mu3_v1",
  "HLT_HIDiJet55_v1",
  "HLT_HIDoublePhoton10_v1",
  "HLT_HIDoublePhoton15_v1",
  "HLT_HIDoublePhoton20_v1",
  "HLT_HIFullTrack12_L1Central_v1",
  "HLT_HIFullTrack12_L1Peripheral_v1",
  "HLT_HIFullTrack14_L1Central_v1",
  "HLT_HIFullTrack14_L1Peripheral_v1",
  "HLT_HIFullTrack20_L1Central_v1",
  "HLT_HIFullTrack20_L1Peripheral_v1",
  "HLT_HIFullTrack25_L1Central_v1",
  "HLT_HIFullTrack25_L1Peripheral_v1",
  "HLT_HIJet55_v1",
  "HLT_HIJet65_Jet55_v1",
  "HLT_HIJet65_v1",
  "HLT_HIJet80_v1",
  "HLT_HIJet95_v1",
  "HLT_HIJetE30_NoBPTX_v1",
  "HLT_HIJetE50_NoBPTX3BX_NoHalo_v1",
  "HLT_HIMET120_v1",
  "HLT_HIMET200_v1",
  "HLT_HIMET220_v1",
  "HLT_HIPhoton10_Photon15_v1",
  "HLT_HIPhoton15_Photon20_v1",
  "HLT_HISinglePhoton15_v1",
  "HLT_HISinglePhoton20_v1",
  "HLT_HISinglePhoton30_v1",
  "HLT_HISinglePhoton40_v1",
  "HLT_HIBptxXOR_v1",
  "HLT_HICentral10_v1",
  "HLT_HICentralityVeto_v1",
  "HLT_HIL1Algo_BptxXOR_BSC_OR_v1",
  "HLT_HIMinBiasBSC_OR_v1",
  "HLT_HIMinBiasBSC_v1",
  "HLT_HIMinBiasHF_v1",
  "HLT_HIMinBiasHfOrBSC_v1",
  "HLT_HIMinBiasHf_OR_v1",
  "HLT_HIMinBiasPixel_SingleTrack_v1",
  "HLT_HIMinBiasZDCPixel_SingleTrack_v1",
  "HLT_HIMinBiasZDC_Calo_PlusOrMinus_v1",
  "HLT_HIMinBiasZDC_Calo_v1",
  "HLT_HIMinBiasZDC_PlusOrMinusPixel_SingleTrack_v1",
  "HLT_HIPhysics_v1",
  "HLT_HIRandom_v1",
  "HLT_HIUCC010_v1",
  "HLT_HIUCC015_v1",
  "HLT_HIUPCNeuEG2Pixel_SingleTrack_v1",
  "HLT_HIUPCNeuEG5Pixel_SingleTrack_v1",
  "HLT_HIUPCNeuHcalHfEG2Pixel_SingleTrack_v1",
  "HLT_HIUPCNeuHcalHfEG5Pixel_SingleTrack_v1",
  "HLT_HIUPCNeuHcalHfMuPixel_SingleTrack_v1",
  "HLT_HIUPCNeuMuPixel_SingleTrack_v1",
  "HLT_HIZeroBiasPixel_SingleTrack_v1",
  "HLT_HIZeroBiasXOR_v1",
  "HLT_HIZeroBias_v1",
  ] )
process.hltanalysis.dummyBranches.extend( [
  "HLT_HIL1DoubleMu0_HighQ_v2",
  "HLT_HIL1DoubleMuOpen_v2",
  "HLT_HIL2DoubleMu0_L1HighQL2NHitQ_v2",
  "HLT_HIL2DoubleMu0_NHitQ_v2",
  "HLT_HIL2DoubleMu0_v2",
  "HLT_HIL2DoubleMu3_v2",
  "HLT_HIL2Mu15_v2",
  "HLT_HIL2Mu3_NHitQ_v2",
  "HLT_HIL2Mu3_v2",
  "HLT_HIL2Mu7_v2",
  "HLT_HIL3DoubleMuOpen_Mgt2_OS_NoCowboy_v2",
  "HLT_HIL3DoubleMuOpen_Mgt2_OS_v2",
  "HLT_HIL3DoubleMuOpen_Mgt2_SS_v2",
  "HLT_HIL3DoubleMuOpen_Mgt2_v2",
  "HLT_HIL3DoubleMuOpen_v2",
  "HLT_HIL3Mu3_v2",
  "HLT_HIDiJet55_v2",
  "HLT_HIDoublePhoton10_v2",
  "HLT_HIDoublePhoton15_v2",
  "HLT_HIDoublePhoton20_v2",
  "HLT_HIFullTrack12_L1Central_v2",
  "HLT_HIFullTrack12_L1Peripheral_v2",
  "HLT_HIFullTrack14_L1Central_v2",
  "HLT_HIFullTrack14_L1Peripheral_v2",
  "HLT_HIFullTrack20_L1Central_v2",
  "HLT_HIFullTrack20_L1Peripheral_v2",
  "HLT_HIFullTrack25_L1Central_v2",
  "HLT_HIFullTrack25_L1Peripheral_v2",
  "HLT_HIJet55_v2",
  "HLT_HIJet65_Jet55_v2",
  "HLT_HIJet65_v2",
  "HLT_HIJet80_v2",
  "HLT_HIJet95_v2",
  "HLT_HIJetE30_NoBPTX_v2",
  "HLT_HIJetE50_NoBPTX3BX_NoHalo_v2",
  "HLT_HIMET120_v2",
  "HLT_HIMET200_v2",
  "HLT_HIMET220_v2",
  "HLT_HIPhoton10_Photon15_v2",
  "HLT_HIPhoton15_Photon20_v2",
  "HLT_HISinglePhoton15_v2",
  "HLT_HISinglePhoton20_v2",
  "HLT_HISinglePhoton30_v2",
  "HLT_HISinglePhoton40_v2",
  "HLT_HIBptxXOR_v2",
  "HLT_HICentral10_v2",
  "HLT_HICentralityVeto_v2",
  "HLT_HIL1Algo_BptxXOR_BSC_OR_v2",
  "HLT_HIMinBiasBSC_OR_v2",
  "HLT_HIMinBiasBSC_v2",
  "HLT_HIMinBiasHF_v2",
  "HLT_HIMinBiasHfOrBSC_v2",
  "HLT_HIMinBiasHf_OR_v2",
  "HLT_HIMinBiasPixel_SingleTrack_v2",
  "HLT_HIMinBiasZDCPixel_SingleTrack_v2",
  "HLT_HIMinBiasZDC_Calo_PlusOrMinus_v2",
  "HLT_HIMinBiasZDC_Calo_v2",
  "HLT_HIMinBiasZDC_PlusOrMinusPixel_SingleTrack_v2",
  "HLT_HIPhysics_v2",
  "HLT_HIRandom_v2",
  "HLT_HIUCC010_v2",
  "HLT_HIUCC015_v2",
  "HLT_HIUPCNeuEG2Pixel_SingleTrack_v2",
  "HLT_HIUPCNeuEG5Pixel_SingleTrack_v2",
  "HLT_HIUPCNeuHcalHfEG2Pixel_SingleTrack_v2",
  "HLT_HIUPCNeuHcalHfEG5Pixel_SingleTrack_v2",
  "HLT_HIUPCNeuHcalHfMuPixel_SingleTrack_v2",
  "HLT_HIUPCNeuMuPixel_SingleTrack_v2",
  "HLT_HIZeroBiasPixel_SingleTrack_v2",
  "HLT_HIZeroBiasXOR_v2",
  "HLT_HIZeroBias_v2",
  ] )
process.hltanalysis.dummyBranches.extend( [
  "HLT_HIL1DoubleMu0_HighQ_v3",
  "HLT_HIL1DoubleMuOpen_v3",
  "HLT_HIL2DoubleMu0_L1HighQL2NHitQ_v3",
  "HLT_HIL2DoubleMu0_NHitQ_v3",
  "HLT_HIL2DoubleMu0_v3",
  "HLT_HIL2DoubleMu3_v3",
  "HLT_HIL2Mu15_v3",
  "HLT_HIL2Mu3_NHitQ_v3",
  "HLT_HIL2Mu3_v3",
  "HLT_HIL2Mu7_v3",
  "HLT_HIL3DoubleMuOpen_Mgt2_OS_NoCowboy_v3",
  "HLT_HIL3DoubleMuOpen_Mgt2_OS_v3",
  "HLT_HIL3DoubleMuOpen_Mgt2_SS_v3",
  "HLT_HIL3DoubleMuOpen_Mgt2_v3",
  "HLT_HIL3DoubleMuOpen_v3",
  "HLT_HIL3Mu3_v3",
  "HLT_HIDiJet55_v3",
  "HLT_HIDoublePhoton10_v3",
  "HLT_HIDoublePhoton15_v3",
  "HLT_HIDoublePhoton20_v3",
  "HLT_HIFullTrack12_L1Central_v3",
  "HLT_HIFullTrack12_L1Peripheral_v3",
  "HLT_HIFullTrack14_L1Central_v3",
  "HLT_HIFullTrack14_L1Peripheral_v3",
  "HLT_HIFullTrack20_L1Central_v3",
  "HLT_HIFullTrack20_L1Peripheral_v3",
  "HLT_HIFullTrack25_L1Central_v3",
  "HLT_HIFullTrack25_L1Peripheral_v3",
  "HLT_HIJet55_v3",
  "HLT_HIJet65_Jet55_v3",
  "HLT_HIJet65_v3",
  "HLT_HIJet80_v3",
  "HLT_HIJet95_v3",
  "HLT_HIJetE30_NoBPTX_v3",
  "HLT_HIJetE50_NoBPTX3BX_NoHalo_v3",
  "HLT_HIMET120_v3",
  "HLT_HIMET200_v3",
  "HLT_HIMET220_v3",
  "HLT_HIPhoton10_Photon15_v3",
  "HLT_HIPhoton15_Photon20_v3",
  "HLT_HISinglePhoton15_v3",
  "HLT_HISinglePhoton20_v3",
  "HLT_HISinglePhoton30_v3",
  "HLT_HISinglePhoton40_v3",
  "HLT_HIBptxXOR_v3",
  "HLT_HICentral10_v3",
  "HLT_HICentralityVeto_v3",
  "HLT_HIL1Algo_BptxXOR_BSC_OR_v3",
  "HLT_HIMinBiasBSC_OR_v3",
  "HLT_HIMinBiasBSC_v3",
  "HLT_HIMinBiasHF_v3",
  "HLT_HIMinBiasHfOrBSC_v3",
  "HLT_HIMinBiasHf_OR_v3",
  "HLT_HIMinBiasPixel_SingleTrack_v3",
  "HLT_HIMinBiasZDCPixel_SingleTrack_v3",
  "HLT_HIMinBiasZDC_Calo_PlusOrMinus_v3",
  "HLT_HIMinBiasZDC_Calo_v3",
  "HLT_HIMinBiasZDC_PlusOrMinusPixel_SingleTrack_v3",
  "HLT_HIPhysics_v3",
  "HLT_HIRandom_v3",
  "HLT_HIUCC010_v3",
  "HLT_HIUCC015_v3",
  "HLT_HIUPCNeuEG2Pixel_SingleTrack_v3",
  "HLT_HIUPCNeuEG5Pixel_SingleTrack_v3",
  "HLT_HIUPCNeuHcalHfEG2Pixel_SingleTrack_v3",
  "HLT_HIUPCNeuHcalHfEG5Pixel_SingleTrack_v3",
  "HLT_HIUPCNeuHcalHfMuPixel_SingleTrack_v3",
  "HLT_HIUPCNeuMuPixel_SingleTrack_v3",
  "HLT_HIZeroBiasPixel_SingleTrack_v3",
  "HLT_HIZeroBiasXOR_v3",
  "HLT_HIZeroBias_v3",
  ] )
process.hltanalysis.dummyBranches.extend( [
  "HLT_HIL1DoubleMu0_HighQ_v4",
  "HLT_HIL1DoubleMuOpen_v4",
  "HLT_HIL2DoubleMu0_L1HighQL2NHitQ_v4",
  "HLT_HIL2DoubleMu0_NHitQ_v4",
  "HLT_HIL2DoubleMu0_v4",
  "HLT_HIL2DoubleMu3_v4",
  "HLT_HIL2Mu15_v4",
  "HLT_HIL2Mu3_NHitQ_v4",
  "HLT_HIL2Mu3_v4",
  "HLT_HIL2Mu7_v4",
  "HLT_HIL3DoubleMuOpen_Mgt2_OS_NoCowboy_v4",
  "HLT_HIL3DoubleMuOpen_Mgt2_OS_v4",
  "HLT_HIL3DoubleMuOpen_Mgt2_SS_v4",
  "HLT_HIL3DoubleMuOpen_Mgt2_v4",
  "HLT_HIL3DoubleMuOpen_v4",
  "HLT_HIL3Mu3_v4",
  "HLT_HIDiJet55_v4",
  "HLT_HIDoublePhoton10_v4",
  "HLT_HIDoublePhoton15_v4",
  "HLT_HIDoublePhoton20_v4",
  "HLT_HIFullTrack12_L1Central_v4",
  "HLT_HIFullTrack12_L1Peripheral_v4",
  "HLT_HIFullTrack14_L1Central_v4",
  "HLT_HIFullTrack14_L1Peripheral_v4",
  "HLT_HIFullTrack20_L1Central_v4",
  "HLT_HIFullTrack20_L1Peripheral_v4",
  "HLT_HIFullTrack25_L1Central_v4",
  "HLT_HIFullTrack25_L1Peripheral_v4",
  "HLT_HIJet55_v4",
  "HLT_HIJet65_Jet55_v4",
  "HLT_HIJet65_v4",
  "HLT_HIJet80_v4",
  "HLT_HIJet95_v4",
  "HLT_HIJetE30_NoBPTX_v4",
  "HLT_HIJetE50_NoBPTX3BX_NoHalo_v4",
  "HLT_HIMET120_v4",
  "HLT_HIMET200_v4",
  "HLT_HIMET220_v4",
  "HLT_HIPhoton10_Photon15_v4",
  "HLT_HIPhoton15_Photon20_v4",
  "HLT_HISinglePhoton15_v4",
  "HLT_HISinglePhoton20_v4",
  "HLT_HISinglePhoton30_v4",
  "HLT_HISinglePhoton40_v4",
  "HLT_HIBptxXOR_v4",
  "HLT_HICentral10_v4",
  "HLT_HICentralityVeto_v4",
  "HLT_HIL1Algo_BptxXOR_BSC_OR_v4",
  "HLT_HIMinBiasBSC_OR_v4",
  "HLT_HIMinBiasBSC_v4",
  "HLT_HIMinBiasHF_v4",
  "HLT_HIMinBiasHfOrBSC_v4",
  "HLT_HIMinBiasHf_OR_v4",
  "HLT_HIMinBiasPixel_SingleTrack_v4",
  "HLT_HIMinBiasZDCPixel_SingleTrack_v4",
  "HLT_HIMinBiasZDC_Calo_PlusOrMinus_v4",
  "HLT_HIMinBiasZDC_Calo_v4",
  "HLT_HIMinBiasZDC_PlusOrMinusPixel_SingleTrack_v4",
  "HLT_HIPhysics_v4",
  "HLT_HIRandom_v4",
  "HLT_HIUCC010_v4",
  "HLT_HIUCC015_v4",
  "HLT_HIUPCNeuEG2Pixel_SingleTrack_v4",
  "HLT_HIUPCNeuEG5Pixel_SingleTrack_v4",
  "HLT_HIUPCNeuHcalHfEG2Pixel_SingleTrack_v4",
  "HLT_HIUPCNeuHcalHfEG5Pixel_SingleTrack_v4",
  "HLT_HIUPCNeuHcalHfMuPixel_SingleTrack_v4",
  "HLT_HIUPCNeuMuPixel_SingleTrack_v4",
  "HLT_HIZeroBiasPixel_SingleTrack_v4",
  "HLT_HIZeroBiasXOR_v4",
  "HLT_HIZeroBias_v4",
  ] )

#process.hltanalysis.hltresults = cms.InputTag("TriggerResults","","RECO")
process.skimanalysis = cms.EDAnalyzer("FilterAnalyzer",
                                     hltresults = cms.InputTag("TriggerResults","","hiForestAna2011")
                                     )
process.hltAna = cms.Path(process.hltanalysis)
process.pAna = cms.EndPath(process.skimanalysis)



process.load('CmsHi.JetAnalysis.rechitanalyzer_cfi')
  
process.rechitanalyzer.HBHETreePtMin = cms.untracked.double(0.5)
process.rechitanalyzer.HFTreePtMin = cms.untracked.double(0.5)
process.rechitanalyzer.EBTreePtMin = cms.untracked.double(0.5)
process.rechitanalyzer.EETreePtMin = cms.untracked.double(0.5)
process.rechitanalyzer.TowerTreePtMin = cms.untracked.double(0.5)
process.rechitanalyzer.doHF = cms.untracked.bool(True)
process.rechitAna = cms.Path(process.rechitanalyzer)

########### random number seed
process.RandomNumberGeneratorService.akPu3PFConesAna = process.RandomNumberGeneratorService.generator.clone()
process.RandomNumberGeneratorService.icPu5CaloConesAna = process.RandomNumberGeneratorService.generator.clone()
process.RandomNumberGeneratorService.akPu5PFConesAna = process.RandomNumberGeneratorService.generator.clone()
process.RandomNumberGeneratorService.akPu3CaloConesAna = process.RandomNumberGeneratorService.generator.clone()
process.RandomNumberGeneratorService.akPu5CaloConesAna = process.RandomNumberGeneratorService.generator.clone()
process.RandomNumberGeneratorService.multiPhotonAnalyzer = process.RandomNumberGeneratorService.generator.clone()

#####################################################################################
# Edm Output
#####################################################################################

#process.out = cms.OutputModule("PoolOutputModule",
#                               fileName = cms.untracked.string("output.root")
#                               )
#process.save = cms.EndPath(process.out)


process.skimanalysis.superFilters = cms.vstring("superFilterPath")
for path in process.paths:
       getattr(process,path)._seq = process.superFilterSequence*getattr(process,path)._seq
       
       
       
       
