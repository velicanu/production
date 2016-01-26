### HiForest Configuration
# Collisions: pp
# Type: Data
# Input: AOD

import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')
process.options = cms.untracked.PSet()

#####################################################################################
# HiForest labelling info
#####################################################################################

process.load("HeavyIonsAnalysis.JetAnalysis.HiForest_cff")
process.HiForest.inputLines = cms.vstring("HiForest V3",)
import subprocess
version = subprocess.Popen(["(cd $CMSSW_BASE/src && git describe --tags)"], stdout=subprocess.PIPE, shell=True).stdout.read()
if version == '':
    version = 'no git info'
process.HiForest.HiForestVersion = cms.string(version)

#####################################################################################
# Input source
#####################################################################################

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                "/store/group/phys_heavyions/velicanu/reco/HIPhysicsMinBiasUPC/v0/000/262/548/recoExpress_84.root"
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
process.load('FWCore.MessageService.MessageLogger_cfi')

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_dataRun2_v12', '')  #for now track GT manually, since centrality tables updated ex post facto
process.HiForest.GlobalTagLabel = process.GlobalTag.globaltag

from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import overrideJEC_PbPb5020
process = overrideJEC_PbPb5020(process)

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("HiForestAOD.root"))

#####################################################################################
# Additional Reconstruction and Analysis: Main Body
#####################################################################################

####################################################################################

#############################
# Jets
#############################
from Configuration.StandardSequences.ReconstructionHeavyIons_cff import voronoiBackgroundPF, voronoiBackgroundCalo

process.voronoiBackgroundPF = voronoiBackgroundPF
process.voronoiBackgroundCalo = voronoiBackgroundCalo
process.load('HeavyIonsAnalysis.JetAnalysis.jets.HiReRecoJets_HI_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu2CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs2CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs2PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu2PFJetSequence_PbPb_data_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu3CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs3CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs3PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_PbPb_data_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs4CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs4PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_PbPb_data_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu5CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs5CaloJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs5PFJetSequence_PbPb_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu5PFJetSequence_PbPb_data_cff')


process.highPurityTracks = cms.EDFilter("TrackSelector",
                                        src = cms.InputTag("hiGeneralTracks"),
                                        cut = cms.string('quality("highPurity")'))

process.load("RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi")
process.offlinePrimaryVertices.TrackLabel = 'highPurityTracks'

process.jetSequences = cms.Sequence(
    voronoiBackgroundPF+
    voronoiBackgroundCalo+

    process.akPu2CaloJets +
    process.akPu2PFJets +
    process.akVs2CaloJets +
    process.akVs2PFJets +

    #process.akPu3CaloJets +
    #process.akPu3PFJets +
    process.akVs3CaloJets +
    process.akVs3PFJets +

    #process.akPu4CaloJets +
    #process.akPu4PFJets +
    process.akVs4CaloJets +
    process.akVs4PFJets +

    process.akPu5CaloJets +
    process.akPu5PFJets +
    process.akVs5CaloJets +
    process.akVs5PFJets +

    process.highPurityTracks +
    process.offlinePrimaryVertices +

    process.akPu2CaloJetSequence +
    process.akVs2CaloJetSequence +
    process.akVs2PFJetSequence +
    process.akPu2PFJetSequence +

    process.akPu3CaloJetSequence +
    process.akVs3CaloJetSequence +
    process.akVs3PFJetSequence +
    process.akPu3PFJetSequence +

    process.akPu4CaloJetSequence +
    process.akVs4CaloJetSequence +
    process.akVs4PFJetSequence +
    process.akPu4PFJetSequence +

    process.akPu5CaloJetSequence +
    process.akVs5CaloJetSequence +
    process.akVs5PFJetSequence +
    process.akPu5PFJetSequence
    )

#####################################################################################

############################
# Event Analysis
############################
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hltobject_PbPb_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')
from HeavyIonsAnalysis.EventAnalysis.dummybranches_cff import addHLTdummybranches
addHLTdummybranches(process)

process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzer_cfi")
process.pfcandAnalyzer.skipCharged = False
process.pfcandAnalyzer.pfPtMin = 0
process.load("HeavyIonsAnalysis.JetAnalysis.hcalNoise_cff")

#####################################################################################

#########################
# Track Analyzer
#########################
process.load('HeavyIonsAnalysis.JetAnalysis.ExtraTrackReco_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_cff')
# process.load("HeavyIonsAnalysis.TrackAnalysis.METAnalyzer_cff")


####################################################################################
#####################################################################################
######################### D finder ##################################################
#####################################################################################
runOnMC = False
RunOnAOD = True
AddCaloMuon = False
HIFormat = False
UseGenPlusSim = False
VtxLabel = "hiSelectedVertex"
from Bfinder.finderMaker.finderMaker_75X_cff import finderMaker_75X
finderMaker_75X(process, AddCaloMuon, runOnMC, HIFormat, UseGenPlusSim)

#default for D0 and Jet triggers, tk pt cut 8.0 GeV
process.Dfinder = cms.EDAnalyzer("Dfinder",
    BSLabel = cms.InputTag("offlineBeamSpot"),
    Dchannel = cms.vint32(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    GenLabel = cms.InputTag("genParticles"),
    HLTLabel = cms.InputTag("TriggerResults","","HLT"),
    MVAMapLabel = cms.string('hiGeneralTracks'),
    MaxDocaCut = cms.vdouble(999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0),
    PUInfoLabel = cms.InputTag("addPileupInfo"),
    PVLabel = cms.InputTag("hiSelectedVertex"),
    RunOnMC = cms.bool(False),
    TrackLabel = cms.InputTag("patTrackCands"),
    dCutSeparating_PtVal = cms.vdouble(5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0),
    dEtaCut = cms.vdouble(1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5),
    dPtCut = cms.vdouble(0.5, 0.5, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 9.0, 9.0),
    detailMode = cms.bool(False),
    doDntupleSkim = cms.bool(False),
    doTkPreCut = cms.bool(True),
    dropUnusedTracks = cms.bool(True),
    makeDntuple = cms.bool(False),
    VtxChiProbCut = cms.vdouble(0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), #this cut not good for decay with resonance now
    alphaCut = cms.vdouble(0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 999.0, 999.0, 999.0, 999.0),
    svpvDistanceCut_highptD = cms.vdouble(2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0),
    svpvDistanceCut_lowptD = cms.vdouble(4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 0.0, 0.0, 0.0, 0.0),
    tkEtaCut = cms.double(2.0),
    tkPtCut = cms.double(6.0),
    tktkRes_alphaCut = cms.vdouble(999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 999.0, 0.2, 0.2, 0.2, 0.2),
    tktkRes_svpvDistanceCut_highptD = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0, 2.0, 2.0),
    tktkRes_svpvDistanceCut_lowptD = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 4.0, 4.0, 4.0)
)
#################################################################################################

#####################
# Photons
#####################
process.load('HeavyIonsAnalysis.PhotonAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.doGenParticles = False
process.ggHiNtuplizerGED = process.ggHiNtuplizer.clone(recoPhotonSrc = cms.InputTag('gedPhotonsTmp'),
                                                       recoPhotonHiIsolationMap = cms.InputTag('photonIsolationHIProducerGED')
)

####################################################################################

#####################
# tupel and necessary PAT sequences
#####################

process.load("HeavyIonsAnalysis.VectorBosonAnalysis.tupelSequence_PbPb_cff")

#####################################################################################

#########################
# Main analysis list
#########################

process.ana_step = cms.Path(process.hltanalysis *
                            process.hltobject *
                            process.centralityBin *
                            process.hiEvtAnalyzer*
                            process.jetSequences +
                            process.ggHiNtuplizer +
                            process.ggHiNtuplizerGED +
                            process.DfinderSequence +
                            process.pfcandAnalyzer +
                            process.HiForest +
                            process.trackSequencesPbPb +
                            process.hcalNoise #+
                            #process.tupelPatSequence
                            )

#####################################################################################

#########################
# Event Selection
#########################

process.load('HeavyIonsAnalysis.JetAnalysis.EventSelection_cff')
process.pcollisionEventSelection = cms.Path(process.collisionEventSelectionAOD)
process.pHBHENoiseFilterResultProducer = cms.Path( process.HBHENoiseFilterResultProducer )
process.HBHENoiseFilterResult = cms.Path(process.fHBHENoiseFilterResult)
process.HBHENoiseFilterResultRun1 = cms.Path(process.fHBHENoiseFilterResultRun1)
process.HBHENoiseFilterResultRun2Loose = cms.Path(process.fHBHENoiseFilterResultRun2Loose)
process.HBHENoiseFilterResultRun2Tight = cms.Path(process.fHBHENoiseFilterResultRun2Tight)
process.HBHEIsoNoiseFilterResult = cms.Path(process.fHBHEIsoNoiseFilterResult)
process.pprimaryVertexFilter = cms.Path(process.primaryVertexFilter )

process.load('HeavyIonsAnalysis.Configuration.hfCoincFilter_cff')
process.phfCoincFilter1 = cms.Path(process.hfCoincFilter)
process.phfCoincFilter2 = cms.Path(process.hfCoincFilter2)
process.phfCoincFilter3 = cms.Path(process.hfCoincFilter3)
process.phfCoincFilter4 = cms.Path(process.hfCoincFilter4)
process.phfCoincFilter5 = cms.Path(process.hfCoincFilter5)

process.pclusterCompatibilityFilter = cms.Path(process.clusterCompatibilityFilter)

process.pAna = cms.EndPath(process.skimanalysis)

# Customization
##########################################UE##########################################
from CondCore.DBCommon.CondDBSetup_cfi import *
process.uetable = cms.ESSource("PoolDBESSource",
      DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0)
        ),
      timetype = cms.string('runnumber'),
      toGet = cms.VPSet(
          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("UETableCompatibilityFormat_PF_v02_offline"),
                   label = cms.untracked.string("UETable_PF")
          ),
          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("UETableCompatibilityFormat_Calo_v02_offline"),
                   label = cms.untracked.string("UETable_Calo")
          )
      ), 
      connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
)
process.es_prefer_uetable = cms.ESPrefer('PoolDBESSource','uetable')
##########################################UE##########################################





import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltfilter = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltfilter.HLTPaths = ["HLT_HIPuAK4CaloJet*_Eta5p1_Cent*100_v*","HLT_HIFullTrack*","HLT_HIDmesonHITrackingGlobal_Dpt*"]
process.superFilterPath = cms.Path(process.hltfilter)
process.skimanalysis.superFilters = cms.vstring("superFilterPath")
##filter all path with the production filter sequence
for path in process.paths:
   getattr(process,path)._seq = process.hltfilter * getattr(process,path)._seq
   
   