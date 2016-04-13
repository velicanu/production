#!/usr/bin/env python2
# Run the foresting configuration on PbPb in CMSSW_5_3_X, using the new HF/Voronoi jets
# Author: Alex Barbieri
# Date: 2013-10-15

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

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100000)
)

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                            fileNames = readFiles, secondaryFileNames = secFiles)

readFiles.extend( [
       '/store/data/Run2011A/MinimumBias2/AOD/12Oct2013-v1/00000/FA9971F6-0348-E311-B44C-003048CFB590.root' ] );


# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1))


#####################################################################################
# Load Global Tag, Geometry, etc.
#####################################################################################

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
#process.load('RecoHI.HiCentralityAlgos.CentralityBin_cfi')

process.load('RecoParticleFlow.PFClusterProducer.particleFlowCluster_cff')
process.load('RecoParticleFlow.Configuration.RecoParticleFlow_cff')

process.load('FWCore.MessageService.MessageLogger_cfi')

# PbPb 53X MC
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'START53_LV6::All', '')

from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import *
#overrideCentrality(process)
overrideGT_pp2760(process)
overrideJEC_pp2760(process)

#process.HeavyIonGlobalParameters = cms.PSet(
#    centralityVariable = cms.string("HFtowersTrunc"),
#    nonDefaultGlauberModel = cms.string(""),
#    centralitySrc = cms.InputTag("pACentrality")
#    )

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string('FA9971F6-0348-E311-B44C-003048CFB590.root'))

#####################################################################################
# Additional Reconstruction and Analysis: Main Body
#####################################################################################

#process.load('Configuration.StandardSequences.Generator_cff')
#process.load('RecoJets.Configuration.GenJetParticles_cff')
#process.load('RecoHI.HiJetAlgos.HiGenJets_cff')
#process.load('RecoHI.HiJetAlgos.HiRecoJets_cff')
#process.load('RecoHI.HiJetAlgos.HiRecoPFJets_cff')

#process.hiGenParticles.srcVector = cms.vstring('generator')

#process.hiCentrality.producePixelhits = False
#process.hiCentrality.producePixelTracks = False
#process.hiCentrality.srcTracks = cms.InputTag("generalTracks")
#process.hiCentrality.srcVertex = cms.InputTag("offlinePrimaryVerticesWithBS")
#process.hiEvtPlane.vtxCollection_ = cms.InputTag("offlinePrimaryVerticesWithBS")
#process.hiEvtPlane.trackCollection_ = cms.InputTag("generalTracks")

process.load('HeavyIonsAnalysis.JetAnalysis.jets.HiGenJetsCleaned_JEC_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu1CaloJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs1CaloJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs1PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu1PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak1PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak1CaloJetSequence_pp_data_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu2CaloJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs2CaloJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs2PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu2PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak2PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak2CaloJetSequence_pp_data_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu3CaloJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs3CaloJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs3PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak3PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak3CaloJetSequence_pp_data_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs4CaloJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs4PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak4PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak4CaloJetSequence_pp_data_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu5CaloJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs5CaloJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs5PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu5PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak5PFJetSequence_pp_data_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak5CaloJetSequence_pp_data_cff')


process.load('HeavyIonsAnalysis.JetAnalysis.jets.HiReRecoJets_pp_cff')

pfTag = 'particleFlow'
trackTag = 'generalTracks'
vertexTag = 'offlinePrimaryVerticesWithBS'

process.voronoiBackgroundPF.src = cms.InputTag(pfTag)
process.PFTowers.src = cms.InputTag(pfTag)

process.ak1PFJets.src = pfTag
process.ak2PFJets.src = pfTag
process.ak3PFJets.src = pfTag
process.ak4PFJets.src = pfTag
process.ak5PFJets.src = pfTag
process.ak6PFJets.src = pfTag
process.ak7PFJets.src = pfTag

#process.akPu1PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
#process.akPu2PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
#process.akPu3PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
#process.akPu4PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
#process.akPu5PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)

#process.akVs1PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
#process.akVs2PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
#process.akVs3PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
#process.akVs4PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
#process.akVs5PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)

process.ak1PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ak2PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ak3PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ak4PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ak5PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)

process.ak1PFJetAnalyzer.trackTag = cms.InputTag(trackTag)
process.ak2PFJetAnalyzer.trackTag = cms.InputTag(trackTag)
process.ak3PFJetAnalyzer.trackTag = cms.InputTag(trackTag)
process.ak4PFJetAnalyzer.trackTag = cms.InputTag(trackTag)
process.ak5PFJetAnalyzer.trackTag = cms.InputTag(trackTag)

#process.akPu1CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
#process.akPu2CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
#process.akPu3CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
#process.akPu4CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
#process.akPu5CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)

#process.akVs1CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
#process.akVs2CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
#process.akVs3CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
#process.akVs4CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
#process.akVs5CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)

process.ak1CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ak2CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ak3CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ak4CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ak5CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)

process.ak1CaloJetAnalyzer.trackTag = cms.InputTag(trackTag)
process.ak2CaloJetAnalyzer.trackTag = cms.InputTag(trackTag)
process.ak3CaloJetAnalyzer.trackTag = cms.InputTag(trackTag)
process.ak4CaloJetAnalyzer.trackTag = cms.InputTag(trackTag)
process.ak5CaloJetAnalyzer.trackTag = cms.InputTag(trackTag)


process.jetSequences = cms.Sequence(#process.voronoiBackgroundCalo +
                                    #process.voronoiBackgroundPF +
                                    #process.PFTowers +
                                    process.hiReRecoCaloJets +
                                    process.hiReRecoPFJets +

                                    #process.akPu2CaloJetSequence +
                                    #process.akVs2CaloJetSequence +
                                    #process.akVs2PFJetSequence +
                                    #process.akPu2PFJetSequence +
                                    process.ak2PFJetSequence +
                                    process.ak2CaloJetSequence +

                                    #process.akPu3CaloJetSequence +
                                    #process.akVs3CaloJetSequence +
                                    #process.akVs3PFJetSequence +
                                    #process.akPu3PFJetSequence +
                                    process.ak3PFJetSequence +
                                    process.ak3CaloJetSequence +

                                    #process.akPu4CaloJetSequence +
                                    #process.akVs4CaloJetSequence +
                                    #process.akVs4PFJetSequence +
                                    #process.akPu4PFJetSequence +
                                    process.ak4PFJetSequence +
                                    process.ak4CaloJetSequence +

                                    #process.akPu5CaloJetSequence +
                                    #process.akVs5CaloJetSequence +
                                    #process.akVs5PFJetSequence +
                                    #process.akPu5PFJetSequence +
                                    process.ak5PFJetSequence +
                                    process.ak5CaloJetSequence

                                    )

process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi')
#process.load('HeavyIonsAnalysis.JetAnalysis.HiGenAnalyzer_cfi')
#process.hiEvtAnalyzer.Vertex = cms.InputTag("offlinePrimaryVerticesWithBS")
#process.hiEvtAnalyzer.Centrality = cms.InputTag("pACentrality")

#####################################################################################
# To be cleaned

process.load('HeavyIonsAnalysis.JetAnalysis.ExtraTrackReco_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_cff')
process.load("HeavyIonsAnalysis.TrackAnalysis.METAnalyzer_cff")
process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzer_pp_cfi")
process.load('HeavyIonsAnalysis.JetAnalysis.rechitanalyzer_pp_cfi')
process.rechitanalyzer.vtxSrc = cms.untracked.InputTag(vertexTag)
process.pfTowers.vtxSrc = cms.untracked.InputTag(vertexTag)

process.rechitAna = cms.Sequence(process.rechitanalyzer+process.pfTowers)

process.pfcandAnalyzer.skipCharged = False
process.pfcandAnalyzer.pfPtMin = 0
process.pfcandAnalyzer.pfCandidateLabel = cms.InputTag(pfTag)

#####################################################################################

#########################
# Track Analyzer
#########################
process.hiTracks.cut = cms.string('quality("highPurity")')

# clusters missing in recodebug - to be resolved
process.anaTrack.doPFMatching = False

process.anaTrack.vertexSrc = [vertexTag]
process.ppTrack.doPFMatching = False
process.ppTrack.doSimTrack = False
process.ppTrack.trackSrc = cms.InputTag(trackTag)
process.ppTrack.vertexSrc = [vertexTag]

#####################
# photons
process.load('HeavyIonsAnalysis.JetAnalysis.EGammaAnalyzers_cff')
process.photonStep.remove(process.photonMatch)
process.hiGoodTracks.src = cms.InputTag(trackTag)
process.hiGoodTracks.vertices = cms.InputTag(vertexTag)
process.RandomNumberGeneratorService.multiPhotonAnalyzer = process.RandomNumberGeneratorService.generator.clone()

#####################
# muons
######################
process.load("HeavyIonsAnalysis.MuonAnalysis.hltMuTree_cfi")
process.hltMuTree.doGen = cms.untracked.bool(True)
process.load("RecoHI.HiMuonAlgos.HiRecoMuon_cff")
process.muons.JetExtractorPSet.JetCollectionLabel = cms.InputTag("akVs3PFJets")
process.globalMuons.TrackerCollectionLabel = trackTag
process.muons.TrackExtractorPSet.inputTrackCollection = trackTag
process.muons.inputCollectionLabels = [trackTag, "globalMuons", "standAloneMuons:UpdatedAtVtx", "tevMuons:firstHit", "tevMuons:picky", "tevMuons:dyt"]

#Filtering
#############################################################
# To filter on an HLT trigger path, uncomment the lines below, add the
# HLT path you would like to filter on to 'HLTPaths' and also
# uncomment the snippet at the end of the configuration.
#############################################################
# Minimum bias trigger selection (later runs)
#process.load("HLTrigger.HLTfilters.hltHighLevel_cfi")
#process.skimFilter = process.hltHighLevel.clone()
#process.skimFilter.HLTPaths = ["HLT_HIMinBiasHfOrBSC_v1"]

#process.superFilterSequence = cms.Sequence(process.skimFilter)
#process.superFilterPath = cms.Path(process.superFilterSequence)
#process.skimanalysis.superFilters = cms.vstring("superFilterPath")
################################################################

process.ana_step = cms.Path(#process.hiCentrality +
                            #process.centralityBin +
                            #process.hiEvtPlane +
                            #process.hiEvtAnalyzer*
                            process.jetSequences +
                            #process.photonStep +
                            process.pfcandAnalyzer +
                            #process.rechitAna +
#temp                            process.hltMuTree +
                            process.HiForest +
                            process.ppTrack)


process.load('HeavyIonsAnalysis.JetAnalysis.EventSelection_cff')
process.primaryVertexFilter.src = cms.InputTag("offlinePrimaryVerticesWithBS")
process.PAprimaryVertexFilter.src = cms.InputTag("offlinePrimaryVerticesWithBS")

process.phltJetHI = cms.Path( process.hltJetHI )
#process.pcollisionEventSelection = cms.Path(process.collisionEventSelection)
process.pPAcollisionEventSelectionPA = cms.Path(process.PAcollisionEventSelection)
process.pHBHENoiseFilter = cms.Path( process.HBHENoiseFilter )
process.phfCoincFilter = cms.Path(process.hfCoincFilter )
process.phfCoincFilter3 = cms.Path(process.hfCoincFilter3 )
#process.pprimaryVertexFilter = cms.Path(process.primaryVertexFilter )
process.pPAprimaryVertexFilter = cms.Path(process.PAprimaryVertexFilter)
#process.phltPixelClusterShapeFilter = cms.Path(process.siPixelRecHits*process.hltPixelClusterShapeFilter )
#process.phiEcalRecHitSpikeFilter = cms.Path(process.hiEcalRecHitSpikeFilter )
process.phfPosFilter3 = cms.Path(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter3)
process.phfNegFilter3 = cms.Path(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfNegFilter3)
#process.phfPosFilter2 = cms.Path(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter2)
#process.phfNegFilter2 = cms.Path(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfNegFilter2)
#process.phfPosFilter1 = cms.Path(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter)
#process.phfNegFilter1 = cms.Path(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfNegFilter)
process.pBeamScrapingFilter=cms.Path(process.NoScraping)

process.load("HeavyIonsAnalysis.VertexAnalysis.PAPileUpVertexFilter_cff")

process.pVertexFilterCutG = cms.Path(process.pileupVertexFilterCutG)
process.pVertexFilterCutGloose = cms.Path(process.pileupVertexFilterCutGloose)
process.pVertexFilterCutGtight = cms.Path(process.pileupVertexFilterCutGtight)
process.pVertexFilterCutGplus = cms.Path(process.pileupVertexFilterCutGplus)
process.pVertexFilterCutE = cms.Path(process.pileupVertexFilterCutE)
process.pVertexFilterCutEandG = cms.Path(process.pileupVertexFilterCutEandG)

#process.load('HeavyIonsAnalysis.JetAnalysis.EventSelection_cff')
#process.phltJetHI = cms.Path( process.hltJetHI )
#process.pcollisionEventSelection = cms.Path(process.collisionEventSelection)
#process.pHBHENoiseFilter = cms.Path( process.HBHENoiseFilter )
#process.phfCoincFilter = cms.Path(process.hfCoincFilter )
#process.phfCoincFilter3 = cms.Path(process.hfCoincFilter3 )
#process.pprimaryVertexFilter = cms.Path(process.PAprimaryVertexFilter )
##process.phltPixelClusterShapeFilter = cms.Path(process.siPixelRecHits*process.hltPixelClusterShapeFilter )
##process.phiEcalRecHitSpikeFilter = cms.Path(process.hiEcalRecHitSpikeFilter )

# Customization
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')

process.hltAna = cms.Path(process.hltanalysis)
process.pAna = cms.EndPath(process.skimanalysis)

#Filtering
#for path in process.paths:
#    getattr(process,path)._seq = process.superFilterSequence*getattr(process,path)._seq
