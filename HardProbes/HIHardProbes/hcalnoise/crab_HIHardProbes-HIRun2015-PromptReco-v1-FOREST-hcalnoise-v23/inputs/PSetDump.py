import FWCore.ParameterSet.Config as cms

process = cms.Process("HiForest")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:/afs/cern.ch/user/v/velicanu/eos/cms/tier0/store/hidata/HIRun2015/HIHardProbes/AOD/PromptReco-v1/000/263/412/00000/A4BECAFD-01AF-E511-BA3E-02163E01346F.root')
)
process.HBHENoiseFilterResultProducer = cms.EDProducer("HBHENoiseFilterResultProducer",
    IgnoreTS4TS5ifJetInLowBVRegion = cms.bool(True),
    defaultDecision = cms.string('HBHENoiseFilterResultRun1'),
    minHPDHits = cms.int32(17),
    minHPDNoOtherHits = cms.int32(10),
    minIsolatedNoiseSumE = cms.double(50.0),
    minIsolatedNoiseSumEt = cms.double(25.0),
    minNumIsolatedNoiseChannels = cms.int32(10),
    minZeros = cms.int32(9999),
    noiselabel = cms.InputTag("hcalnoise")
)


process.PFTowers = cms.EDProducer("ParticleTowerProducer",
    src = cms.InputTag("particleFlowTmp"),
    useHF = cms.bool(False)
)


process.ak1CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.1),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak1PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.1),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlowTmp"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak2CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.2),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak2PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.2),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlowTmp"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak3CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.3),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak3PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.3),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlowTmp"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlowTmp"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak5CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.5),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak5JetExtender = cms.EDProducer("JetExtender",
    coneSize = cms.double(0.5),
    jet2TracksAtCALO = cms.InputTag("ak5JetTracksAssociatorAtCaloFace"),
    jet2TracksAtVX = cms.InputTag("ak5JetTracksAssociatorAtVertex"),
    jets = cms.InputTag("ak5CaloJets")
)


process.ak5JetTracksAssociatorAtCaloFace = cms.EDProducer("JetTracksAssociatorAtCaloFace",
    coneSize = cms.double(0.5),
    extrapolations = cms.InputTag("trackExtrapolator"),
    jets = cms.InputTag("ak5CaloJets"),
    trackQuality = cms.string('goodIterative'),
    tracks = cms.InputTag("generalTracks")
)


process.ak5JetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("ak5CaloJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)


process.ak5JetTracksAssociatorAtVertexPF = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("ak5PFJetsCHS"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)


process.ak5JetTracksAssociatorExplicit = cms.EDProducer("JetTracksAssociatorExplicit",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("ak5PFJetsCHS"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)


process.ak5PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.5),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlowTmp"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak6CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.6),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak6PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.6),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlowTmp"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak7CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.7),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akPu1CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(4),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.1),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akPu1PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('BasicJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.1),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("PFTowers"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akPu2CaloCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloImpactParameterTagInfos"), cms.InputTag("akPu2CaloSecondaryVertexTagInfos"))
)


process.akPu2CaloCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloImpactParameterTagInfos"), cms.InputTag("akPu2CaloSecondaryVertexTagInfos"))
)


process.akPu2CaloImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("akPu2CaloJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.akPu2CaloJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloImpactParameterTagInfos"))
)


process.akPu2CaloJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("akPu2CaloJets"),
    useRecHits = cms.bool(True)
)


process.akPu2CaloJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloImpactParameterTagInfos"))
)


process.akPu2CaloJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("akPu2CaloJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.akPu2CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(4),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.2),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akPu2CaloNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloImpactParameterTagInfos"), cms.InputTag("akPu2CaloSecondaryVertexNegativeTagInfos"))
)


process.akPu2CaloNegativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloImpactParameterTagInfos"))
)


process.akPu2CaloNegativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloImpactParameterTagInfos"))
)


process.akPu2CaloNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloSecondaryVertexNegativeTagInfos"))
)


process.akPu2CaloNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloSecondaryVertexNegativeTagInfos"))
)


process.akPu2CaloNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloSoftPFMuonsTagInfos"))
)


process.akPu2CaloNegativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloImpactParameterTagInfos"))
)


process.akPu2CaloNegativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloImpactParameterTagInfos"))
)


process.akPu2CaloPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("akPu2CaloPatJetPartonAssociationLegacy")
)


process.akPu2CaloPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("akPu2CaloJets"),
    partons = cms.InputTag("myPartons")
)


process.akPu2CaloPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.akPu2CaloPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloImpactParameterTagInfos"), cms.InputTag("akPu2CaloSecondaryVertexTagInfos"))
)


process.akPu2CaloPositiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloImpactParameterTagInfos"))
)


process.akPu2CaloPositiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloImpactParameterTagInfos"))
)


process.akPu2CaloPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloSoftPFMuonsTagInfos"))
)


process.akPu2CaloSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akPu2CaloImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akPu2CaloSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akPu2CaloImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akPu2CaloSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloSecondaryVertexTagInfos"))
)


process.akPu2CaloSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloSecondaryVertexTagInfos"))
)


process.akPu2CaloSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloSoftPFMuonsTagInfos"))
)


process.akPu2CaloSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloSoftPFMuonsTagInfos"))
)


process.akPu2CaloSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloSoftPFMuonsTagInfos"))
)


process.akPu2CaloSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("akPu2CaloJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.akPu2CaloTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloImpactParameterTagInfos"))
)


process.akPu2CaloTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2CaloImpactParameterTagInfos"))
)


process.akPu2Calocorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute'),
    payload = cms.string('AKPu2Calo_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akPu2CaloJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akPu2Calomatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak2HiGenJets"),
    maxDeltaR = cms.double(0.2),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akPu2CaloJets")
)


process.akPu2Caloparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akPu2CaloJets")
)


process.akPu2CalopatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akPu2CaloPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akPu2CaloPatJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("akPu2CaloSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("akPu2CaloSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("akPu2CaloCombinedSecondaryVertexBJetTags"), cms.InputTag("akPu2CaloCombinedSecondaryVertexV2BJetTags"), cms.InputTag("akPu2CaloJetBProbabilityBJetTags"), 
        cms.InputTag("akPu2CaloJetProbabilityBJetTags"), cms.InputTag("akPu2CaloTrackCountingHighEffBJetTags"), cms.InputTag("akPu2CaloTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akPu2Calomatch"),
    genPartonMatch = cms.InputTag("akPu2Caloparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2Calocorr")),
    jetIDMap = cms.InputTag("akPu2CaloJetID"),
    jetSource = cms.InputTag("akPu2CaloJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("akPu2CaloJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.akPu2PFCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFImpactParameterTagInfos"), cms.InputTag("akPu2PFSecondaryVertexTagInfos"))
)


process.akPu2PFCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFImpactParameterTagInfos"), cms.InputTag("akPu2PFSecondaryVertexTagInfos"))
)


process.akPu2PFImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("akPu2PFJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.akPu2PFJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFImpactParameterTagInfos"))
)


process.akPu2PFJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("akPu2CaloJets"),
    useRecHits = cms.bool(True)
)


process.akPu2PFJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFImpactParameterTagInfos"))
)


process.akPu2PFJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("akPu2PFJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.akPu2PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('BasicJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.2),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("PFTowers"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akPu2PFNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFImpactParameterTagInfos"), cms.InputTag("akPu2PFSecondaryVertexNegativeTagInfos"))
)


process.akPu2PFNegativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFImpactParameterTagInfos"))
)


process.akPu2PFNegativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFImpactParameterTagInfos"))
)


process.akPu2PFNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFSecondaryVertexNegativeTagInfos"))
)


process.akPu2PFNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFSecondaryVertexNegativeTagInfos"))
)


process.akPu2PFNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFSoftPFMuonsTagInfos"))
)


process.akPu2PFNegativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFImpactParameterTagInfos"))
)


process.akPu2PFNegativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFImpactParameterTagInfos"))
)


process.akPu2PFPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("akPu2PFPatJetPartonAssociationLegacy")
)


process.akPu2PFPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("akPu2PFJets"),
    partons = cms.InputTag("myPartons")
)


process.akPu2PFPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.akPu2PFPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFImpactParameterTagInfos"), cms.InputTag("akPu2PFSecondaryVertexTagInfos"))
)


process.akPu2PFPositiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFImpactParameterTagInfos"))
)


process.akPu2PFPositiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFImpactParameterTagInfos"))
)


process.akPu2PFPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFSoftPFMuonsTagInfos"))
)


process.akPu2PFSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akPu2PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akPu2PFSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akPu2PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akPu2PFSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFSecondaryVertexTagInfos"))
)


process.akPu2PFSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFSecondaryVertexTagInfos"))
)


process.akPu2PFSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFSoftPFMuonsTagInfos"))
)


process.akPu2PFSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFSoftPFMuonsTagInfos"))
)


process.akPu2PFSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFSoftPFMuonsTagInfos"))
)


process.akPu2PFSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("akPu2PFJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.akPu2PFTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFImpactParameterTagInfos"))
)


process.akPu2PFTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu2PFImpactParameterTagInfos"))
)


process.akPu2PFcorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute'),
    payload = cms.string('AKPu2PF_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akPu2PFJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akPu2PFmatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak2HiGenJets"),
    maxDeltaR = cms.double(0.2),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akPu2PFJets")
)


process.akPu2PFparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akPu2PFJets")
)


process.akPu2PFpatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akPu2PFPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akPu2PFPatJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("akPu2PFSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("akPu2PFSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("akPu2PFCombinedSecondaryVertexBJetTags"), cms.InputTag("akPu2PFCombinedSecondaryVertexV2BJetTags"), cms.InputTag("akPu2PFJetBProbabilityBJetTags"), 
        cms.InputTag("akPu2PFJetProbabilityBJetTags"), cms.InputTag("akPu2PFTrackCountingHighEffBJetTags"), cms.InputTag("akPu2PFTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akPu2PFmatch"),
    genPartonMatch = cms.InputTag("akPu2PFparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2PFcorr")),
    jetIDMap = cms.InputTag("akPu2PFJetID"),
    jetSource = cms.InputTag("akPu2PFJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("akPu2PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.akPu3CaloCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"), cms.InputTag("akPu3CaloSecondaryVertexTagInfos"))
)


process.akPu3CaloCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"), cms.InputTag("akPu3CaloSecondaryVertexTagInfos"))
)


process.akPu3CaloImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("akPu3CaloJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.akPu3CaloJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))
)


process.akPu3CaloJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("akPu3CaloJets"),
    useRecHits = cms.bool(True)
)


process.akPu3CaloJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))
)


process.akPu3CaloJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("akPu3CaloJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.akPu3CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(6),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.3),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akPu3CaloNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"), cms.InputTag("akPu3CaloSecondaryVertexNegativeTagInfos"))
)


process.akPu3CaloNegativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))
)


process.akPu3CaloNegativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))
)


process.akPu3CaloNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloSecondaryVertexNegativeTagInfos"))
)


process.akPu3CaloNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloSecondaryVertexNegativeTagInfos"))
)


process.akPu3CaloNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloSoftPFMuonsTagInfos"))
)


process.akPu3CaloNegativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))
)


process.akPu3CaloNegativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))
)


process.akPu3CaloPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("akPu3CaloPatJetPartonAssociationLegacy")
)


process.akPu3CaloPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("akPu3CaloJets"),
    partons = cms.InputTag("myPartons")
)


process.akPu3CaloPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.akPu3CaloPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"), cms.InputTag("akPu3CaloSecondaryVertexTagInfos"))
)


process.akPu3CaloPositiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))
)


process.akPu3CaloPositiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))
)


process.akPu3CaloPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloSoftPFMuonsTagInfos"))
)


process.akPu3CaloSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akPu3CaloImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akPu3CaloSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akPu3CaloImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akPu3CaloSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloSecondaryVertexTagInfos"))
)


process.akPu3CaloSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloSecondaryVertexTagInfos"))
)


process.akPu3CaloSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloSoftPFMuonsTagInfos"))
)


process.akPu3CaloSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloSoftPFMuonsTagInfos"))
)


process.akPu3CaloSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloSoftPFMuonsTagInfos"))
)


process.akPu3CaloSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("akPu3CaloJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.akPu3CaloTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))
)


process.akPu3CaloTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3CaloImpactParameterTagInfos"))
)


process.akPu3Calocorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute'),
    payload = cms.string('AKPu3Calo_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akPu3CaloJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akPu3Calomatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak3HiGenJets"),
    maxDeltaR = cms.double(0.3),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akPu3CaloJets")
)


process.akPu3Caloparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akPu3CaloJets")
)


process.akPu3CalopatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akPu3CaloPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akPu3CaloPatJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("akPu3CaloSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("akPu3CaloSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("akPu3CaloCombinedSecondaryVertexBJetTags"), cms.InputTag("akPu3CaloCombinedSecondaryVertexV2BJetTags"), cms.InputTag("akPu3CaloJetBProbabilityBJetTags"), 
        cms.InputTag("akPu3CaloJetProbabilityBJetTags"), cms.InputTag("akPu3CaloTrackCountingHighEffBJetTags"), cms.InputTag("akPu3CaloTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akPu3Calomatch"),
    genPartonMatch = cms.InputTag("akPu3Caloparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3Calocorr")),
    jetIDMap = cms.InputTag("akPu3CaloJetID"),
    jetSource = cms.InputTag("akPu3CaloJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("akPu3CaloJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.akPu3PFCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"), cms.InputTag("akPu3PFSecondaryVertexTagInfos"))
)


process.akPu3PFCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"), cms.InputTag("akPu3PFSecondaryVertexTagInfos"))
)


process.akPu3PFImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("akPu3PFJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.akPu3PFJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))
)


process.akPu3PFJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("akPu3CaloJets"),
    useRecHits = cms.bool(True)
)


process.akPu3PFJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))
)


process.akPu3PFJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("akPu3PFJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.akPu3PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('BasicJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(15),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.3),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("PFTowers"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akPu3PFNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"), cms.InputTag("akPu3PFSecondaryVertexNegativeTagInfos"))
)


process.akPu3PFNegativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))
)


process.akPu3PFNegativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))
)


process.akPu3PFNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFSecondaryVertexNegativeTagInfos"))
)


process.akPu3PFNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFSecondaryVertexNegativeTagInfos"))
)


process.akPu3PFNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFSoftPFMuonsTagInfos"))
)


process.akPu3PFNegativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))
)


process.akPu3PFNegativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))
)


process.akPu3PFPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("akPu3PFPatJetPartonAssociationLegacy")
)


process.akPu3PFPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("akPu3PFJets"),
    partons = cms.InputTag("myPartons")
)


process.akPu3PFPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.akPu3PFPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"), cms.InputTag("akPu3PFSecondaryVertexTagInfos"))
)


process.akPu3PFPositiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))
)


process.akPu3PFPositiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))
)


process.akPu3PFPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFSoftPFMuonsTagInfos"))
)


process.akPu3PFSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akPu3PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akPu3PFSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akPu3PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akPu3PFSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFSecondaryVertexTagInfos"))
)


process.akPu3PFSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFSecondaryVertexTagInfos"))
)


process.akPu3PFSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFSoftPFMuonsTagInfos"))
)


process.akPu3PFSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFSoftPFMuonsTagInfos"))
)


process.akPu3PFSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFSoftPFMuonsTagInfos"))
)


process.akPu3PFSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("akPu3PFJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.akPu3PFTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))
)


process.akPu3PFTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu3PFImpactParameterTagInfos"))
)


process.akPu3PFcorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute'),
    payload = cms.string('AKPu3PF_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akPu3PFJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akPu3PFmatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak3HiGenJets"),
    maxDeltaR = cms.double(0.3),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akPu3PFJets")
)


process.akPu3PFparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akPu3PFJets")
)


process.akPu3PFpatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akPu3PFPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akPu3PFPatJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("akPu3PFSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("akPu3PFSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("akPu3PFCombinedSecondaryVertexBJetTags"), cms.InputTag("akPu3PFCombinedSecondaryVertexV2BJetTags"), cms.InputTag("akPu3PFJetBProbabilityBJetTags"), 
        cms.InputTag("akPu3PFJetProbabilityBJetTags"), cms.InputTag("akPu3PFTrackCountingHighEffBJetTags"), cms.InputTag("akPu3PFTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akPu3PFmatch"),
    genPartonMatch = cms.InputTag("akPu3PFparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3PFcorr")),
    jetIDMap = cms.InputTag("akPu3PFJetID"),
    jetSource = cms.InputTag("akPu3PFJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("akPu3PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.akPu4CaloCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"), cms.InputTag("akPu4CaloSecondaryVertexTagInfos"))
)


process.akPu4CaloCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"), cms.InputTag("akPu4CaloSecondaryVertexTagInfos"))
)


process.akPu4CaloImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("akPu4CaloJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.akPu4CaloJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))
)


process.akPu4CaloJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("akPu4CaloJets"),
    useRecHits = cms.bool(True)
)


process.akPu4CaloJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))
)


process.akPu4CaloJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("akPu4CaloJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.akPu4CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(8),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akPu4CaloNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"), cms.InputTag("akPu4CaloSecondaryVertexNegativeTagInfos"))
)


process.akPu4CaloNegativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))
)


process.akPu4CaloNegativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))
)


process.akPu4CaloNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloSecondaryVertexNegativeTagInfos"))
)


process.akPu4CaloNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloSecondaryVertexNegativeTagInfos"))
)


process.akPu4CaloNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloSoftPFMuonsTagInfos"))
)


process.akPu4CaloNegativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))
)


process.akPu4CaloNegativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))
)


process.akPu4CaloPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("akPu4CaloPatJetPartonAssociationLegacy")
)


process.akPu4CaloPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("akPu4CaloJets"),
    partons = cms.InputTag("myPartons")
)


process.akPu4CaloPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.akPu4CaloPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"), cms.InputTag("akPu4CaloSecondaryVertexTagInfos"))
)


process.akPu4CaloPositiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))
)


process.akPu4CaloPositiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))
)


process.akPu4CaloPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloSoftPFMuonsTagInfos"))
)


process.akPu4CaloSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akPu4CaloImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akPu4CaloSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akPu4CaloImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akPu4CaloSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloSecondaryVertexTagInfos"))
)


process.akPu4CaloSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloSecondaryVertexTagInfos"))
)


process.akPu4CaloSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloSoftPFMuonsTagInfos"))
)


process.akPu4CaloSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloSoftPFMuonsTagInfos"))
)


process.akPu4CaloSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloSoftPFMuonsTagInfos"))
)


process.akPu4CaloSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("akPu4CaloJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.akPu4CaloTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))
)


process.akPu4CaloTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"))
)


process.akPu4Calocorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute'),
    payload = cms.string('AKPu4Calo_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akPu4CaloJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akPu4Calomatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak4HiGenJets"),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akPu4CaloJets")
)


process.akPu4Caloparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akPu4CaloJets")
)


process.akPu4CalopatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akPu4CaloPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akPu4CaloPatJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("akPu4CaloSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("akPu4CaloSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("akPu4CaloCombinedSecondaryVertexBJetTags"), cms.InputTag("akPu4CaloCombinedSecondaryVertexV2BJetTags"), cms.InputTag("akPu4CaloJetBProbabilityBJetTags"), 
        cms.InputTag("akPu4CaloJetProbabilityBJetTags"), cms.InputTag("akPu4CaloTrackCountingHighEffBJetTags"), cms.InputTag("akPu4CaloTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akPu4Calomatch"),
    genPartonMatch = cms.InputTag("akPu4Caloparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4Calocorr")),
    jetIDMap = cms.InputTag("akPu4CaloJetID"),
    jetSource = cms.InputTag("akPu4CaloJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("akPu4CaloJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.akPu4PFCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"), cms.InputTag("akPu4PFSecondaryVertexTagInfos"))
)


process.akPu4PFCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"), cms.InputTag("akPu4PFSecondaryVertexTagInfos"))
)


process.akPu4PFImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("akPu4PFJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.akPu4PFJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))
)


process.akPu4PFJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("akPu4CaloJets"),
    useRecHits = cms.bool(True)
)


process.akPu4PFJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))
)


process.akPu4PFJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("akPu4PFJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.akPu4PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('BasicJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(20),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("PFTowers"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akPu4PFNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"), cms.InputTag("akPu4PFSecondaryVertexNegativeTagInfos"))
)


process.akPu4PFNegativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))
)


process.akPu4PFNegativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))
)


process.akPu4PFNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFSecondaryVertexNegativeTagInfos"))
)


process.akPu4PFNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFSecondaryVertexNegativeTagInfos"))
)


process.akPu4PFNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFSoftPFMuonsTagInfos"))
)


process.akPu4PFNegativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))
)


process.akPu4PFNegativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))
)


process.akPu4PFPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("akPu4PFPatJetPartonAssociationLegacy")
)


process.akPu4PFPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("akPu4PFJets"),
    partons = cms.InputTag("myPartons")
)


process.akPu4PFPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.akPu4PFPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"), cms.InputTag("akPu4PFSecondaryVertexTagInfos"))
)


process.akPu4PFPositiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))
)


process.akPu4PFPositiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))
)


process.akPu4PFPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFSoftPFMuonsTagInfos"))
)


process.akPu4PFSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akPu4PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akPu4PFSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akPu4PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akPu4PFSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFSecondaryVertexTagInfos"))
)


process.akPu4PFSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFSecondaryVertexTagInfos"))
)


process.akPu4PFSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFSoftPFMuonsTagInfos"))
)


process.akPu4PFSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFSoftPFMuonsTagInfos"))
)


process.akPu4PFSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFSoftPFMuonsTagInfos"))
)


process.akPu4PFSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("akPu4PFJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.akPu4PFTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))
)


process.akPu4PFTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"))
)


process.akPu4PFcorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute'),
    payload = cms.string('AKPu4PF_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akPu4PFJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akPu4PFmatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak4HiGenJets"),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akPu4PFJets")
)


process.akPu4PFparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akPu4PFJets")
)


process.akPu4PFpatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akPu4PFPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akPu4PFPatJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("akPu4PFSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("akPu4PFSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("akPu4PFCombinedSecondaryVertexBJetTags"), cms.InputTag("akPu4PFCombinedSecondaryVertexV2BJetTags"), cms.InputTag("akPu4PFJetBProbabilityBJetTags"), 
        cms.InputTag("akPu4PFJetProbabilityBJetTags"), cms.InputTag("akPu4PFTrackCountingHighEffBJetTags"), cms.InputTag("akPu4PFTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akPu4PFmatch"),
    genPartonMatch = cms.InputTag("akPu4PFparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4PFcorr")),
    jetIDMap = cms.InputTag("akPu4PFJetID"),
    jetSource = cms.InputTag("akPu4PFJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("akPu4PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.akPu5CaloCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"), cms.InputTag("akPu5CaloSecondaryVertexTagInfos"))
)


process.akPu5CaloCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"), cms.InputTag("akPu5CaloSecondaryVertexTagInfos"))
)


process.akPu5CaloImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("akPu5CaloJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.akPu5CaloJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))
)


process.akPu5CaloJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("akPu5CaloJets"),
    useRecHits = cms.bool(True)
)


process.akPu5CaloJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))
)


process.akPu5CaloJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("akPu5CaloJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.akPu5CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.5),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akPu5CaloNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"), cms.InputTag("akPu5CaloSecondaryVertexNegativeTagInfos"))
)


process.akPu5CaloNegativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))
)


process.akPu5CaloNegativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))
)


process.akPu5CaloNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloSecondaryVertexNegativeTagInfos"))
)


process.akPu5CaloNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloSecondaryVertexNegativeTagInfos"))
)


process.akPu5CaloNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloSoftPFMuonsTagInfos"))
)


process.akPu5CaloNegativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))
)


process.akPu5CaloNegativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))
)


process.akPu5CaloPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("akPu5CaloPatJetPartonAssociationLegacy")
)


process.akPu5CaloPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("akPu5CaloJets"),
    partons = cms.InputTag("myPartons")
)


process.akPu5CaloPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.akPu5CaloPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"), cms.InputTag("akPu5CaloSecondaryVertexTagInfos"))
)


process.akPu5CaloPositiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))
)


process.akPu5CaloPositiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))
)


process.akPu5CaloPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloSoftPFMuonsTagInfos"))
)


process.akPu5CaloSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akPu5CaloImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akPu5CaloSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akPu5CaloImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akPu5CaloSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloSecondaryVertexTagInfos"))
)


process.akPu5CaloSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloSecondaryVertexTagInfos"))
)


process.akPu5CaloSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloSoftPFMuonsTagInfos"))
)


process.akPu5CaloSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloSoftPFMuonsTagInfos"))
)


process.akPu5CaloSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloSoftPFMuonsTagInfos"))
)


process.akPu5CaloSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("akPu5CaloJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.akPu5CaloTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))
)


process.akPu5CaloTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5CaloImpactParameterTagInfos"))
)


process.akPu5Calocorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute'),
    payload = cms.string('AKPu5Calo_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akPu5CaloJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akPu5Calomatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak5HiGenJets"),
    maxDeltaR = cms.double(0.5),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akPu5CaloJets")
)


process.akPu5Caloparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akPu5CaloJets")
)


process.akPu5CalopatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akPu5CaloPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akPu5CaloPatJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("akPu5CaloSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("akPu5CaloSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("akPu5CaloCombinedSecondaryVertexBJetTags"), cms.InputTag("akPu5CaloCombinedSecondaryVertexV2BJetTags"), cms.InputTag("akPu5CaloJetBProbabilityBJetTags"), 
        cms.InputTag("akPu5CaloJetProbabilityBJetTags"), cms.InputTag("akPu5CaloTrackCountingHighEffBJetTags"), cms.InputTag("akPu5CaloTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akPu5Calomatch"),
    genPartonMatch = cms.InputTag("akPu5Caloparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu5Calocorr")),
    jetIDMap = cms.InputTag("akPu5CaloJetID"),
    jetSource = cms.InputTag("akPu5CaloJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("akPu5CaloJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.akPu5PFCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"), cms.InputTag("akPu5PFSecondaryVertexTagInfos"))
)


process.akPu5PFCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"), cms.InputTag("akPu5PFSecondaryVertexTagInfos"))
)


process.akPu5PFImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("akPu5PFJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.akPu5PFJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))
)


process.akPu5PFJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("akPu5CaloJets"),
    useRecHits = cms.bool(True)
)


process.akPu5PFJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))
)


process.akPu5PFJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("akPu5PFJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.akPu5PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('BasicJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(25),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.5),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("PFTowers"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akPu5PFNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"), cms.InputTag("akPu5PFSecondaryVertexNegativeTagInfos"))
)


process.akPu5PFNegativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))
)


process.akPu5PFNegativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))
)


process.akPu5PFNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFSecondaryVertexNegativeTagInfos"))
)


process.akPu5PFNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFSecondaryVertexNegativeTagInfos"))
)


process.akPu5PFNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFSoftPFMuonsTagInfos"))
)


process.akPu5PFNegativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))
)


process.akPu5PFNegativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))
)


process.akPu5PFPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("akPu5PFPatJetPartonAssociationLegacy")
)


process.akPu5PFPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("akPu5PFJets"),
    partons = cms.InputTag("myPartons")
)


process.akPu5PFPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.akPu5PFPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"), cms.InputTag("akPu5PFSecondaryVertexTagInfos"))
)


process.akPu5PFPositiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))
)


process.akPu5PFPositiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))
)


process.akPu5PFPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFSoftPFMuonsTagInfos"))
)


process.akPu5PFSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akPu5PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akPu5PFSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akPu5PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akPu5PFSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFSecondaryVertexTagInfos"))
)


process.akPu5PFSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFSecondaryVertexTagInfos"))
)


process.akPu5PFSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFSoftPFMuonsTagInfos"))
)


process.akPu5PFSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFSoftPFMuonsTagInfos"))
)


process.akPu5PFSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFSoftPFMuonsTagInfos"))
)


process.akPu5PFSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("akPu5PFJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.akPu5PFTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))
)


process.akPu5PFTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu5PFImpactParameterTagInfos"))
)


process.akPu5PFcorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute'),
    payload = cms.string('AKPu5PF_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akPu5PFJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akPu5PFmatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak5HiGenJets"),
    maxDeltaR = cms.double(0.5),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akPu5PFJets")
)


process.akPu5PFparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akPu5PFJets")
)


process.akPu5PFpatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akPu5PFPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akPu5PFPatJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("akPu5PFSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("akPu5PFSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("akPu5PFCombinedSecondaryVertexBJetTags"), cms.InputTag("akPu5PFCombinedSecondaryVertexV2BJetTags"), cms.InputTag("akPu5PFJetBProbabilityBJetTags"), 
        cms.InputTag("akPu5PFJetProbabilityBJetTags"), cms.InputTag("akPu5PFTrackCountingHighEffBJetTags"), cms.InputTag("akPu5PFTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akPu5PFmatch"),
    genPartonMatch = cms.InputTag("akPu5PFparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu5PFcorr")),
    jetIDMap = cms.InputTag("akPu5PFJetID"),
    jetSource = cms.InputTag("akPu5PFJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("akPu5PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.akPu6CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(12),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.6),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akPu6PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('BasicJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(30),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.6),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("PFTowers"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akPu7CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(14),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.7),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akPu7PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(10),
    jetType = cms.string('BasicJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(35),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.7),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("PFTowers"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akVs1CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    bkg = cms.InputTag("voronoiBackgroundCalo"),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.1),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('VoronoiSubtractor'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akVs1PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    bkg = cms.InputTag("voronoiBackgroundPF"),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(0),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.1),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlowTmp"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('VoronoiSubtractor'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akVs2CaloCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloImpactParameterTagInfos"), cms.InputTag("akVs2CaloSecondaryVertexTagInfos"))
)


process.akVs2CaloCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloImpactParameterTagInfos"), cms.InputTag("akVs2CaloSecondaryVertexTagInfos"))
)


process.akVs2CaloImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("akVs2CaloJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.akVs2CaloJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloImpactParameterTagInfos"))
)


process.akVs2CaloJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("akVs2CaloJets"),
    useRecHits = cms.bool(True)
)


process.akVs2CaloJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloImpactParameterTagInfos"))
)


process.akVs2CaloJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("akVs2CaloJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.akVs2CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    bkg = cms.InputTag("voronoiBackgroundCalo"),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.2),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('VoronoiSubtractor'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akVs2CaloNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloImpactParameterTagInfos"), cms.InputTag("akVs2CaloSecondaryVertexNegativeTagInfos"))
)


process.akVs2CaloNegativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloImpactParameterTagInfos"))
)


process.akVs2CaloNegativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloImpactParameterTagInfos"))
)


process.akVs2CaloNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloSecondaryVertexNegativeTagInfos"))
)


process.akVs2CaloNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloSecondaryVertexNegativeTagInfos"))
)


process.akVs2CaloNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloSoftPFMuonsTagInfos"))
)


process.akVs2CaloNegativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloImpactParameterTagInfos"))
)


process.akVs2CaloNegativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloImpactParameterTagInfos"))
)


process.akVs2CaloPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("akVs2CaloPatJetPartonAssociationLegacy")
)


process.akVs2CaloPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("akVs2CaloJets"),
    partons = cms.InputTag("myPartons")
)


process.akVs2CaloPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.akVs2CaloPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloImpactParameterTagInfos"), cms.InputTag("akVs2CaloSecondaryVertexTagInfos"))
)


process.akVs2CaloPositiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloImpactParameterTagInfos"))
)


process.akVs2CaloPositiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloImpactParameterTagInfos"))
)


process.akVs2CaloPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloSoftPFMuonsTagInfos"))
)


process.akVs2CaloSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akVs2CaloImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akVs2CaloSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akVs2CaloImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akVs2CaloSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloSecondaryVertexTagInfos"))
)


process.akVs2CaloSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloSecondaryVertexTagInfos"))
)


process.akVs2CaloSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloSoftPFMuonsTagInfos"))
)


process.akVs2CaloSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloSoftPFMuonsTagInfos"))
)


process.akVs2CaloSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloSoftPFMuonsTagInfos"))
)


process.akVs2CaloSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("akVs2CaloJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.akVs2CaloTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloImpactParameterTagInfos"))
)


process.akVs2CaloTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2CaloImpactParameterTagInfos"))
)


process.akVs2Calocorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute'),
    payload = cms.string('AK2Calo_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akVs2CaloJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akVs2Calomatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak2HiGenJets"),
    maxDeltaR = cms.double(0.2),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akVs2CaloJets")
)


process.akVs2Caloparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akVs2CaloJets")
)


process.akVs2CalopatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akVs2CaloPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akVs2CaloPatJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("akVs2CaloSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("akVs2CaloSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("akVs2CaloCombinedSecondaryVertexBJetTags"), cms.InputTag("akVs2CaloCombinedSecondaryVertexV2BJetTags"), cms.InputTag("akVs2CaloJetBProbabilityBJetTags"), 
        cms.InputTag("akVs2CaloJetProbabilityBJetTags"), cms.InputTag("akVs2CaloTrackCountingHighEffBJetTags"), cms.InputTag("akVs2CaloTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akVs2Calomatch"),
    genPartonMatch = cms.InputTag("akVs2Caloparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs2Calocorr")),
    jetIDMap = cms.InputTag("akVs2CaloJetID"),
    jetSource = cms.InputTag("akVs2CaloJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("akVs2CaloJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.akVs2PFCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFImpactParameterTagInfos"), cms.InputTag("akVs2PFSecondaryVertexTagInfos"))
)


process.akVs2PFCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFImpactParameterTagInfos"), cms.InputTag("akVs2PFSecondaryVertexTagInfos"))
)


process.akVs2PFImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("akVs2PFJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.akVs2PFJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFImpactParameterTagInfos"))
)


process.akVs2PFJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("akVs2CaloJets"),
    useRecHits = cms.bool(True)
)


process.akVs2PFJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFImpactParameterTagInfos"))
)


process.akVs2PFJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("akVs2PFJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.akVs2PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    bkg = cms.InputTag("voronoiBackgroundPF"),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(0),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.2),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlowTmp"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('VoronoiSubtractor'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akVs2PFNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFImpactParameterTagInfos"), cms.InputTag("akVs2PFSecondaryVertexNegativeTagInfos"))
)


process.akVs2PFNegativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFImpactParameterTagInfos"))
)


process.akVs2PFNegativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFImpactParameterTagInfos"))
)


process.akVs2PFNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFSecondaryVertexNegativeTagInfos"))
)


process.akVs2PFNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFSecondaryVertexNegativeTagInfos"))
)


process.akVs2PFNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFSoftPFMuonsTagInfos"))
)


process.akVs2PFNegativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFImpactParameterTagInfos"))
)


process.akVs2PFNegativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFImpactParameterTagInfos"))
)


process.akVs2PFPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("akVs2PFPatJetPartonAssociationLegacy")
)


process.akVs2PFPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("akVs2PFJets"),
    partons = cms.InputTag("myPartons")
)


process.akVs2PFPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.akVs2PFPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFImpactParameterTagInfos"), cms.InputTag("akVs2PFSecondaryVertexTagInfos"))
)


process.akVs2PFPositiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFImpactParameterTagInfos"))
)


process.akVs2PFPositiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFImpactParameterTagInfos"))
)


process.akVs2PFPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFSoftPFMuonsTagInfos"))
)


process.akVs2PFSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akVs2PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akVs2PFSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akVs2PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akVs2PFSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFSecondaryVertexTagInfos"))
)


process.akVs2PFSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFSecondaryVertexTagInfos"))
)


process.akVs2PFSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFSoftPFMuonsTagInfos"))
)


process.akVs2PFSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFSoftPFMuonsTagInfos"))
)


process.akVs2PFSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFSoftPFMuonsTagInfos"))
)


process.akVs2PFSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("akVs2PFJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.akVs2PFTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFImpactParameterTagInfos"))
)


process.akVs2PFTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs2PFImpactParameterTagInfos"))
)


process.akVs2PFcorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute'),
    payload = cms.string('AK2PF_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akVs2PFJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akVs2PFmatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak2HiGenJets"),
    maxDeltaR = cms.double(0.2),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akVs2PFJets")
)


process.akVs2PFparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akVs2PFJets")
)


process.akVs2PFpatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akVs2PFPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akVs2PFPatJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("akVs2PFSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("akVs2PFSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("akVs2PFCombinedSecondaryVertexBJetTags"), cms.InputTag("akVs2PFCombinedSecondaryVertexV2BJetTags"), cms.InputTag("akVs2PFJetBProbabilityBJetTags"), 
        cms.InputTag("akVs2PFJetProbabilityBJetTags"), cms.InputTag("akVs2PFTrackCountingHighEffBJetTags"), cms.InputTag("akVs2PFTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akVs2PFmatch"),
    genPartonMatch = cms.InputTag("akVs2PFparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs2PFcorr")),
    jetIDMap = cms.InputTag("akVs2PFJetID"),
    jetSource = cms.InputTag("akVs2PFJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("akVs2PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.akVs3CaloCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloImpactParameterTagInfos"), cms.InputTag("akVs3CaloSecondaryVertexTagInfos"))
)


process.akVs3CaloCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloImpactParameterTagInfos"), cms.InputTag("akVs3CaloSecondaryVertexTagInfos"))
)


process.akVs3CaloImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("akVs3CaloJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.akVs3CaloJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloImpactParameterTagInfos"))
)


process.akVs3CaloJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("akVs3CaloJets"),
    useRecHits = cms.bool(True)
)


process.akVs3CaloJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloImpactParameterTagInfos"))
)


process.akVs3CaloJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("akVs3CaloJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.akVs3CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    bkg = cms.InputTag("voronoiBackgroundCalo"),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.3),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('VoronoiSubtractor'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akVs3CaloNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloImpactParameterTagInfos"), cms.InputTag("akVs3CaloSecondaryVertexNegativeTagInfos"))
)


process.akVs3CaloNegativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloImpactParameterTagInfos"))
)


process.akVs3CaloNegativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloImpactParameterTagInfos"))
)


process.akVs3CaloNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloSecondaryVertexNegativeTagInfos"))
)


process.akVs3CaloNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloSecondaryVertexNegativeTagInfos"))
)


process.akVs3CaloNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloSoftPFMuonsTagInfos"))
)


process.akVs3CaloNegativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloImpactParameterTagInfos"))
)


process.akVs3CaloNegativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloImpactParameterTagInfos"))
)


process.akVs3CaloPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("akVs3CaloPatJetPartonAssociationLegacy")
)


process.akVs3CaloPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("akVs3CaloJets"),
    partons = cms.InputTag("myPartons")
)


process.akVs3CaloPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.akVs3CaloPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloImpactParameterTagInfos"), cms.InputTag("akVs3CaloSecondaryVertexTagInfos"))
)


process.akVs3CaloPositiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloImpactParameterTagInfos"))
)


process.akVs3CaloPositiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloImpactParameterTagInfos"))
)


process.akVs3CaloPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloSoftPFMuonsTagInfos"))
)


process.akVs3CaloSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akVs3CaloImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akVs3CaloSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akVs3CaloImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akVs3CaloSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloSecondaryVertexTagInfos"))
)


process.akVs3CaloSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloSecondaryVertexTagInfos"))
)


process.akVs3CaloSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloSoftPFMuonsTagInfos"))
)


process.akVs3CaloSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloSoftPFMuonsTagInfos"))
)


process.akVs3CaloSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloSoftPFMuonsTagInfos"))
)


process.akVs3CaloSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("akVs3CaloJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.akVs3CaloTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloImpactParameterTagInfos"))
)


process.akVs3CaloTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3CaloImpactParameterTagInfos"))
)


process.akVs3Calocorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute'),
    payload = cms.string('AK3Calo_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akVs3CaloJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akVs3Calomatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak3HiGenJets"),
    maxDeltaR = cms.double(0.3),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akVs3CaloJets")
)


process.akVs3Caloparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akVs3CaloJets")
)


process.akVs3CalopatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akVs3CaloPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akVs3CaloPatJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("akVs3CaloSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("akVs3CaloSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("akVs3CaloCombinedSecondaryVertexBJetTags"), cms.InputTag("akVs3CaloCombinedSecondaryVertexV2BJetTags"), cms.InputTag("akVs3CaloJetBProbabilityBJetTags"), 
        cms.InputTag("akVs3CaloJetProbabilityBJetTags"), cms.InputTag("akVs3CaloTrackCountingHighEffBJetTags"), cms.InputTag("akVs3CaloTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akVs3Calomatch"),
    genPartonMatch = cms.InputTag("akVs3Caloparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs3Calocorr")),
    jetIDMap = cms.InputTag("akVs3CaloJetID"),
    jetSource = cms.InputTag("akVs3CaloJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("akVs3CaloJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.akVs3PFCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFImpactParameterTagInfos"), cms.InputTag("akVs3PFSecondaryVertexTagInfos"))
)


process.akVs3PFCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFImpactParameterTagInfos"), cms.InputTag("akVs3PFSecondaryVertexTagInfos"))
)


process.akVs3PFImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("akVs3PFJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.akVs3PFJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFImpactParameterTagInfos"))
)


process.akVs3PFJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("akVs3CaloJets"),
    useRecHits = cms.bool(True)
)


process.akVs3PFJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFImpactParameterTagInfos"))
)


process.akVs3PFJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("akVs3PFJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.akVs3PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    bkg = cms.InputTag("voronoiBackgroundPF"),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(0),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.3),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlowTmp"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('VoronoiSubtractor'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akVs3PFNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFImpactParameterTagInfos"), cms.InputTag("akVs3PFSecondaryVertexNegativeTagInfos"))
)


process.akVs3PFNegativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFImpactParameterTagInfos"))
)


process.akVs3PFNegativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFImpactParameterTagInfos"))
)


process.akVs3PFNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFSecondaryVertexNegativeTagInfos"))
)


process.akVs3PFNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFSecondaryVertexNegativeTagInfos"))
)


process.akVs3PFNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFSoftPFMuonsTagInfos"))
)


process.akVs3PFNegativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFImpactParameterTagInfos"))
)


process.akVs3PFNegativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFImpactParameterTagInfos"))
)


process.akVs3PFPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("akVs3PFPatJetPartonAssociationLegacy")
)


process.akVs3PFPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("akVs3PFJets"),
    partons = cms.InputTag("myPartons")
)


process.akVs3PFPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.akVs3PFPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFImpactParameterTagInfos"), cms.InputTag("akVs3PFSecondaryVertexTagInfos"))
)


process.akVs3PFPositiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFImpactParameterTagInfos"))
)


process.akVs3PFPositiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFImpactParameterTagInfos"))
)


process.akVs3PFPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFSoftPFMuonsTagInfos"))
)


process.akVs3PFSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akVs3PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akVs3PFSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akVs3PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akVs3PFSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFSecondaryVertexTagInfos"))
)


process.akVs3PFSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFSecondaryVertexTagInfos"))
)


process.akVs3PFSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFSoftPFMuonsTagInfos"))
)


process.akVs3PFSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFSoftPFMuonsTagInfos"))
)


process.akVs3PFSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFSoftPFMuonsTagInfos"))
)


process.akVs3PFSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("akVs3PFJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.akVs3PFTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFImpactParameterTagInfos"))
)


process.akVs3PFTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs3PFImpactParameterTagInfos"))
)


process.akVs3PFcorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute'),
    payload = cms.string('AK3PF_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akVs3PFJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akVs3PFmatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak3HiGenJets"),
    maxDeltaR = cms.double(0.3),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akVs3PFJets")
)


process.akVs3PFparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akVs3PFJets")
)


process.akVs3PFpatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akVs3PFPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akVs3PFPatJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("akVs3PFSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("akVs3PFSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("akVs3PFCombinedSecondaryVertexBJetTags"), cms.InputTag("akVs3PFCombinedSecondaryVertexV2BJetTags"), cms.InputTag("akVs3PFJetBProbabilityBJetTags"), 
        cms.InputTag("akVs3PFJetProbabilityBJetTags"), cms.InputTag("akVs3PFTrackCountingHighEffBJetTags"), cms.InputTag("akVs3PFTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akVs3PFmatch"),
    genPartonMatch = cms.InputTag("akVs3PFparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs3PFcorr")),
    jetIDMap = cms.InputTag("akVs3PFJetID"),
    jetSource = cms.InputTag("akVs3PFJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("akVs3PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.akVs4CaloCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloImpactParameterTagInfos"), cms.InputTag("akVs4CaloSecondaryVertexTagInfos"))
)


process.akVs4CaloCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloImpactParameterTagInfos"), cms.InputTag("akVs4CaloSecondaryVertexTagInfos"))
)


process.akVs4CaloImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("akVs4CaloJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.akVs4CaloJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloImpactParameterTagInfos"))
)


process.akVs4CaloJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("akVs4CaloJets"),
    useRecHits = cms.bool(True)
)


process.akVs4CaloJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloImpactParameterTagInfos"))
)


process.akVs4CaloJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("akVs4CaloJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.akVs4CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    bkg = cms.InputTag("voronoiBackgroundCalo"),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('VoronoiSubtractor'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akVs4CaloNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloImpactParameterTagInfos"), cms.InputTag("akVs4CaloSecondaryVertexNegativeTagInfos"))
)


process.akVs4CaloNegativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloImpactParameterTagInfos"))
)


process.akVs4CaloNegativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloImpactParameterTagInfos"))
)


process.akVs4CaloNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloSecondaryVertexNegativeTagInfos"))
)


process.akVs4CaloNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloSecondaryVertexNegativeTagInfos"))
)


process.akVs4CaloNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloSoftPFMuonsTagInfos"))
)


process.akVs4CaloNegativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloImpactParameterTagInfos"))
)


process.akVs4CaloNegativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloImpactParameterTagInfos"))
)


process.akVs4CaloPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("akVs4CaloPatJetPartonAssociationLegacy")
)


process.akVs4CaloPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("akVs4CaloJets"),
    partons = cms.InputTag("myPartons")
)


process.akVs4CaloPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.akVs4CaloPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloImpactParameterTagInfos"), cms.InputTag("akVs4CaloSecondaryVertexTagInfos"))
)


process.akVs4CaloPositiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloImpactParameterTagInfos"))
)


process.akVs4CaloPositiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloImpactParameterTagInfos"))
)


process.akVs4CaloPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloSoftPFMuonsTagInfos"))
)


process.akVs4CaloSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akVs4CaloImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akVs4CaloSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akVs4CaloImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akVs4CaloSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloSecondaryVertexTagInfos"))
)


process.akVs4CaloSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloSecondaryVertexTagInfos"))
)


process.akVs4CaloSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloSoftPFMuonsTagInfos"))
)


process.akVs4CaloSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloSoftPFMuonsTagInfos"))
)


process.akVs4CaloSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloSoftPFMuonsTagInfos"))
)


process.akVs4CaloSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("akVs4CaloJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.akVs4CaloTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloImpactParameterTagInfos"))
)


process.akVs4CaloTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4CaloImpactParameterTagInfos"))
)


process.akVs4Calocorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute'),
    payload = cms.string('AK4Calo_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akVs4CaloJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akVs4Calomatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak4HiGenJets"),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akVs4CaloJets")
)


process.akVs4Caloparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akVs4CaloJets")
)


process.akVs4CalopatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akVs4CaloPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akVs4CaloPatJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("akVs4CaloSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("akVs4CaloSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("akVs4CaloCombinedSecondaryVertexBJetTags"), cms.InputTag("akVs4CaloCombinedSecondaryVertexV2BJetTags"), cms.InputTag("akVs4CaloJetBProbabilityBJetTags"), 
        cms.InputTag("akVs4CaloJetProbabilityBJetTags"), cms.InputTag("akVs4CaloTrackCountingHighEffBJetTags"), cms.InputTag("akVs4CaloTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akVs4Calomatch"),
    genPartonMatch = cms.InputTag("akVs4Caloparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs4Calocorr")),
    jetIDMap = cms.InputTag("akVs4CaloJetID"),
    jetSource = cms.InputTag("akVs4CaloJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("akVs4CaloJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.akVs4PFCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFImpactParameterTagInfos"), cms.InputTag("akVs4PFSecondaryVertexTagInfos"))
)


process.akVs4PFCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFImpactParameterTagInfos"), cms.InputTag("akVs4PFSecondaryVertexTagInfos"))
)


process.akVs4PFImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("akVs4PFJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.akVs4PFJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFImpactParameterTagInfos"))
)


process.akVs4PFJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("akVs4CaloJets"),
    useRecHits = cms.bool(True)
)


process.akVs4PFJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFImpactParameterTagInfos"))
)


process.akVs4PFJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("akVs4PFJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.akVs4PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    bkg = cms.InputTag("voronoiBackgroundPF"),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(0),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlowTmp"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('VoronoiSubtractor'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akVs4PFNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFImpactParameterTagInfos"), cms.InputTag("akVs4PFSecondaryVertexNegativeTagInfos"))
)


process.akVs4PFNegativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFImpactParameterTagInfos"))
)


process.akVs4PFNegativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFImpactParameterTagInfos"))
)


process.akVs4PFNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFSecondaryVertexNegativeTagInfos"))
)


process.akVs4PFNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFSecondaryVertexNegativeTagInfos"))
)


process.akVs4PFNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFSoftPFMuonsTagInfos"))
)


process.akVs4PFNegativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFImpactParameterTagInfos"))
)


process.akVs4PFNegativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFImpactParameterTagInfos"))
)


process.akVs4PFPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("akVs4PFPatJetPartonAssociationLegacy")
)


process.akVs4PFPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("akVs4PFJets"),
    partons = cms.InputTag("myPartons")
)


process.akVs4PFPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.akVs4PFPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFImpactParameterTagInfos"), cms.InputTag("akVs4PFSecondaryVertexTagInfos"))
)


process.akVs4PFPositiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFImpactParameterTagInfos"))
)


process.akVs4PFPositiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFImpactParameterTagInfos"))
)


process.akVs4PFPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFSoftPFMuonsTagInfos"))
)


process.akVs4PFSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akVs4PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akVs4PFSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akVs4PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akVs4PFSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFSecondaryVertexTagInfos"))
)


process.akVs4PFSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFSecondaryVertexTagInfos"))
)


process.akVs4PFSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFSoftPFMuonsTagInfos"))
)


process.akVs4PFSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFSoftPFMuonsTagInfos"))
)


process.akVs4PFSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFSoftPFMuonsTagInfos"))
)


process.akVs4PFSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("akVs4PFJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.akVs4PFTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFImpactParameterTagInfos"))
)


process.akVs4PFTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs4PFImpactParameterTagInfos"))
)


process.akVs4PFcorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute'),
    payload = cms.string('AK4PF_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akVs4PFJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akVs4PFmatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak4HiGenJets"),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akVs4PFJets")
)


process.akVs4PFparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akVs4PFJets")
)


process.akVs4PFpatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akVs4PFPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akVs4PFPatJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("akVs4PFSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("akVs4PFSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("akVs4PFCombinedSecondaryVertexBJetTags"), cms.InputTag("akVs4PFCombinedSecondaryVertexV2BJetTags"), cms.InputTag("akVs4PFJetBProbabilityBJetTags"), 
        cms.InputTag("akVs4PFJetProbabilityBJetTags"), cms.InputTag("akVs4PFTrackCountingHighEffBJetTags"), cms.InputTag("akVs4PFTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akVs4PFmatch"),
    genPartonMatch = cms.InputTag("akVs4PFparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs4PFcorr")),
    jetIDMap = cms.InputTag("akVs4PFJetID"),
    jetSource = cms.InputTag("akVs4PFJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("akVs4PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.akVs5CaloCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloImpactParameterTagInfos"), cms.InputTag("akVs5CaloSecondaryVertexTagInfos"))
)


process.akVs5CaloCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloImpactParameterTagInfos"), cms.InputTag("akVs5CaloSecondaryVertexTagInfos"))
)


process.akVs5CaloImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("akVs5CaloJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.akVs5CaloJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloImpactParameterTagInfos"))
)


process.akVs5CaloJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("akVs5CaloJets"),
    useRecHits = cms.bool(True)
)


process.akVs5CaloJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloImpactParameterTagInfos"))
)


process.akVs5CaloJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("akVs5CaloJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.akVs5CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    bkg = cms.InputTag("voronoiBackgroundCalo"),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.5),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('VoronoiSubtractor'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akVs5CaloNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloImpactParameterTagInfos"), cms.InputTag("akVs5CaloSecondaryVertexNegativeTagInfos"))
)


process.akVs5CaloNegativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloImpactParameterTagInfos"))
)


process.akVs5CaloNegativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloImpactParameterTagInfos"))
)


process.akVs5CaloNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloSecondaryVertexNegativeTagInfos"))
)


process.akVs5CaloNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloSecondaryVertexNegativeTagInfos"))
)


process.akVs5CaloNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloSoftPFMuonsTagInfos"))
)


process.akVs5CaloNegativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloImpactParameterTagInfos"))
)


process.akVs5CaloNegativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloImpactParameterTagInfos"))
)


process.akVs5CaloPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("akVs5CaloPatJetPartonAssociationLegacy")
)


process.akVs5CaloPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("akVs5CaloJets"),
    partons = cms.InputTag("myPartons")
)


process.akVs5CaloPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.akVs5CaloPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloImpactParameterTagInfos"), cms.InputTag("akVs5CaloSecondaryVertexTagInfos"))
)


process.akVs5CaloPositiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloImpactParameterTagInfos"))
)


process.akVs5CaloPositiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloImpactParameterTagInfos"))
)


process.akVs5CaloPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloSoftPFMuonsTagInfos"))
)


process.akVs5CaloSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akVs5CaloImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akVs5CaloSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akVs5CaloImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akVs5CaloSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloSecondaryVertexTagInfos"))
)


process.akVs5CaloSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloSecondaryVertexTagInfos"))
)


process.akVs5CaloSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloSoftPFMuonsTagInfos"))
)


process.akVs5CaloSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloSoftPFMuonsTagInfos"))
)


process.akVs5CaloSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloSoftPFMuonsTagInfos"))
)


process.akVs5CaloSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("akVs5CaloJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.akVs5CaloTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloImpactParameterTagInfos"))
)


process.akVs5CaloTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5CaloImpactParameterTagInfos"))
)


process.akVs5Calocorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute'),
    payload = cms.string('AK5Calo_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akVs5CaloJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akVs5Calomatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak5HiGenJets"),
    maxDeltaR = cms.double(0.5),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akVs5CaloJets")
)


process.akVs5Caloparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akVs5CaloJets")
)


process.akVs5CalopatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akVs5CaloPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akVs5CaloPatJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("akVs5CaloSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("akVs5CaloSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("akVs5CaloCombinedSecondaryVertexBJetTags"), cms.InputTag("akVs5CaloCombinedSecondaryVertexV2BJetTags"), cms.InputTag("akVs5CaloJetBProbabilityBJetTags"), 
        cms.InputTag("akVs5CaloJetProbabilityBJetTags"), cms.InputTag("akVs5CaloTrackCountingHighEffBJetTags"), cms.InputTag("akVs5CaloTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akVs5Calomatch"),
    genPartonMatch = cms.InputTag("akVs5Caloparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs5Calocorr")),
    jetIDMap = cms.InputTag("akVs5CaloJetID"),
    jetSource = cms.InputTag("akVs5CaloJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("akVs5CaloJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.akVs5PFCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFImpactParameterTagInfos"), cms.InputTag("akVs5PFSecondaryVertexTagInfos"))
)


process.akVs5PFCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFImpactParameterTagInfos"), cms.InputTag("akVs5PFSecondaryVertexTagInfos"))
)


process.akVs5PFImpactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("akVs5PFJetTracksAssociatorAtVertex"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.akVs5PFJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFImpactParameterTagInfos"))
)


process.akVs5PFJetID = cms.EDProducer("JetIDProducer",
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    src = cms.InputTag("akVs5CaloJets"),
    useRecHits = cms.bool(True)
)


process.akVs5PFJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFImpactParameterTagInfos"))
)


process.akVs5PFJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("akVs5PFJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("highPurityTracks"),
    useAssigned = cms.bool(False)
)


process.akVs5PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    bkg = cms.InputTag("voronoiBackgroundPF"),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(0),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.5),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlowTmp"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('VoronoiSubtractor'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akVs5PFNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFImpactParameterTagInfos"), cms.InputTag("akVs5PFSecondaryVertexNegativeTagInfos"))
)


process.akVs5PFNegativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFImpactParameterTagInfos"))
)


process.akVs5PFNegativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFImpactParameterTagInfos"))
)


process.akVs5PFNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFSecondaryVertexNegativeTagInfos"))
)


process.akVs5PFNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFSecondaryVertexNegativeTagInfos"))
)


process.akVs5PFNegativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFSoftPFMuonsTagInfos"))
)


process.akVs5PFNegativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFImpactParameterTagInfos"))
)


process.akVs5PFNegativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFImpactParameterTagInfos"))
)


process.akVs5PFPatJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("akVs5PFPatJetPartonAssociationLegacy")
)


process.akVs5PFPatJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("akVs5PFJets"),
    partons = cms.InputTag("myPartons")
)


process.akVs5PFPatJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.akVs5PFPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFImpactParameterTagInfos"), cms.InputTag("akVs5PFSecondaryVertexTagInfos"))
)


process.akVs5PFPositiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFImpactParameterTagInfos"))
)


process.akVs5PFPositiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFImpactParameterTagInfos"))
)


process.akVs5PFPositiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFSoftPFMuonsTagInfos"))
)


process.akVs5PFSecondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akVs5PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akVs5PFSecondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("akVs5PFImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.akVs5PFSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFSecondaryVertexTagInfos"))
)


process.akVs5PFSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFSecondaryVertexTagInfos"))
)


process.akVs5PFSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFSoftPFMuonsTagInfos"))
)


process.akVs5PFSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFSoftPFMuonsTagInfos"))
)


process.akVs5PFSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFSoftPFMuonsTagInfos"))
)


process.akVs5PFSoftPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("akVs5PFJets"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.akVs5PFTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFImpactParameterTagInfos"))
)


process.akVs5PFTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("akVs5PFImpactParameterTagInfos"))
)


process.akVs5PFcorr = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L2Relative', 
        'L3Absolute'),
    payload = cms.string('AK5PF_offline'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("akVs5PFJets"),
    useNPV = cms.bool(False),
    useRho = cms.bool(False)
)


process.akVs5PFmatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak5HiGenJets"),
    maxDeltaR = cms.double(0.5),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akVs5PFJets")
)


process.akVs5PFparton = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("akVs5PFJets")
)


process.akVs5PFpatJetsWithBtagging = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("akVs5PFPatJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("akVs5PFPatJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("akVs5PFSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("akVs5PFSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("akVs5PFCombinedSecondaryVertexBJetTags"), cms.InputTag("akVs5PFCombinedSecondaryVertexV2BJetTags"), cms.InputTag("akVs5PFJetBProbabilityBJetTags"), 
        cms.InputTag("akVs5PFJetProbabilityBJetTags"), cms.InputTag("akVs5PFTrackCountingHighEffBJetTags"), cms.InputTag("akVs5PFTrackCountingHighPurBJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(False),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("akVs5PFmatch"),
    genPartonMatch = cms.InputTag("akVs5PFparton"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs5PFcorr")),
    jetIDMap = cms.InputTag("akVs5PFJetID"),
    jetSource = cms.InputTag("akVs5PFJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("akVs5PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.akVs6CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    bkg = cms.InputTag("voronoiBackgroundCalo"),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.6),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('VoronoiSubtractor'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akVs6PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    bkg = cms.InputTag("voronoiBackgroundPF"),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(1),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(0),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.6),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlowTmp"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('VoronoiSubtractor'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akVs7CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    bkg = cms.InputTag("voronoiBackgroundCalo"),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.7),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('VoronoiSubtractor'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.akVs7PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    bkg = cms.InputTag("voronoiBackgroundPF"),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(10),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(0),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.7),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlowTmp"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('VoronoiSubtractor'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.bToCharmDecayVertexMerged = cms.EDProducer("BtoCharmDecayVertexMerger",
    maxDRUnique = cms.double(0.4),
    maxPtreltomerge = cms.double(7777.0),
    maxvecSumIMifsmallDRUnique = cms.double(5.5),
    minCosPAtomerge = cms.double(0.99),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("inclusiveSecondaryVerticesFiltered")
)


process.caloTowers = cms.EDProducer("CaloTowerCandidateCreator",
    e = cms.double(0.0),
    et = cms.double(0.0),
    minimumE = cms.double(0.0),
    minimumEt = cms.double(0.0),
    pt = cms.double(0.0),
    src = cms.InputTag("towerMaker"),
    verbose = cms.untracked.int32(0)
)


process.calotowermaker = cms.EDProducer("CaloTowersCreator",
    AllowMissingInputs = cms.bool(False),
    EBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    EBSumThreshold = cms.double(0.2),
    EBThreshold = cms.double(0.07),
    EBWeight = cms.double(1.0),
    EBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    EEGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    EESumThreshold = cms.double(0.45),
    EEThreshold = cms.double(0.3),
    EEWeight = cms.double(1.0),
    EEWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring('kTime', 
        'kWeird', 
        'kBad'),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(),
    EcutTower = cms.double(-1000.0),
    HBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HBThreshold = cms.double(0.7),
    HBWeight = cms.double(1.0),
    HBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HEDGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HEDThreshold = cms.double(0.8),
    HEDWeight = cms.double(1.0),
    HEDWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HESGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HESThreshold = cms.double(0.8),
    HESWeight = cms.double(1.0),
    HESWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HF1Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HF1Threshold = cms.double(0.5),
    HF1Weight = cms.double(1.0),
    HF1Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HF2Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HF2Threshold = cms.double(0.85),
    HF2Weight = cms.double(1.0),
    HF2Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HOGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HOThreshold0 = cms.double(1.1),
    HOThresholdMinus1 = cms.double(3.5),
    HOThresholdMinus2 = cms.double(3.5),
    HOThresholdPlus1 = cms.double(3.5),
    HOThresholdPlus2 = cms.double(3.5),
    HOWeight = cms.double(1.0),
    HOWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HcalAcceptSeverityLevel = cms.uint32(9),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32(9999),
    HcalThreshold = cms.double(-1000.0),
    MomConstrMethod = cms.int32(1),
    MomEBDepth = cms.double(0.3),
    MomEEDepth = cms.double(0.0),
    MomHBDepth = cms.double(0.2),
    MomHEDepth = cms.double(0.4),
    UseEcalRecoveredHits = cms.bool(False),
    UseEtEBTreshold = cms.bool(False),
    UseEtEETreshold = cms.bool(False),
    UseHO = cms.bool(True),
    UseHcalRecoveredHits = cms.bool(True),
    UseRejectedHitsOnly = cms.bool(False),
    UseRejectedRecoveredEcalHits = cms.bool(False),
    UseRejectedRecoveredHcalHits = cms.bool(True),
    UseSymEBTreshold = cms.bool(True),
    UseSymEETreshold = cms.bool(True),
    ecalInputs = cms.VInputTag(cms.InputTag("ecalRecHit","EcalRecHitsEB"), cms.InputTag("ecalRecHit","EcalRecHitsEE")),
    hbheInput = cms.InputTag("hbhereco"),
    hfInput = cms.InputTag("hfreco"),
    hoInput = cms.InputTag("horeco")
)


process.candidateVertexArbitrator = cms.EDProducer("CandidateVertexArbitrator",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    dLenFraction = cms.double(0.333),
    dRCut = cms.double(0.4),
    distCut = cms.double(0.04),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("candidateVertexMerger"),
    sigCut = cms.double(5),
    trackMinLayers = cms.int32(4),
    trackMinPixels = cms.int32(1),
    trackMinPt = cms.double(0.4),
    tracks = cms.InputTag("particleFlow")
)


process.candidateVertexArbitratorCtagL = cms.EDProducer("CandidateVertexArbitrator",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    dLenFraction = cms.double(0.333),
    dRCut = cms.double(0.4),
    distCut = cms.double(0.04),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("candidateVertexMergerCtagL"),
    sigCut = cms.double(5),
    trackMinLayers = cms.int32(4),
    trackMinPixels = cms.int32(1),
    trackMinPt = cms.double(0.4),
    tracks = cms.InputTag("particleFlow")
)


process.candidateVertexMerger = cms.EDProducer("CandidateVertexMerger",
    maxFraction = cms.double(0.7),
    minSignificance = cms.double(2),
    secondaryVertices = cms.InputTag("inclusiveCandidateVertexFinder")
)


process.candidateVertexMergerCtagL = cms.EDProducer("CandidateVertexMerger",
    maxFraction = cms.double(0.7),
    minSignificance = cms.double(2),
    secondaryVertices = cms.InputTag("inclusiveCandidateVertexFinderCtagL")
)


process.centralityBin = cms.EDProducer("CentralityBinProducer",
    Centrality = cms.InputTag("hiCentrality"),
    centralityVariable = cms.string('HFtowers'),
    nonDefaultGlauberModel = cms.string(''),
    pPbRunFlip = cms.uint32(99999999)
)


process.combinedInclusiveSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("inclusiveSecondaryVertexFinderTagInfos"))
)


process.combinedInclusiveSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("inclusiveSecondaryVertexFinderTagInfos"))
)


process.combinedMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedMVAComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("inclusiveSecondaryVertexFinderTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.combinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexTagInfos"))
)


process.combinedSecondaryVertexSoftLeptonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexSoftLeptonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.combinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexTagInfos"))
)


process.doubleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('doubleVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("inclusiveSecondaryVertexFinderFilteredTagInfos"))
)


process.ghostTrackBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('ghostTrackComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("ghostTrackVertexTagInfos"))
)


process.ghostTrackVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(1),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('gtvr'),
        fitType = cms.string('RefitGhostTrackWithVertices'),
        maxFitChi2 = cms.double(10.0),
        mergeThreshold = cms.double(3.0),
        primcut = cms.double(2.0),
        seccut = cms.double(4.0)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.impactParameterMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('impactParameterMVAComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.impactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.inclusiveCandidateSecondaryVertices = cms.EDProducer("CandidateVertexMerger",
    maxFraction = cms.double(0.2),
    minSignificance = cms.double(10.0),
    secondaryVertices = cms.InputTag("candidateVertexArbitrator")
)


process.inclusiveCandidateSecondaryVerticesCtagL = cms.EDProducer("CandidateVertexMerger",
    maxFraction = cms.double(0.2),
    minSignificance = cms.double(10.0),
    secondaryVertices = cms.InputTag("candidateVertexArbitratorCtagL")
)


process.inclusiveCandidateVertexFinder = cms.EDProducer("InclusiveCandidateVertexFinder",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterizer = cms.PSet(
        clusterMaxDistance = cms.double(0.05),
        clusterMaxSignificance = cms.double(4.5),
        clusterMinAngleCosine = cms.double(0.5),
        distanceRatio = cms.double(20),
        seedMax3DIPSignificance = cms.double(9999.0),
        seedMax3DIPValue = cms.double(9999.0),
        seedMin3DIPSignificance = cms.double(1.2),
        seedMin3DIPValue = cms.double(0.005)
    ),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxNTracks = cms.uint32(30),
    maximumLongitudinalImpactParameter = cms.double(0.3),
    minHits = cms.uint32(8),
    minPt = cms.double(0.8),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("particleFlow"),
    useDirectVertexFitter = cms.bool(True),
    useVertexReco = cms.bool(True),
    vertexMinAngleCosine = cms.double(0.95),
    vertexMinDLen2DSig = cms.double(2.5),
    vertexMinDLenSig = cms.double(0.5),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        primcut = cms.double(1.0),
        seccut = cms.double(3),
        smoothing = cms.bool(True)
    )
)


process.inclusiveCandidateVertexFinderCtagL = cms.EDProducer("InclusiveCandidateVertexFinder",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterizer = cms.PSet(
        clusterMaxDistance = cms.double(0.05),
        clusterMaxSignificance = cms.double(4.5),
        clusterMinAngleCosine = cms.double(0.5),
        distanceRatio = cms.double(10),
        seedMax3DIPSignificance = cms.double(9999.0),
        seedMax3DIPValue = cms.double(9999.0),
        seedMin3DIPSignificance = cms.double(1.0),
        seedMin3DIPValue = cms.double(0.005)
    ),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxNTracks = cms.uint32(30),
    maximumLongitudinalImpactParameter = cms.double(0.3),
    minHits = cms.uint32(8),
    minPt = cms.double(0.8),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("particleFlow"),
    useDirectVertexFitter = cms.bool(True),
    useVertexReco = cms.bool(True),
    vertexMinAngleCosine = cms.double(0.95),
    vertexMinDLen2DSig = cms.double(1.25),
    vertexMinDLenSig = cms.double(0.25),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        primcut = cms.double(1.0),
        seccut = cms.double(3),
        smoothing = cms.bool(True)
    )
)


process.inclusiveSecondaryVertexFinderFilteredNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("bToCharmDecayVertexMerged"),
    extSVDeltaRToJet = cms.double(-0.4),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-2.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.inclusiveSecondaryVertexFinderFilteredTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("bToCharmDecayVertexMerged"),
    extSVDeltaRToJet = cms.double(0.4),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.inclusiveSecondaryVertexFinderNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveSecondaryVertices"),
    extSVDeltaRToJet = cms.double(-0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-2.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.inclusiveSecondaryVertexFinderTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.inclusiveSecondaryVertices = cms.EDProducer("VertexMerger",
    maxFraction = cms.double(0.2),
    minSignificance = cms.double(10.0),
    secondaryVertices = cms.InputTag("trackVertexArbitrator")
)


process.inclusiveVertexFinder = cms.EDProducer("InclusiveVertexFinder",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterizer = cms.PSet(
        clusterMaxDistance = cms.double(0.05),
        clusterMaxSignificance = cms.double(4.5),
        clusterMinAngleCosine = cms.double(0.5),
        distanceRatio = cms.double(20),
        seedMax3DIPSignificance = cms.double(9999.0),
        seedMax3DIPValue = cms.double(9999.0),
        seedMin3DIPSignificance = cms.double(1.2),
        seedMin3DIPValue = cms.double(0.005)
    ),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxNTracks = cms.uint32(30),
    maximumLongitudinalImpactParameter = cms.double(0.3),
    minHits = cms.uint32(8),
    minPt = cms.double(0.8),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useDirectVertexFitter = cms.bool(True),
    useVertexReco = cms.bool(True),
    vertexMinAngleCosine = cms.double(0.95),
    vertexMinDLen2DSig = cms.double(2.5),
    vertexMinDLenSig = cms.double(0.5),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        primcut = cms.double(1.0),
        seccut = cms.double(3),
        smoothing = cms.bool(True)
    )
)


process.iterativeConePu5CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('IterativeCone'),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.5),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.jetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.jetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.ktPu4CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('Kt'),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ktPu6CaloJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('Kt'),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.6),
    radiusPU = cms.double(0.7),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.muonHLTL1Match = cms.EDProducer("HLTL1MuonMatcher",
    fallbackToME1 = cms.bool(False),
    l1PhiOffset = cms.double(0.0218166156499),
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltL1extraParticles")'),
    maxDeltaEta = cms.double(99),
    maxDeltaPhi = cms.double(6),
    maxDeltaR = cms.double(0.5),
    resolveAmbiguities = cms.bool(True),
    setPropLabel = cms.string('propagatedToM2'),
    sortBy = cms.string('pt'),
    src = cms.InputTag("muons"),
    useSimpleGeometry = cms.bool(True),
    useState = cms.string('atVertex'),
    useTrack = cms.string('tracker'),
    writeExtraInfo = cms.bool(True)
)


process.muonL1Info = cms.EDProducer("L1MuonMatcher",
    fallbackToME1 = cms.bool(False),
    l1PhiOffset = cms.double(0.0218166156499),
    matched = cms.InputTag("l1extraParticles"),
    maxDeltaEta = cms.double(99),
    maxDeltaPhi = cms.double(6),
    maxDeltaR = cms.double(0.5),
    preselection = cms.string('bx == 0'),
    setL1Label = cms.string('l1'),
    setPropLabel = cms.string('propagated'),
    sortBy = cms.string('pt'),
    src = cms.InputTag("muons"),
    useSimpleGeometry = cms.bool(True),
    useState = cms.string('atVertex'),
    useTrack = cms.string('tracker'),
    writeExtraInfo = cms.bool(True)
)


process.muonMatchHLTCtfTrack = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltMuTrackJpsiCtfTrackCands")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchHLTCtfTrack2 = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltMuTrackJpsiEffCtfTrackCands")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchHLTL1 = cms.EDProducer("HLTL1MuonMatcher",
    fallbackToME1 = cms.bool(False),
    l1PhiOffset = cms.double(0.0218166156499),
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltL1extraParticles")'),
    maxDeltaEta = cms.double(99),
    maxDeltaPhi = cms.double(6),
    maxDeltaR = cms.double(0.5),
    resolveAmbiguities = cms.bool(True),
    setPropLabel = cms.string('propagatedToM2'),
    sortBy = cms.string('pt'),
    src = cms.InputTag("patMuonsWithoutTrigger"),
    useSimpleGeometry = cms.bool(True),
    useState = cms.string('atVertex'),
    useTrack = cms.string('tracker'),
    writeExtraInfo = cms.bool(True)
)


process.muonMatchHLTL2 = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltL2MuonCandidates")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.3),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchHLTL3 = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltHIL3MuonCandidates")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchHLTL3T = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltGlbTrkMuonCands")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchHLTTrackMu = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltMuTkMuJpsiTrackerMuonCands")'),
    maxDPtRel = cms.double(10.0),
    maxDeltaR = cms.double(0.1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.muonMatchL1 = cms.EDProducer("HLTL1MuonMatcher",
    fallbackToME1 = cms.bool(False),
    l1PhiOffset = cms.double(0.0218166156499),
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string('coll("hltL1extraParticles")'),
    maxDeltaEta = cms.double(99),
    maxDeltaPhi = cms.double(6),
    maxDeltaR = cms.double(0.5),
    resolveAmbiguities = cms.bool(True),
    setPropLabel = cms.string('propagatedToM2'),
    sortBy = cms.string('pt'),
    src = cms.InputTag("patMuonsWithoutTrigger"),
    useSimpleGeometry = cms.bool(True),
    useState = cms.string('atVertex'),
    useTrack = cms.string('tracker'),
    writeExtraInfo = cms.bool(True)
)


process.muonTriggerMatchHLT = cms.EDProducer("PATTriggerMatcherDRDPtLessByR",
    matched = cms.InputTag("patTrigger"),
    matchedCuts = cms.string(''),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.negativeCombinedInclusiveSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("inclusiveSecondaryVertexFinderNegativeTagInfos"))
)


process.negativeCombinedInclusiveSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("inclusiveSecondaryVertexFinderNegativeTagInfos"))
)


process.negativeCombinedMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedMVAComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("inclusiveSecondaryVertexFinderNegativeTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.negativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexNegativeTagInfos"))
)


process.negativeCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexNegativeTagInfos"))
)


process.negativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.negativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.negativeSimpleInclusiveSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("inclusiveSecondaryVertexFinderFilteredNegativeTagInfos"))
)


process.negativeSimpleInclusiveSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("inclusiveSecondaryVertexFinderFilteredNegativeTagInfos"))
)


process.negativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexNegativeTagInfos"))
)


process.negativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexNegativeTagInfos"))
)


process.negativeSoftPFElectronBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFElectronComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.negativeSoftPFElectronByIP2dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFElectronByIP2dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.negativeSoftPFElectronByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFElectronByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.negativeSoftPFElectronByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFElectronByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.negativeSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.negativeSoftPFMuonByIP2dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByIP2dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.negativeSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.negativeSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.negativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.negativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('negativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.offlinePrimaryVertices = cms.EDProducer("PrimaryVertexProducer",
    TkClusParameters = cms.PSet(
        TkDAClusParameters = cms.PSet(
            Tmin = cms.double(4.0),
            coolingFactor = cms.double(0.6),
            d0CutOff = cms.double(3.0),
            dzCutOff = cms.double(4.0),
            vertexSize = cms.double(0.01)
        ),
        algorithm = cms.string('DA_vect')
    ),
    TkFilterParameters = cms.PSet(
        algorithm = cms.string('filter'),
        maxD0Significance = cms.double(5.0),
        maxNormalizedChi2 = cms.double(20.0),
        minPixelLayersWithHits = cms.int32(2),
        minPt = cms.double(0.0),
        minSiliconLayersWithHits = cms.int32(5),
        trackQuality = cms.string('any')
    ),
    TrackLabel = cms.InputTag("highPurityTracks"),
    beamSpotLabel = cms.InputTag("offlineBeamSpot"),
    verbose = cms.untracked.bool(False),
    vertexCollections = cms.VPSet(cms.PSet(
        algorithm = cms.string('AdaptiveVertexFitter'),
        label = cms.string(''),
        maxDistanceToBeam = cms.double(1.0),
        minNdof = cms.double(0.0),
        useBeamConstraint = cms.bool(False)
    ), 
        cms.PSet(
            algorithm = cms.string('AdaptiveVertexFitter'),
            label = cms.string('WithBS'),
            maxDistanceToBeam = cms.double(1.0),
            minNdof = cms.double(2.0),
            useBeamConstraint = cms.bool(True)
        ))
)


process.patElectrons = cms.EDProducer("PATElectronProducer",
    addEfficiencies = cms.bool(False),
    addElectronID = cms.bool(False),
    addGenMatch = cms.bool(True),
    addPFClusterIso = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    efficiencies = cms.PSet(

    ),
    electronIDSources = cms.PSet(
        eidLoose = cms.InputTag("eidLoose"),
        eidRobustHighEnergy = cms.InputTag("eidRobustHighEnergy"),
        eidRobustLoose = cms.InputTag("eidRobustLoose"),
        eidRobustTight = cms.InputTag("eidRobustTight"),
        eidTight = cms.InputTag("eidTight")
    ),
    electronSource = cms.InputTag("gedGsfElectronsTmp"),
    embedBasicClusters = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedGsfElectronCore = cms.bool(True),
    embedGsfTrack = cms.bool(True),
    embedHighLevelSelection = cms.bool(True),
    embedPFCandidate = cms.bool(True),
    embedPflowBasicClusters = cms.bool(True),
    embedPflowPreshowerClusters = cms.bool(True),
    embedPflowSuperCluster = cms.bool(True),
    embedPreshowerClusters = cms.bool(True),
    embedRecHits = cms.bool(True),
    embedSeedCluster = cms.bool(True),
    embedSuperCluster = cms.bool(True),
    embedTrack = cms.bool(True),
    genParticleMatch = cms.InputTag("electronMatch"),
    isoDeposits = cms.PSet(

    ),
    pfCandidateMap = cms.InputTag("particleFlow","electrons"),
    pfElectronSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertex"),
    reducedBarrelRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    resolutions = cms.PSet(

    ),
    useParticleFlow = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patJetCorrFactors = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute'),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak4PFJetsCHS"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetFlavourAssociation = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak4PFJetsCHS"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","algorithmicPartons"),
    rParam = cms.double(0.4)
)


process.patJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacy")
)


process.patJetGenJetMatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak4GenJets"),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak4PFJetsCHS")
)


process.patJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak4PFJetsCHS"),
    partons = cms.InputTag("patJetPartonsLegacy")
)


process.patJetPartonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(1, 2, 3, 4, 5, 
        21),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak4PFJetsCHS")
)


process.patJetPartons = cms.EDProducer("HadronAndPartonSelector",
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.patJetPartonsLegacy = cms.EDProducer("PartonSelector",
    src = cms.InputTag("genParticles"),
    withLeptons = cms.bool(False)
)


process.patJets = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("combinedSecondaryVertexBJetTags"), cms.InputTag("pfJetBProbabilityBJetTags"), cms.InputTag("pfJetProbabilityBJetTags"), cms.InputTag("pfTrackCountingHighPurBJetTags"), cms.InputTag("pfTrackCountingHighEffBJetTags"), 
        cms.InputTag("pfSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("pfSimpleSecondaryVertexHighPurBJetTags"), cms.InputTag("pfCombinedSecondaryVertexV2BJetTags"), cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"), cms.InputTag("softPFMuonBJetTags"), 
        cms.InputTag("softPFElectronBJetTags"), cms.InputTag("pfCombinedMVABJetTags")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatch"),
    genPartonMatch = cms.InputTag("patJetPartonMatch"),
    getJetMCFlavour = cms.bool(True),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactors")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak4PFJetsCHS"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patMuonsWithTrigger = cms.EDProducer("PATTriggerMatchMuonEmbedder",
    matches = cms.VInputTag(cms.InputTag("muonMatchHLTL2"), cms.InputTag("muonMatchHLTL3"), cms.InputTag("muonMatchHLTL3T"), cms.InputTag("muonMatchHLTCtfTrack"), cms.InputTag("muonMatchHLTCtfTrack2"), 
        cms.InputTag("muonMatchHLTTrackMu")),
    src = cms.InputTag("patMuonsWithoutTrigger")
)


process.patMuonsWithoutTrigger = cms.EDProducer("PATMuonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    caloMETMuonCorrs = cms.InputTag("muonMETValueMapProducer","muCorrData"),
    efficiencies = cms.PSet(

    ),
    embedCaloMETMuonCorrs = cms.bool(False),
    embedCombinedMuon = cms.bool(True),
    embedDytMuon = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedHighLevelSelection = cms.bool(True),
    embedMuonBestTrack = cms.bool(True),
    embedPFCandidate = cms.bool(False),
    embedPfEcalEnergy = cms.bool(False),
    embedPickyMuon = cms.bool(False),
    embedStandAloneMuon = cms.bool(True),
    embedTcMETMuonCorrs = cms.bool(False),
    embedTpfmsMuon = cms.bool(False),
    embedTrack = cms.bool(True),
    embedTunePMuonBestTrack = cms.bool(True),
    forceBestTrackEmbedding = cms.bool(False),
    genParticleMatch = cms.InputTag("muonMatch"),
    isoDeposits = cms.PSet(

    ),
    muonSource = cms.InputTag("muons"),
    pfMuonSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertex"),
    resolutions = cms.PSet(

    ),
    tcMETMuonCorrs = cms.InputTag("muonTCMETValueMapProducer","muCorrData"),
    useParticleFlow = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag(cms.InputTag("muonL1Info"))
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag()
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag(cms.InputTag("muonL1Info","deltaR"))
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag(cms.InputTag("muonL1Info","quality"))
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patPhotons = cms.EDProducer("PATPhotonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(True),
    addPFClusterIso = cms.bool(False),
    addPhotonID = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    efficiencies = cms.PSet(

    ),
    electronSource = cms.InputTag("gedGsfElectronsTmp"),
    embedBasicClusters = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedPreshowerClusters = cms.bool(True),
    embedRecHits = cms.bool(False),
    embedSeedCluster = cms.bool(True),
    embedSuperCluster = cms.bool(True),
    genParticleMatch = cms.InputTag("photonMatch"),
    isoDeposits = cms.PSet(

    ),
    photonIDSources = cms.PSet(
        PhotonCutBasedIDLoose = cms.InputTag("PhotonIDProdGED","PhotonCutBasedIDLoose"),
        PhotonCutBasedIDTight = cms.InputTag("PhotonIDProdGED","PhotonCutBasedIDTight")
    ),
    photonSource = cms.InputTag("photons"),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    resolutions = cms.PSet(

    ),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patTrigger = cms.EDProducer("TriggerObjectFilterByCollection",
    collections = cms.vstring('hltL1extraParticles', 
        'hltL2MuonCandidates', 
        'hltGlbTrkMuonCands', 
        'hltMuTrackJpsiCtfTrackCands', 
        'hltMuTrackJpsiEffCtfTrackCands', 
        'hltMuTkMuJpsiTrackerMuonCands', 
        'hltHIL3MuonCandidates'),
    src = cms.InputTag("patTriggerFull")
)


process.patTriggerFull = cms.EDProducer("PATTriggerProducer",
    l1GtReadoutRecordInputTag = cms.InputTag("gtDigis","","RECO"),
    onlyStandAlone = cms.bool(True),
    processName = cms.string('HLT')
)


process.pfBoostedDoubleSecondaryVertexAK8BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexAK8Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosAK8"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAK8"), cms.InputTag("softPFMuonsTagInfosAK8"), cms.InputTag("softPFElectronsTagInfosAK8"))
)


process.pfBoostedDoubleSecondaryVertexCA15BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexCA15Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfosCA15"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosCA15"), cms.InputTag("softPFMuonsTagInfosCA15"), cms.InputTag("softPFElectronsTagInfosCA15"))
)


process.pfCombinedInclusiveSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos"))
)


process.pfCombinedInclusiveSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos"))
)


process.pfCombinedMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedMVAComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.pfCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfSecondaryVertexTagInfos"))
)


process.pfCombinedSecondaryVertexSoftLeptonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedSecondaryVertexSoftLeptonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.pfCombinedSecondaryVertexSoftLeptonCtagLJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedSecondaryVertexSoftLeptonCtagLComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCtagLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.pfCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfSecondaryVertexTagInfos"))
)


process.pfImpactParameterTagInfos = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("particleFlow"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak4PFJetsCHS"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosAK8 = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("particleFlow"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PFJetsCHS"),
    maxDeltaR = cms.double(0.8),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosCA15 = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("particleFlow"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ca15PFJetsCHS"),
    maxDeltaR = cms.double(1.5),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfInclusiveSecondaryVertexFinderCtagLNegativeTagInfos = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveCandidateSecondaryVerticesCtagL"),
    extSVDeltaRToJet = cms.double(-0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-2.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderCtagLTagInfos = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveCandidateSecondaryVerticesCtagL"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(1.5),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderNegativeTagInfos = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveCandidateSecondaryVertices"),
    extSVDeltaRToJet = cms.double(-0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-2.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfos = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveCandidateSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosAK8 = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveCandidateSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.8),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAK8"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.8),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosCA15 = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("inclusiveCandidateSecondaryVertices"),
    extSVDeltaRToJet = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosCA15"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(1.5),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(1.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfNegativeCombinedInclusiveSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderNegativeTagInfos"))
)


process.pfNegativeCombinedInclusiveSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderNegativeTagInfos"))
)


process.pfNegativeCombinedMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeCombinedMVAComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderNegativeTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.pfNegativeCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfSecondaryVertexNegativeTagInfos"))
)


process.pfNegativeCombinedSecondaryVertexSoftLeptonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeCombinedSecondaryVertexSoftLeptonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderNegativeTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.pfNegativeCombinedSecondaryVertexSoftLeptonCtagLJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeCombinedSecondaryVertexSoftLeptonCtagLComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCtagLNegativeTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.pfNegativeCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfSecondaryVertexNegativeTagInfos"))
)


process.pfNegativeOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfNegativeOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfNegativeSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateSimpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfSecondaryVertexNegativeTagInfos"))
)


process.pfNegativeSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateSimpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfSecondaryVertexNegativeTagInfos"))
)


process.pfNegativeTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfNegativeTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateNegativeTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfPositiveCombinedInclusiveSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidatePositiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos"))
)


process.pfPositiveCombinedInclusiveSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidatePositiveCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos"))
)


process.pfPositiveCombinedMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidatePositiveCombinedMVAComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.pfPositiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidatePositiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfSecondaryVertexTagInfos"))
)


process.pfPositiveCombinedSecondaryVertexSoftLeptonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidatePositiveCombinedSecondaryVertexSoftLeptonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.pfPositiveCombinedSecondaryVertexSoftLeptonCtagLJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidatePositiveCombinedSecondaryVertexSoftLeptonCtagLComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCtagLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.pfPositiveCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidatePositiveCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfSecondaryVertexTagInfos"))
)


process.pfPositiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidatePositiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfPositiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidatePositiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfSecondaryVertexNegativeTagInfos = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfSecondaryVertexTagInfos = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfSimpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateSimpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfSecondaryVertexTagInfos"))
)


process.pfSimpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateSimpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfSecondaryVertexTagInfos"))
)


process.pfTrackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateTrackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.pfTrackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateTrackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"))
)


process.positiveCombinedInclusiveSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("inclusiveSecondaryVertexFinderTagInfos"))
)


process.positiveCombinedInclusiveSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("inclusiveSecondaryVertexFinderTagInfos"))
)


process.positiveCombinedMVABJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedMVAComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("inclusiveSecondaryVertexFinderTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos"))
)


process.positiveCombinedSecondaryVertexBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexTagInfos"))
)


process.positiveCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveCombinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexTagInfos"))
)


process.positiveOnlyJetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.positiveOnlyJetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.positiveSoftPFElectronBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFElectronComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.positiveSoftPFElectronByIP2dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFElectronByIP2dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.positiveSoftPFElectronByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFElectronByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.positiveSoftPFElectronByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFElectronByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.positiveSoftPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.positiveSoftPFMuonByIP2dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByIP2dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.positiveSoftPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.positiveSoftPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('positiveSoftPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.secondaryVertexNegativeTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(-3.0),
        distSig2dMin = cms.double(-99999.9),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(-0.01),
        distVal2dMin = cms.double(-2.5),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(-0.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.secondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.siPixelRecHits = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("siPixelClusters")
)


process.siPixelRecHitsPreSplitting = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("siPixelClustersPreSplitting")
)


process.simpleInclusiveSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("inclusiveSecondaryVertexFinderFilteredTagInfos"))
)


process.simpleInclusiveSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("inclusiveSecondaryVertexFinderFilteredTagInfos"))
)


process.simpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfos"))
)


process.simpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfos"))
)


process.softMuonTagInfos = cms.EDProducer("SoftLepton",
    jets = cms.InputTag("ak4PFJetsCHS"),
    leptonCands = cms.InputTag(""),
    leptonChi2Cut = cms.double(9999.0),
    leptonDeltaRCut = cms.double(0.4),
    leptonId = cms.InputTag(""),
    leptons = cms.InputTag("muons"),
    muonSelection = cms.uint32(1),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    refineJetAxis = cms.uint32(0)
)


process.softPFElectronBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFElectronComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.softPFElectronByIP2dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFElectronByIP2dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.softPFElectronByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFElectronByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.softPFElectronByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFElectronByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFElectronsTagInfos"))
)


process.softPFElectronsTagInfos = cms.EDProducer("SoftPFElectronTagInfoProducer",
    DeltaRElectronJet = cms.double(0.4),
    MaxSip3D = cms.double(200),
    electrons = cms.InputTag("gedGsfElectrons"),
    jets = cms.InputTag("ak4PFJetsCHS"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.softPFElectronsTagInfosAK8 = cms.EDProducer("SoftPFElectronTagInfoProducer",
    DeltaRElectronJet = cms.double(0.8),
    MaxSip3D = cms.double(200),
    electrons = cms.InputTag("gedGsfElectrons"),
    jets = cms.InputTag("ak8PFJetsCHS"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.softPFElectronsTagInfosCA15 = cms.EDProducer("SoftPFElectronTagInfoProducer",
    DeltaRElectronJet = cms.double(1.5),
    MaxSip3D = cms.double(200),
    electrons = cms.InputTag("gedGsfElectrons"),
    jets = cms.InputTag("ca15PFJetsCHS"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.softPFMuonBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.softPFMuonByIP2dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP2dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.softPFMuonByIP3dBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByIP3dComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.softPFMuonByPtBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('softPFMuonByPtComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("softPFMuonsTagInfos"))
)


process.softPFMuonsTagInfos = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("ak4PFJetsCHS"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.softPFMuonsTagInfosAK8 = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("ak8PFJetsCHS"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.softPFMuonsTagInfosCA15 = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIp = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("ca15PFJetsCHS"),
    muonPt = cms.double(2.0),
    muonSIP = cms.double(200.0),
    muons = cms.InputTag("muons"),
    primaryVertex = cms.InputTag("offlinePrimaryVertices")
)


process.towerMaker = cms.EDProducer("CaloTowersCreator",
    AllowMissingInputs = cms.bool(False),
    EBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    EBSumThreshold = cms.double(0.2),
    EBThreshold = cms.double(0.07),
    EBWeight = cms.double(1.0),
    EBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    EEGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    EESumThreshold = cms.double(0.45),
    EEThreshold = cms.double(0.3),
    EEWeight = cms.double(1.0),
    EEWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring('kTime', 
        'kWeird', 
        'kBad'),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(),
    EcutTower = cms.double(-1000.0),
    HBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HBThreshold = cms.double(0.7),
    HBWeight = cms.double(1.0),
    HBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HEDGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HEDThreshold = cms.double(0.8),
    HEDWeight = cms.double(1.0),
    HEDWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HESGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HESThreshold = cms.double(0.8),
    HESWeight = cms.double(1.0),
    HESWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HF1Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HF1Threshold = cms.double(0.5),
    HF1Weight = cms.double(1.0),
    HF1Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HF2Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HF2Threshold = cms.double(0.85),
    HF2Weight = cms.double(1.0),
    HF2Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HOGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HOThreshold0 = cms.double(1.1),
    HOThresholdMinus1 = cms.double(3.5),
    HOThresholdMinus2 = cms.double(3.5),
    HOThresholdPlus1 = cms.double(3.5),
    HOThresholdPlus2 = cms.double(3.5),
    HOWeight = cms.double(1.0),
    HOWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HcalAcceptSeverityLevel = cms.uint32(9),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32(9999),
    HcalThreshold = cms.double(-1000.0),
    MomConstrMethod = cms.int32(1),
    MomEBDepth = cms.double(0.3),
    MomEEDepth = cms.double(0.0),
    MomHBDepth = cms.double(0.2),
    MomHEDepth = cms.double(0.4),
    UseEcalRecoveredHits = cms.bool(False),
    UseEtEBTreshold = cms.bool(False),
    UseEtEETreshold = cms.bool(False),
    UseHO = cms.bool(False),
    UseHcalRecoveredHits = cms.bool(True),
    UseRejectedHitsOnly = cms.bool(False),
    UseRejectedRecoveredEcalHits = cms.bool(False),
    UseRejectedRecoveredHcalHits = cms.bool(True),
    UseSymEBTreshold = cms.bool(True),
    UseSymEETreshold = cms.bool(True),
    ecalInputs = cms.VInputTag(cms.InputTag("ecalRecHit","EcalRecHitsEB"), cms.InputTag("ecalRecHit","EcalRecHitsEE")),
    hbheInput = cms.InputTag("hbhereco"),
    hfInput = cms.InputTag("hfreco"),
    hoInput = cms.InputTag("horeco")
)


process.towerMakerWithHO = cms.EDProducer("CaloTowersCreator",
    AllowMissingInputs = cms.bool(False),
    EBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    EBSumThreshold = cms.double(0.2),
    EBThreshold = cms.double(0.07),
    EBWeight = cms.double(1.0),
    EBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    EEGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    EESumThreshold = cms.double(0.45),
    EEThreshold = cms.double(0.3),
    EEWeight = cms.double(1.0),
    EEWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring('kTime', 
        'kWeird', 
        'kBad'),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(),
    EcutTower = cms.double(-1000.0),
    HBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HBThreshold = cms.double(0.7),
    HBWeight = cms.double(1.0),
    HBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HEDGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HEDThreshold = cms.double(0.8),
    HEDWeight = cms.double(1.0),
    HEDWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HESGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HESThreshold = cms.double(0.8),
    HESWeight = cms.double(1.0),
    HESWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HF1Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HF1Threshold = cms.double(0.5),
    HF1Weight = cms.double(1.0),
    HF1Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HF2Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HF2Threshold = cms.double(0.85),
    HF2Weight = cms.double(1.0),
    HF2Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HOGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HOThreshold0 = cms.double(1.1),
    HOThresholdMinus1 = cms.double(3.5),
    HOThresholdMinus2 = cms.double(3.5),
    HOThresholdPlus1 = cms.double(3.5),
    HOThresholdPlus2 = cms.double(3.5),
    HOWeight = cms.double(1.0),
    HOWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HcalAcceptSeverityLevel = cms.uint32(9),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32(9999),
    HcalThreshold = cms.double(-1000.0),
    MomConstrMethod = cms.int32(1),
    MomEBDepth = cms.double(0.3),
    MomEEDepth = cms.double(0.0),
    MomHBDepth = cms.double(0.2),
    MomHEDepth = cms.double(0.4),
    UseEcalRecoveredHits = cms.bool(False),
    UseEtEBTreshold = cms.bool(False),
    UseEtEETreshold = cms.bool(False),
    UseHO = cms.bool(True),
    UseHcalRecoveredHits = cms.bool(True),
    UseRejectedHitsOnly = cms.bool(False),
    UseRejectedRecoveredEcalHits = cms.bool(False),
    UseRejectedRecoveredHcalHits = cms.bool(True),
    UseSymEBTreshold = cms.bool(True),
    UseSymEETreshold = cms.bool(True),
    ecalInputs = cms.VInputTag(cms.InputTag("ecalRecHit","EcalRecHitsEB"), cms.InputTag("ecalRecHit","EcalRecHitsEE")),
    hbheInput = cms.InputTag("hbhereco"),
    hfInput = cms.InputTag("hfreco"),
    hoInput = cms.InputTag("horeco")
)


process.towersAboveThreshold = cms.EDProducer("CaloTowerCandidateCreator",
    minimumE = cms.double(3.0),
    minimumEt = cms.double(0.0),
    src = cms.InputTag("towerMaker"),
    verbose = cms.untracked.int32(0)
)


process.trackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.trackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.trackVertexArbitrator = cms.EDProducer("TrackVertexArbitrator",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    dLenFraction = cms.double(0.333),
    dRCut = cms.double(0.4),
    distCut = cms.double(0.04),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("vertexMerger"),
    sigCut = cms.double(5),
    trackMinLayers = cms.int32(4),
    trackMinPixels = cms.int32(1),
    trackMinPt = cms.double(0.4),
    tracks = cms.InputTag("generalTracks")
)


process.vertexMerger = cms.EDProducer("VertexMerger",
    maxFraction = cms.double(0.7),
    minSignificance = cms.double(2),
    secondaryVertices = cms.InputTag("inclusiveVertexFinder")
)


process.voronoiBackgroundCalo = cms.EDProducer("VoronoiBackgroundProducer",
    doEqualize = cms.bool(False),
    equalizeR = cms.double(0.4),
    equalizeThreshold0 = cms.double(5.0),
    equalizeThreshold1 = cms.double(35.0),
    etaBins = cms.int32(15),
    fourierOrder = cms.int32(5),
    isCalo = cms.bool(True),
    jetCorrectorFormat = cms.bool(True),
    src = cms.InputTag("towerMaker"),
    tableLabel = cms.string('UETable_Calo'),
    useTextTable = cms.bool(False)
)


process.voronoiBackgroundPF = cms.EDProducer("VoronoiBackgroundProducer",
    doEqualize = cms.bool(False),
    equalizeR = cms.double(0.3),
    equalizeThreshold0 = cms.double(5.0),
    equalizeThreshold1 = cms.double(35.0),
    etaBins = cms.int32(15),
    fourierOrder = cms.int32(5),
    isCalo = cms.bool(False),
    jetCorrectorFormat = cms.bool(True),
    src = cms.InputTag("particleFlowTmp"),
    tableLabel = cms.string('UETable_PF'),
    useTextTable = cms.bool(False)
)


process.bVertexFilter = cms.EDFilter("BVertexFilter",
    minVertices = cms.int32(0),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("secondaryVertices"),
    useVertexKinematicAsJetAxis = cms.bool(True),
    vertexFilter = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.1),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    )
)


process.clusterCompatibilityFilter = cms.EDFilter("HIClusterCompatibilityFilter",
    cluscomSrc = cms.InputTag("hiClusterCompatibility"),
    clusterPars = cms.vdouble(0.0, 0.0045),
    clusterTrunc = cms.double(2.0),
    maxZ = cms.double(20.05),
    minZ = cms.double(-20.0),
    nhitsTrunc = cms.int32(150)
)


process.fHBHEIsoNoiseFilterResult = cms.EDFilter("BooleanFlagFilter",
    inputLabel = cms.InputTag("HBHENoiseFilterResultProducer","HBHEIsoNoiseFilterResult"),
    reverseDecision = cms.bool(False)
)


process.fHBHENoiseFilterResult = cms.EDFilter("BooleanFlagFilter",
    inputLabel = cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResult"),
    reverseDecision = cms.bool(False)
)


process.fHBHENoiseFilterResultRun1 = cms.EDFilter("BooleanFlagFilter",
    inputLabel = cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun1"),
    reverseDecision = cms.bool(False)
)


process.fHBHENoiseFilterResultRun2Loose = cms.EDFilter("BooleanFlagFilter",
    inputLabel = cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun2Loose"),
    reverseDecision = cms.bool(False)
)


process.fHBHENoiseFilterResultRun2Tight = cms.EDFilter("BooleanFlagFilter",
    inputLabel = cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun2Tight"),
    reverseDecision = cms.bool(False)
)


process.hfNegFilter = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegFilter2 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(2),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegFilter3 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(3),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegFilter4 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(4),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegFilter5 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(5),
    src = cms.InputTag("hfNegTowers")
)


process.hfNegTowers = cms.EDFilter("EtaPtMinCandSelector",
    etaMax = cms.double(-3.0),
    etaMin = cms.double(-6.0),
    ptMin = cms.double(0),
    src = cms.InputTag("towersAboveThreshold")
)


process.hfPosFilter = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(1),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosFilter2 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(2),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosFilter3 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(3),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosFilter4 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(4),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosFilter5 = cms.EDFilter("CandCountFilter",
    minNumber = cms.uint32(5),
    src = cms.InputTag("hfPosTowers")
)


process.hfPosTowers = cms.EDFilter("EtaPtMinCandSelector",
    etaMax = cms.double(6.0),
    etaMin = cms.double(3.0),
    ptMin = cms.double(0),
    src = cms.InputTag("towersAboveThreshold")
)


process.hiTracks = cms.EDFilter("TrackSelector",
    cut = cms.string('quality("highPurity")'),
    src = cms.InputTag("hiGeneralTracks")
)


process.highPurityTracks = cms.EDFilter("TrackSelector",
    cut = cms.string('quality("highPurity")'),
    src = cms.InputTag("hiGeneralTracks")
)


process.hltLevel1GTSeed = cms.EDFilter("HLTLevel1GTSeed",
    L1CollectionsTag = cms.InputTag("l1extraParticles"),
    L1GtObjectMapTag = cms.InputTag("l1GtObjectMap"),
    L1GtReadoutRecordTag = cms.InputTag("gtDigis"),
    L1MuonCollectionTag = cms.InputTag("l1extraParticles"),
    L1NrBxInEvent = cms.int32(3),
    L1SeedsLogicalExpression = cms.string(''),
    L1TechTriggerSeeding = cms.bool(False),
    L1UseAliasesForSeeding = cms.bool(True),
    L1UseL1TriggerObjectMaps = cms.bool(True),
    saveTags = cms.bool(False)
)


process.hltPixelClusterShapeFilter = cms.EDFilter("HLTPixelClusterShapeFilter",
    clusterPars = cms.vdouble(0, 0.0045),
    clusterTrunc = cms.double(2),
    inputTag = cms.InputTag("siPixelRecHits"),
    maxZ = cms.double(20.05),
    minZ = cms.double(-20),
    nhitsTrunc = cms.int32(150),
    saveTags = cms.bool(False),
    zStep = cms.double(0.2)
)


process.hltfilter = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring('HLT_HIPuAK4CaloJet100_Eta5p1_v*', 
        'HLT_HIPuAK4CaloJet80_Eta5p1_Cent30_100_v*'),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    throw = cms.bool(True)
)


process.inclusiveSecondaryVerticesFiltered = cms.EDFilter("BVertexFilter",
    minVertices = cms.int32(0),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("inclusiveSecondaryVertices"),
    useVertexKinematicAsJetAxis = cms.bool(True),
    vertexFilter = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.1),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    )
)


process.noBSChalo = cms.EDFilter("HLTLevel1GTSeed",
    L1CollectionsTag = cms.InputTag("l1extraParticles"),
    L1GtObjectMapTag = cms.InputTag("l1GtObjectMap"),
    L1GtReadoutRecordTag = cms.InputTag("gtDigis"),
    L1MuonCollectionTag = cms.InputTag("l1extraParticles"),
    L1NrBxInEvent = cms.int32(3),
    L1SeedsLogicalExpression = cms.string('NOT (36 OR 37 OR 38 OR 39)'),
    L1TechTriggerSeeding = cms.bool(True),
    L1UseAliasesForSeeding = cms.bool(True),
    L1UseL1TriggerObjectMaps = cms.bool(True),
    saveTags = cms.bool(False)
)


process.pileupVertexFilterCutE = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(True),
    doDzNtrkCut = cms.bool(False),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 3.0, 2.4, 2.0, 1.2, 
        1.2, 0.9, 0.6),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutEandG = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(True),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 3.0, 2.4, 2.0, 1.2, 
        1.2, 0.9, 0.6),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutG = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 3.0, 2.4, 2.0, 1.2, 
        1.2, 0.9, 0.6),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutGloose = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 4.5, 3.2, 3.0, 1.8, 
        1.8, 1.35, 0.9),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutGplus = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(0.05),
    dzCutByNtrk = cms.vdouble(999.0, 999.0, 999.0, 3.0, 2.0, 
        1.6, 1.4, 1.2, 1.1, 1.0, 
        0.9, 0.8, 0.7, 0.7, 0.6, 
        0.6, 0.5, 0.5, 0.4, 0.4, 
        0.4, 0.3, 0.3, 0.3, 0.3, 
        0.3, 0.2, 0.2, 0.2, 0.2, 
        0.0),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutGplusNV = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 999.0, 999.0, 3.0, 2.0, 
        1.6, 1.4, 1.2, 1.1, 1.0, 
        0.9, 0.8, 0.7, 0.7, 0.6, 
        0.6, 0.5, 0.5, 0.4, 0.4, 
        0.4, 0.3, 0.3, 0.3, 0.3, 
        0.3, 0.2, 0.2, 0.2, 0.2, 
        0.0),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutGplusUpsPP = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 999.0, 1.5, 1.0, 0.8, 
        0.6, 0.5, 0.4, 0.3, 0.2, 
        0.2, 0.2, 0.2, 0.2, 0.2, 
        0.2, 0.0),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutGplusplus = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(False),
    doSurfaceCut = cms.bool(True),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(0.05),
    dzCutByNtrk = cms.vdouble(999.0, 3.0, 2.4, 2.0, 1.2, 
        1.2, 0.9, 0.6),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(28.593, -1.525, 2.636788, -1.5e-05, 200.0, 
        0.0),
    surfaceFunctionString = cms.string('[0]*exp([1]*(x-([3]*(y-[4])**2+[5])))+[2]'),
    surfaceMinDzEval = cms.double(0.0),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutGtight = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(True),
    doSurfaceCut = cms.bool(False),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 2.0, 1.6, 1.333, 0.8, 
        0.8, 0.6, 0.4),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutW = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(False),
    doSurfaceCut = cms.bool(True),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(999.0),
    dzCutByNtrk = cms.vdouble(999.0, 3.0, 2.4, 2.0, 1.2, 
        1.2, 0.9, 0.6),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pileupVertexFilterCutWplus = cms.EDFilter("PAPileUpVertexFilter",
    doDxyDzCut = cms.bool(False),
    doDzNtrkCut = cms.bool(False),
    doSurfaceCut = cms.bool(True),
    dxyDzCutPar0 = cms.double(0.6),
    dxyDzCutPar1 = cms.double(13.333),
    dxyVeto = cms.double(0.05),
    dzCutByNtrk = cms.vdouble(999.0, 3.0, 2.4, 2.0, 1.2, 
        1.2, 0.9, 0.6),
    dzVeto = cms.double(-999.0),
    surfaceCutParameters = cms.vdouble(0.92473, 7.484908, 8.84978, -0.587169, 0.478601, 
        -0.000106, -0.000385, -0.09479, 0.250266, 198.662432, 
        728.42475, 2.958134),
    surfaceFunctionString = cms.string('[2]*exp(-x**2/[0])*x**[3]+[1]+([6]*exp(-x/[4])*x**[7]+[5])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])*(y-[10]*exp(-x**2/[8])*x**[11]-[9])'),
    surfaceMinDzEval = cms.double(0.2),
    vtxSrc = cms.InputTag("offlinePrimaryVertices")
)


process.primaryVertexFilter = cms.EDFilter("VertexSelector",
    cut = cms.string('!isFake && abs(z) <= 25 && position.Rho <= 2 && tracksSize >= 2'),
    filter = cms.bool(True),
    src = cms.InputTag("hiSelectedVertex")
)


process.HiForest = cms.EDAnalyzer("HiForestInfo",
    GlobalTagLabel = cms.string('75X_dataRun2_v12'),
    HiForestVersion = cms.string('CMSSW_7_5_8-417-ga5a61cc\n'),
    inputLines = cms.vstring('HiForest V3', 
        "\'JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK4PF_offline\'")
)


process.akPu2CaloJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('akPu2Calo'),
    doHiJetID = cms.untracked.bool(True),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doTower = cms.untracked.bool(True),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(15),
    genjetTag = cms.InputTag("ak2HiGenJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetTag = cms.InputTag("akPu2CalopatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlowTmp"),
    rParam = cms.double(0.2),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.akPu2PFJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('akPu2PF'),
    doHiJetID = cms.untracked.bool(True),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doTower = cms.untracked.bool(True),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(15),
    genjetTag = cms.InputTag("ak2HiGenJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetTag = cms.InputTag("akPu2PFpatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlowTmp"),
    rParam = cms.double(0.2),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.akPu3CaloJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('akPu3Calo'),
    doHiJetID = cms.untracked.bool(True),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doTower = cms.untracked.bool(True),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(15),
    genjetTag = cms.InputTag("ak3HiGenJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetTag = cms.InputTag("akPu3CalopatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlowTmp"),
    rParam = cms.double(0.3),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.akPu3PFJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('akPu3PF'),
    doHiJetID = cms.untracked.bool(True),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doTower = cms.untracked.bool(True),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(15),
    genjetTag = cms.InputTag("ak3HiGenJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetTag = cms.InputTag("akPu3PFpatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlowTmp"),
    rParam = cms.double(0.3),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.akPu4CaloJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('akPu4Calo'),
    doHiJetID = cms.untracked.bool(True),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doTower = cms.untracked.bool(True),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(15),
    genjetTag = cms.InputTag("ak4HiGenJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetTag = cms.InputTag("akPu4CalopatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlowTmp"),
    rParam = cms.double(0.4),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.akPu4PFJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('akPu4PF'),
    doHiJetID = cms.untracked.bool(True),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doTower = cms.untracked.bool(True),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(15),
    genjetTag = cms.InputTag("ak4HiGenJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetTag = cms.InputTag("akPu4PFpatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlowTmp"),
    rParam = cms.double(0.4),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.akPu5CaloJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('akPu5Calo'),
    doHiJetID = cms.untracked.bool(True),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doTower = cms.untracked.bool(True),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(15),
    genjetTag = cms.InputTag("ak5HiGenJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetTag = cms.InputTag("akPu5CalopatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlowTmp"),
    rParam = cms.double(0.5),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.akPu5PFJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('akPu5PF'),
    doHiJetID = cms.untracked.bool(True),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doTower = cms.untracked.bool(True),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(15),
    genjetTag = cms.InputTag("ak5HiGenJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetTag = cms.InputTag("akPu5PFpatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlowTmp"),
    rParam = cms.double(0.5),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.akVs2CaloJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('akVs2Calo'),
    doHiJetID = cms.untracked.bool(True),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doTower = cms.untracked.bool(True),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(15),
    genjetTag = cms.InputTag("ak2HiGenJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetTag = cms.InputTag("akVs2CalopatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlowTmp"),
    rParam = cms.double(0.2),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.akVs2PFJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('akVs2PF'),
    doHiJetID = cms.untracked.bool(True),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doTower = cms.untracked.bool(True),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(15),
    genjetTag = cms.InputTag("ak2HiGenJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetTag = cms.InputTag("akVs2PFpatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlowTmp"),
    rParam = cms.double(0.2),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.akVs3CaloJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('akVs3Calo'),
    doHiJetID = cms.untracked.bool(True),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doTower = cms.untracked.bool(True),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(15),
    genjetTag = cms.InputTag("ak3HiGenJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetTag = cms.InputTag("akVs3CalopatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlowTmp"),
    rParam = cms.double(0.3),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.akVs3PFJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('akVs3PF'),
    doHiJetID = cms.untracked.bool(True),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doTower = cms.untracked.bool(True),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(15),
    genjetTag = cms.InputTag("ak3HiGenJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetTag = cms.InputTag("akVs3PFpatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlowTmp"),
    rParam = cms.double(0.3),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.akVs4CaloJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('akVs4Calo'),
    doHiJetID = cms.untracked.bool(True),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doTower = cms.untracked.bool(True),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(15),
    genjetTag = cms.InputTag("ak4HiGenJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetTag = cms.InputTag("akVs4CalopatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlowTmp"),
    rParam = cms.double(0.4),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.akVs4PFJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('akVs4PF'),
    doHiJetID = cms.untracked.bool(True),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doTower = cms.untracked.bool(True),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(15),
    genjetTag = cms.InputTag("ak4HiGenJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetTag = cms.InputTag("akVs4PFpatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlowTmp"),
    rParam = cms.double(0.4),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.akVs5CaloJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('akVs5Calo'),
    doHiJetID = cms.untracked.bool(True),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doTower = cms.untracked.bool(True),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(15),
    genjetTag = cms.InputTag("ak5HiGenJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetTag = cms.InputTag("akVs5CalopatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlowTmp"),
    rParam = cms.double(0.5),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.akVs5PFJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    bTagJetName = cms.untracked.string('akVs5PF'),
    doHiJetID = cms.untracked.bool(True),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    doTower = cms.untracked.bool(True),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    genPtMin = cms.untracked.double(15),
    genjetTag = cms.InputTag("ak5HiGenJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HISIGNAL'),
    isMC = cms.untracked.bool(False),
    jetTag = cms.InputTag("akVs5PFpatJetsWithBtagging"),
    matchJets = cms.untracked.bool(False),
    matchTag = cms.untracked.InputTag("patJetsWithBtagging"),
    pfCandidateLabel = cms.untracked.InputTag("particleFlowTmp"),
    rParam = cms.double(0.5),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.anaTrack = cms.EDAnalyzer("TrackAnalyzer",
    associatorMap = cms.InputTag("tpRecoAssocHiGeneralTracks"),
    beamSpotSrc = cms.untracked.InputTag("offlineBeamSpot"),
    doMVA = cms.untracked.bool(True),
    doPFMatching = cms.untracked.bool(True),
    doSimTrack = cms.untracked.bool(False),
    doSimVertex = cms.untracked.bool(False),
    fillSimTrack = cms.untracked.bool(False),
    mvaSrc = cms.InputTag("hiGeneralTracks","MVAVals"),
    particleSrc = cms.InputTag("genParticles"),
    pfCandSrc = cms.InputTag("particleFlowTmp"),
    qualityString = cms.untracked.string('highPurity'),
    qualityStrings = cms.untracked.vstring('highPurity', 
        'tight', 
        'loose'),
    simTrackPtMin = cms.untracked.double(0.4),
    tpEffSrc = cms.untracked.InputTag("mix","MergedTrackTruth"),
    tpFakeSrc = cms.untracked.InputTag("mix","MergedTrackTruth"),
    trackPtMin = cms.untracked.double(0.49),
    trackSrc = cms.InputTag("hiGeneralTracks"),
    useQuality = cms.untracked.bool(False),
    vertexSrc = cms.vstring('hiSelectedVertex')
)


process.ggHiNtuplizer = cms.EDAnalyzer("ggHiNtuplizer",
    VtxLabel = cms.InputTag("offlinePrimaryVertices"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversions = cms.InputTag("allConversions"),
    doElectronVID = cms.bool(False),
    doGenParticles = cms.bool(False),
    doPfIso = cms.bool(True),
    doVsIso = cms.bool(True),
    effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
    electronLooseID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-loose"),
    electronMediumID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-medium"),
    electronTightID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-tight"),
    electronVetoID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-veto"),
    genParticleSrc = cms.InputTag("genParticles"),
    gsfElectronLabel = cms.InputTag("gedGsfElectronsTmp"),
    particleFlowCollection = cms.InputTag("particleFlowTmp"),
    pileupCollection = cms.InputTag("addPileupInfo"),
    recoMuonSrc = cms.InputTag("muons"),
    recoPhotonHiIsolationMap = cms.InputTag("photonIsolationHIProducer"),
    recoPhotonSrc = cms.InputTag("photons"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    runOnParticleGun = cms.bool(False),
    useValMapIso = cms.bool(True),
    voronoiBackgroundCalo = cms.InputTag("voronoiBackgroundCalo"),
    voronoiBackgroundPF = cms.InputTag("voronoiBackgroundPF")
)


process.ggHiNtuplizerGED = cms.EDAnalyzer("ggHiNtuplizer",
    VtxLabel = cms.InputTag("offlinePrimaryVertices"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversions = cms.InputTag("allConversions"),
    doElectronVID = cms.bool(False),
    doGenParticles = cms.bool(False),
    doPfIso = cms.bool(True),
    doVsIso = cms.bool(True),
    effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
    electronLooseID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-loose"),
    electronMediumID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-medium"),
    electronTightID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-tight"),
    electronVetoID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-veto"),
    genParticleSrc = cms.InputTag("genParticles"),
    gsfElectronLabel = cms.InputTag("gedGsfElectronsTmp"),
    particleFlowCollection = cms.InputTag("particleFlowTmp"),
    pileupCollection = cms.InputTag("addPileupInfo"),
    recoMuonSrc = cms.InputTag("muons"),
    recoPhotonHiIsolationMap = cms.InputTag("photonIsolationHIProducerGED"),
    recoPhotonSrc = cms.InputTag("gedPhotonsTmp"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    runOnParticleGun = cms.bool(False),
    useValMapIso = cms.bool(True),
    voronoiBackgroundCalo = cms.InputTag("voronoiBackgroundCalo"),
    voronoiBackgroundPF = cms.InputTag("voronoiBackgroundPF")
)


process.hcalNoise = cms.EDAnalyzer("HiHcalAnalyzer",
    NoiseRBXTag = cms.untracked.InputTag("hcalnoise"),
    NoiseSummaryTag = cms.untracked.InputTag("hcalnoise")
)


process.hiEvtAnalyzer = cms.EDAnalyzer("HiEvtAnalyzer",
    CentralityBinSrc = cms.InputTag("centralityBin","HFtowers"),
    CentralitySrc = cms.InputTag("hiCentrality"),
    EvtPlane = cms.InputTag("hiEvtPlane"),
    EvtPlaneFlat = cms.InputTag("hiEvtPlaneFlat"),
    HiMC = cms.InputTag("heavyIon"),
    Vertex = cms.InputTag("hiSelectedVertex"),
    doCentrality = cms.bool(True),
    doEvtPlane = cms.bool(True),
    doEvtPlaneFlat = cms.bool(False),
    doHiMC = cms.bool(False),
    doMC = cms.bool(False),
    doVertex = cms.bool(True),
    evtPlaneLevel = cms.int32(0),
    useHepMC = cms.bool(False)
)


process.hltanalysis = cms.EDAnalyzer("HLTBitAnalyzer",
    HLTProcessName = cms.string('HLT'),
    RunParameters = cms.PSet(
        HistogramFile = cms.untracked.string('hltbitanalysis.root')
    ),
    UseTFileService = cms.untracked.bool(True),
    dummyBranches = cms.untracked.vstring( ('HLT_HIPuAK4CaloJet40_Eta5p1_v1', 
        'HLT_HIPuAK4CaloJet40_Eta5p1_v2', 
        'HLT_HIPuAK4CaloJet60_Eta5p1_v1', 
        'HLT_HIPuAK4CaloJet80_Eta5p1_v1', 
        'HLT_HIPuAK4CaloJet80_Eta5p1ForZS_v1', 
        'HLT_HIPuAK4CaloJet100_Eta5p1_v1', 
        'HLT_HIPuAK4CaloJet110_Eta5p1_v1', 
        'HLT_HIPuAK4CaloJet120_Eta5p1_v1', 
        'HLT_HIPuAK4CaloJet150_Eta5p1_v1', 
        'HLT_HIPuAK4CaloJet40_Eta5p1_Cent30_100_v1', 
        'HLT_HIPuAK4CaloJet60_Eta5p1_Cent30_100_v1', 
        'HLT_HIPuAK4CaloJet80_Eta5p1_Cent30_100_v1', 
        'HLT_HIPuAK4CaloJet100_Eta5p1_Cent30_100_v1', 
        'HLT_HIPuAK4CaloJet40_Eta5p1_Cent50_100_v1', 
        'HLT_HIPuAK4CaloJet60_Eta5p1_Cent50_100_v1', 
        'HLT_HIPuAK4CaloJet80_Eta5p1_Cent50_100_v1', 
        'HLT_HIPuAK4CaloJet100_Eta5p1_Cent50_100_v1', 
        'HLT_HIPuAK4CaloJet80_Jet35_Eta1p1_v1', 
        'HLT_HIPuAK4CaloJet80_Jet35_Eta0p7_v1', 
        'HLT_HIPuAK4CaloJet100_Jet35_Eta1p1_v1', 
        'HLT_HIPuAK4CaloJet100_Jet35_Eta0p7_v1', 
        'HLT_HIPuAK4CaloJet80_45_45_Eta2p1_v1', 
        'HLT_HIPuAK4CaloDJet60_Eta2p1_v1', 
        'HLT_HIPuAK4CaloDJet80_Eta2p1_v1', 
        'HLT_HIPuAK4CaloBJetCSV60_Eta2p1_v1', 
        'HLT_HIPuAK4CaloBJetCSV80_Eta2p1_v1', 
        'HLT_HIPuAK4CaloBJetSSV60_Eta2p1_v1', 
        'HLT_HIPuAK4CaloBJetSSV80_Eta2p1_v1', 
        'HLT_HIDmesonHITrackingGlobal_Dpt20_v1', 
        'HLT_HIDmesonHITrackingGlobal_Dpt20_v2', 
        'HLT_HIDmesonHITrackingGlobal_Dpt20_Cent0_10_v1', 
        'HLT_HIDmesonHITrackingGlobal_Dpt20_Cent0_10_v2', 
        'HLT_HIDmesonHITrackingGlobal_Dpt20_Cent30_100_v1', 
        'HLT_HIDmesonHITrackingGlobal_Dpt20_Cent30_100_v2', 
        'HLT_HIDmesonHITrackingGlobal_Dpt20_Cent30_100_v3', 
        'HLT_HIDmesonHITrackingGlobal_Dpt20_Cent50_100_v1', 
        'HLT_HIDmesonHITrackingGlobal_Dpt20_Cent50_100_v2', 
        'HLT_HIDmesonHITrackingGlobal_Dpt20_Cent50_100_v3', 
        'HLT_HIDmesonHITrackingGlobal_Dpt30_v1', 
        'HLT_HIDmesonHITrackingGlobal_Dpt30_Cent0_10_v1', 
        'HLT_HIDmesonHITrackingGlobal_Dpt30_Cent0_10_v2', 
        'HLT_HIDmesonHITrackingGlobal_Dpt30_Cent30_100_v1', 
        'HLT_HIDmesonHITrackingGlobal_Dpt30_Cent50_100_v1', 
        'HLT_HIDmesonHITrackingGlobal_Dpt40_v1', 
        'HLT_HIDmesonHITrackingGlobal_Dpt40_Cent0_10_v1', 
        'HLT_HIDmesonHITrackingGlobal_Dpt40_Cent0_10_v2', 
        'HLT_HIDmesonHITrackingGlobal_Dpt40_Cent30_100_v1', 
        'HLT_HIDmesonHITrackingGlobal_Dpt40_Cent50_100_v1', 
        'HLT_HIDmesonHITrackingGlobal_Dpt50_v1', 
        'HLT_HIDmesonHITrackingGlobal_Dpt60_v1', 
        'HLT_HIDmesonHITrackingGlobal_Dpt70_v1', 
        'HLT_HIDmesonHITrackingGlobal_Dpt60_Cent30_100_v1', 
        'HLT_HIDmesonHITrackingGlobal_Dpt60_Cent50_100_v1', 
        'HLT_HISinglePhoton10_Eta1p5_v1', 
        'HLT_HISinglePhoton10_Eta1p5_v2', 
        'HLT_HISinglePhoton15_Eta1p5_v1', 
        'HLT_HISinglePhoton15_Eta1p5_v2', 
        'HLT_HISinglePhoton20_Eta1p5_v1', 
        'HLT_HISinglePhoton20_Eta1p5_v2', 
        'HLT_HISinglePhoton30_Eta1p5_v1', 
        'HLT_HISinglePhoton40_Eta1p5_v1', 
        'HLT_HISinglePhoton50_Eta1p5_v1', 
        'HLT_HISinglePhoton60_Eta1p5_v1', 
        'HLT_HISinglePhoton10_Eta1p5_Cent50_100_v1', 
        'HLT_HISinglePhoton15_Eta1p5_Cent50_100_v1', 
        'HLT_HISinglePhoton20_Eta1p5_Cent50_100_v1', 
        'HLT_HISinglePhoton30_Eta1p5_Cent50_100_v1', 
        'HLT_HISinglePhoton40_Eta1p5_Cent50_100_v1', 
        'HLT_HISinglePhoton10_Eta1p5_Cent30_100_v1', 
        'HLT_HISinglePhoton15_Eta1p5_Cent30_100_v1', 
        'HLT_HISinglePhoton20_Eta1p5_Cent30_100_v1', 
        'HLT_HISinglePhoton30_Eta1p5_Cent30_100_v1', 
        'HLT_HISinglePhoton40_Eta1p5_Cent30_100_v1', 
        'HLT_HISinglePhoton40_Eta2p1_v1', 
        'HLT_HISinglePhoton10_Eta3p1_v1', 
        'HLT_HISinglePhoton10_Eta3p1_v2', 
        'HLT_HISinglePhoton15_Eta3p1_v1', 
        'HLT_HISinglePhoton15_Eta3p1_v2', 
        'HLT_HISinglePhoton20_Eta3p1_v1', 
        'HLT_HISinglePhoton20_Eta3p1_v2', 
        'HLT_HISinglePhoton30_Eta3p1_v1', 
        'HLT_HISinglePhoton40_Eta3p1_v1', 
        'HLT_HISinglePhoton50_Eta3p1_v1', 
        'HLT_HISinglePhoton60_Eta3p1_v1', 
        'HLT_HISinglePhoton10_Eta3p1_Cent50_100_v1', 
        'HLT_HISinglePhoton15_Eta3p1_Cent50_100_v1', 
        'HLT_HISinglePhoton20_Eta3p1_Cent50_100_v1', 
        'HLT_HISinglePhoton30_Eta3p1_Cent50_100_v1', 
        'HLT_HISinglePhoton40_Eta3p1_Cent50_100_v1', 
        'HLT_HISinglePhoton10_Eta3p1_Cent30_100_v1', 
        'HLT_HISinglePhoton15_Eta3p1_Cent30_100_v1', 
        'HLT_HISinglePhoton20_Eta3p1_Cent30_100_v1', 
        'HLT_HISinglePhoton30_Eta3p1_Cent30_100_v1', 
        'HLT_HISinglePhoton40_Eta3p1_Cent30_100_v1', 
        'HLT_HIDoublePhoton15_Eta1p5_Mass50_1000_v1', 
        'HLT_HIDoublePhoton15_Eta1p5_Mass50_1000_R9HECut_v1', 
        'HLT_HIDoublePhoton15_Eta2p1_Mass50_1000_R9Cut_v1', 
        'HLT_HIDoublePhoton15_Eta2p5_Mass50_1000_R9SigmaHECut_v1', 
        'HLT_HIL2Mu3Eta2p5_PuAK4CaloJet40Eta2p1_v1', 
        'HLT_HIL2Mu3Eta2p5_PuAK4CaloJet60Eta2p1_v1', 
        'HLT_HIL2Mu3Eta2p5_PuAK4CaloJet60Eta2p1_v2', 
        'HLT_HIL2Mu3Eta2p5_PuAK4CaloJet80Eta2p1_v1', 
        'HLT_HIL2Mu3Eta2p5_PuAK4CaloJet100Eta2p1_v1', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton10Eta1p5_v1', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton15Eta1p5_v1', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton20Eta1p5_v1', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton30Eta1p5_v1', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton40Eta1p5_v1', 
        'HLT_HIUCC100_v1', 
        'HLT_HIUCC100_v2', 
        'HLT_HIUCC100_v3', 
        'HLT_HIUCC020_v1', 
        'HLT_HIUCC020_v2', 
        'HLT_HIUCC020_v3', 
        'HLT_HIQ2Bottom005_Centrality1030_v1', 
        'HLT_HIQ2Bottom005_Centrality1030_v2', 
        'HLT_HIQ2Bottom005_Centrality1030_v3', 
        'HLT_HIQ2Top005_Centrality1030_v1', 
        'HLT_HIQ2Top005_Centrality1030_v2', 
        'HLT_HIQ2Top005_Centrality1030_v3', 
        'HLT_HIQ2Bottom005_Centrality3050_v1', 
        'HLT_HIQ2Bottom005_Centrality3050_v2', 
        'HLT_HIQ2Bottom005_Centrality3050_v3', 
        'HLT_HIQ2Top005_Centrality3050_v1', 
        'HLT_HIQ2Top005_Centrality3050_v2', 
        'HLT_HIQ2Top005_Centrality3050_v3', 
        'HLT_HIQ2Bottom005_Centrality5070_v1', 
        'HLT_HIQ2Bottom005_Centrality5070_v2', 
        'HLT_HIQ2Bottom005_Centrality5070_v3', 
        'HLT_HIQ2Top005_Centrality5070_v1', 
        'HLT_HIQ2Top005_Centrality5070_v2', 
        'HLT_HIQ2Top005_Centrality5070_v3', 
        'HLT_HIFullTrack12_L1MinimumBiasHF2_AND_v1', 
        'HLT_HIFullTrack12_L1Centrality010_v1', 
        'HLT_HIFullTrack12_L1Centrality010_v2', 
        'HLT_HIFullTrack12_L1Centrality30100_v1', 
        'HLT_HIFullTrack18_L1MinimumBiasHF2_AND_v1', 
        'HLT_HIFullTrack18_L1Centrality010_v1', 
        'HLT_HIFullTrack18_L1Centrality010_v2', 
        'HLT_HIFullTrack18_L1Centrality30100_v1', 
        'HLT_HIFullTrack24_v1', 
        'HLT_HIFullTrack24_L1Centrality30100_v1', 
        'HLT_HIFullTrack34_v1', 
        'HLT_HIFullTrack34_L1Centrality30100_v1', 
        'HLT_HIFullTrack45_v1', 
        'HLT_HIFullTrack45_L1Centrality30100_v1', 
        'HLT_HIL1DoubleMu0_v1', 
        'HLT_HIL1DoubleMu0_part1_v1', 
        'HLT_HIL1DoubleMu0_part2_v1', 
        'HLT_HIL1DoubleMu0_part3_v1', 
        'HLT_HIL1DoubleMu0_2HF_v1', 
        'HLT_HIL1DoubleMu0_2HF0_v1', 
        'HLT_HIL1DoubleMu10_v1', 
        'HLT_HIL2DoubleMu0_NHitQ_v1', 
        'HLT_HIL2DoubleMu0_NHitQ_v2', 
        'HLT_HIL2DoubleMu0_NHitQ_2HF_v1', 
        'HLT_HIL2DoubleMu0_NHitQ_2HF0_v1', 
        'HLT_HIL2Mu3_NHitQ10_2HF_v1', 
        'HLT_HIL2Mu3_NHitQ10_2HF0_v1', 
        'HLT_HIL3Mu3_NHitQ15_2HF_v1', 
        'HLT_HIL3Mu3_NHitQ15_2HF0_v1', 
        'HLT_HIL2Mu5_NHitQ10_2HF_v1', 
        'HLT_HIL2Mu5_NHitQ10_2HF0_v1', 
        'HLT_HIL3Mu5_NHitQ15_2HF_v1', 
        'HLT_HIL3Mu5_NHitQ15_2HF0_v1', 
        'HLT_HIL2Mu7_NHitQ10_2HF_v1', 
        'HLT_HIL2Mu7_NHitQ10_2HF0_v1', 
        'HLT_HIL3Mu7_NHitQ15_2HF_v1', 
        'HLT_HIL3Mu7_NHitQ15_2HF0_v1', 
        'HLT_HIL2Mu15_v1', 
        'HLT_HIL2Mu15_v2', 
        'HLT_HIL2Mu15_2HF_v1', 
        'HLT_HIL2Mu15_2HF0_v1', 
        'HLT_HIL3Mu15_v1', 
        'HLT_HIL3Mu15_2HF_v1', 
        'HLT_HIL3Mu15_2HF0_v1', 
        'HLT_HIL2Mu20_v1', 
        'HLT_HIL2Mu20_2HF_v1', 
        'HLT_HIL2Mu20_2HF0_v1', 
        'HLT_HIL3Mu20_v1', 
        'HLT_HIL3Mu20_2HF_v1', 
        'HLT_HIL3Mu20_2HF0_v1', 
        'HLT_HIL1DoubleMu0_2HF_Cent30100_v1', 
        'HLT_HIL1DoubleMu0_2HF0_Cent30100_v1', 
        'HLT_HIL2DoubleMu0_2HF_Cent30100_NHitQ_v1', 
        'HLT_HIL1DoubleMu0_Cent30_v1', 
        'HLT_HIL2DoubleMu0_2HF0_Cent30100_NHitQ_v1', 
        'HLT_HIL2DoubleMu0_Cent30_OS_NHitQ_v1', 
        'HLT_HIL2DoubleMu0_Cent30_NHitQ_v1', 
        'HLT_HIL3DoubleMu0_Cent30_v1', 
        'HLT_HIL3DoubleMu0_Cent30_OS_m2p5to4p5_v1', 
        'HLT_HIL3DoubleMu0_Cent30_OS_m7to14_v1', 
        'HLT_HIL3DoubleMu0_OS_m2p5to4p5_v1', 
        'HLT_HIL3DoubleMu0_OS_m7to14_v1', 
        'HLT_HIUPCL1SingleMuOpenNotHF2_v1', 
        'HLT_HIUPCSingleMuNotHF2Pixel_SingleTrack_v1', 
        'HLT_HIUPCL1DoubleMuOpenNotHF2_v1', 
        'HLT_HIUPCDoubleMuNotHF2Pixel_SingleTrack_v1', 
        'HLT_HIUPCL1SingleEG2NotHF2_v1', 
        'HLT_HIUPCSingleEG2NotHF2Pixel_SingleTrack_v1', 
        'HLT_HIUPCL1DoubleEG2NotHF2_v1', 
        'HLT_HIUPCDoubleEG2NotHF2Pixel_SingleTrack_v1', 
        'HLT_HIUPCL1SingleEG5NotHF2_v1', 
        'HLT_HIUPCSingleEG5NotHF2Pixel_SingleTrack_v1', 
        'HLT_HIUPCL1DoubleMuOpenNotHF1_v1', 
        'HLT_HIUPCDoubleMuNotHF1Pixel_SingleTrack_v1', 
        'HLT_HIUPCL1DoubleEG2NotZDCAND_v1', 
        'HLT_HIUPCL1DoubleEG2NotZDCANDPixel_SingleTrack_v1', 
        'HLT_HIUPCL1DoubleMuOpenNotZDCAND_v1', 
        'HLT_HIUPCL1DoubleMuOpenNotZDCANDPixel_SingleTrack_v1', 
        'HLT_HIUPCL1EG2NotZDCAND_v1', 
        'HLT_HIUPCEG2NotZDCANDPixel_SingleTrack_v1', 
        'HLT_HIUPCL1MuOpenNotZDCAND_v1', 
        'HLT_HIUPCL1MuOpenNotZDCANDPixel_SingleTrack_v1', 
        'HLT_HIUPCL1NotHFplusANDminusTH0BptxAND_v1', 
        'HLT_HIUPCL1NotHFplusANDminusTH0BptxANDPixel_SingleTrack_v1', 
        'HLT_HIUPCL1NotHFMinimumbiasHFplusANDminustTH0_v1', 
        'HLT_HIUPCL1NotHFMinimumbiasHFplusANDminustTH0Pixel_SingleTrack_v1', 
        'HLT_HIUPCL1DoubleMuOpenNotHFMinimumbiasHFplusANDminustTH0_v1', 
        'HLT_HIUPCL1DoubleMuOpenNotHFMinimumbiasHFplusANDminustTH0Pixel_SingleTrack_v1', 
        'HLT_HIL1CastorMediumJet_v1', 
        'HLT_HIL1CastorMediumJetAK4CaloJet20_v1', 
        'HLT_HICastorMediumJetPixel_SingleTrack_v1', 
        'HLT_HICastorMediumJetPixel_SingleTrack_v2', 
        'HLT_HIUPCL1NotMinimumBiasHF2_AND_v1', 
        'HLT_HIUPCL1NotMinimumBiasHF2_ANDPixel_SingleTrack_v1', 
        'HLT_HIUPCL1ZdcOR_BptxAND_v1', 
        'HLT_HIUPCL1ZdcOR_BptxANDPixel_SingleTrack_v1', 
        'HLT_HIUPCL1ZdcXOR_BptxAND_v1', 
        'HLT_HIUPCL1ZdcXOR_BptxANDPixel_SingleTrack_v1', 
        'HLT_HIUPCL1NotZdcOR_BptxAND_v1', 
        'HLT_HIUPCL1NotZdcOR_BptxANDPixel_SingleTrack_v1', 
        'HLT_HIZeroBias_v1', 
        'HLT_HICentralityVeto_v1', 
        'HLT_HICentralityVeto_v2', 
        'HLT_HIL1Tech5_BPTX_PlusOnly_v1', 
        'HLT_HIL1Tech6_BPTX_MinusOnly_v1', 
        'HLT_HIL1Tech7_NoBPTX_v1', 
        'HLT_HIL1MinimumBiasHF1OR_v1', 
        'HLT_HIL1MinimumBiasHF2OR_v1', 
        'HLT_HIL1MinimumBiasHF1AND_v1', 
        'HLT_HIL1MinimumBiasHF1ANDExpress_v1', 
        'HLT_HIL1MinimumBiasHF2AND_part1_v1', 
        'HLT_HIL1MinimumBiasHF2AND_part2_v1', 
        'HLT_HIL1MinimumBiasHF2AND_part3_v1', 
        'HLT_HIL1MinimumBiasHF2AND_part4_v1', 
        'HLT_HIL1MinimumBiasHF2AND_part5_v1', 
        'HLT_HIL1MinimumBiasHF2AND_part6_v1', 
        'HLT_HIL1MinimumBiasHF2AND_part7_v1', 
        'HLT_HIL1MinimumBiasHF2AND_part8_v1', 
        'HLT_HIL1MinimumBiasHF2AND_part9_v1', 
        'HLT_HIL1MinimumBiasHF2AND_part10_v1', 
        'HLT_HIL1MinimumBiasHF2AND_part11_v1', 
        'HLT_HIL1MinimumBiasHF2ANDExpress_v1', 
        'HLT_HIL1HFplusANDminusTH0Express_v1', 
        'HLT_HIL1MinimumBiasHF1ANDPixel_SingleTrack_v1', 
        'HLT_HIL1MinimumBiasHF2ANDPixel_SingleTrack_v1', 
        'HLT_HIZeroBiasPixel_SingleTrack_v1', 
        'HLT_HIL1Centralityext30100MinimumumBiasHF1AND_v1', 
        'HLT_HIL1Centralityext30100MinimumumBiasHF2AND_part1_v1', 
        'HLT_HIL1Centralityext30100MinimumumBiasHF2AND_part2_v1', 
        'HLT_HIL1Centralityext30100MinimumumBiasHF2AND_part3_v1', 
        'HLT_HIL1Centralityext50100MinimumumBiasHF1AND_v1', 
        'HLT_HIL1Centralityext50100MinimumumBiasHF2AND_v1', 
        'HLT_HIL1Centralityext70100MinimumumBiasHF1AND_v1', 
        'HLT_HIL1Centralityext010MinimumumBiasHF1ANDForZS_v1', 
        'HLT_HIPhysics_v1', 
        'HLT_HIPhysicsForZS_v1', 
        'HLT_HIRandom_v1', 
        'HLT_EcalCalibration_v1', 
        'HLT_HcalCalibration_v1', 
        'HLT_HIPhysicsNoZS_v1', 
        'HLT_HIL1MinimumBiasHF2AND_v1', 
        'HLT_HIL1Centralityext30100MinimumumBiasHF2AND_v1', 
        'HLT_HIL1Centralityext30100HFplusANDminusTH0_v1', 
        'HLT_HIL1Centralityext50100HFplusANDminusTH0_v1', 
        'HLT_HIL1Centralityext70100HFplusANDminusTH0_v1' ) ),
    hltresults = cms.InputTag("TriggerResults","","HLT"),
    l1GctHFBitCounts = cms.InputTag("gctDigis"),
    l1GctHFRingSums = cms.InputTag("gctDigis"),
    l1GtObjectMapRecord = cms.InputTag("hltL1GtObjectMap","","HLT"),
    l1GtReadoutRecord = cms.InputTag("gtDigis"),
    l1extramc = cms.string('l1extraParticles'),
    l1extramu = cms.string('l1extraParticles')
)


process.hltbitanalysis = cms.EDAnalyzer("HLTBitAnalyzer",
    HLTProcessName = cms.string('HLT'),
    RunParameters = cms.PSet(
        HistogramFile = cms.untracked.string('hltbitanalysis.root')
    ),
    UseTFileService = cms.untracked.bool(True),
    hltresults = cms.InputTag("TriggerResults","","HLT"),
    l1GctHFBitCounts = cms.InputTag("hltGctDigis"),
    l1GctHFRingSums = cms.InputTag("hltGctDigis"),
    l1GtObjectMapRecord = cms.InputTag("hltL1GtObjectMap","","HLT"),
    l1GtReadoutRecord = cms.InputTag("hltGtDigis","","HLT"),
    l1extramc = cms.string('hltL1extraParticles'),
    l1extramu = cms.string('hltL1extraParticles')
)


process.hltobject = cms.EDAnalyzer("TriggerObjectAnalyzer",
    processName = cms.string('HLT'),
    treeName = cms.string('JetTriggers'),
    triggerEvent = cms.InputTag("hltTriggerSummaryAOD","","HLT"),
    triggerNames = cms.vstring('HLT_HIDmesonHITrackingGlobal_Dpt20_Cent30_100_v', 
        'HLT_HIDmesonHITrackingGlobal_Dpt20_Cent50_100_v', 
        'HLT_HIDmesonHITrackingGlobal_Dpt20_v', 
        'HLT_HIDmesonHITrackingGlobal_Dpt30_Cent30_100_v', 
        'HLT_HIDmesonHITrackingGlobal_Dpt30_Cent50_100_v', 
        'HLT_HIDmesonHITrackingGlobal_Dpt30_v', 
        'HLT_HIDmesonHITrackingGlobal_Dpt40_Cent30_100_v', 
        'HLT_HIDmesonHITrackingGlobal_Dpt40_Cent50_100_v', 
        'HLT_HIDmesonHITrackingGlobal_Dpt40_v', 
        'HLT_HIDmesonHITrackingGlobal_Dpt50_v', 
        'HLT_HIDmesonHITrackingGlobal_Dpt60_Cent30_100_v', 
        'HLT_HIDmesonHITrackingGlobal_Dpt60_Cent50_100_v', 
        'HLT_HIDmesonHITrackingGlobal_Dpt60_v', 
        'HLT_HIDmesonHITrackingGlobal_Dpt70_v', 
        'HLT_HIDoublePhoton15_Eta1p5_Mass50_1000_R9HECut_v', 
        'HLT_HIDoublePhoton15_Eta1p5_Mass50_1000_v', 
        'HLT_HIDoublePhoton15_Eta2p1_Mass50_1000_R9Cut_v', 
        'HLT_HIDoublePhoton15_Eta2p5_Mass50_1000_R9SigmaHECut_v', 
        'HLT_HIFullTrack12_L1Centrality010_v', 
        'HLT_HIFullTrack12_L1Centrality30100_v', 
        'HLT_HIFullTrack12_L1MinimumBiasHF1_AND_v', 
        'HLT_HIFullTrack18_L1Centrality010_v', 
        'HLT_HIFullTrack18_L1Centrality30100_v', 
        'HLT_HIFullTrack18_L1MinimumBiasHF1_AND_v', 
        'HLT_HIFullTrack24_L1Centrality30100_v', 
        'HLT_HIFullTrack24_v', 
        'HLT_HIFullTrack34_L1Centrality30100_v', 
        'HLT_HIFullTrack34_v', 
        'HLT_HIFullTrack45_L1Centrality30100_v', 
        'HLT_HIFullTrack45_v', 
        'HLT_HIL1CastorMediumJetAK4CaloJet20_v', 
        'HLT_HIL1CastorMediumJet_v', 
        'HLT_HIL1Centralityext30100HFplusANDminusTH0_v', 
        'HLT_HIL1Centralityext50100HFplusANDminusTH0_v', 
        'HLT_HIL1Centralityext70100HFplusANDminusTH0_v', 
        'HLT_HIL1DoubleMu0_2HF0_Cent30100_v', 
        'HLT_HIL1DoubleMu0_2HF0_v', 
        'HLT_HIL1DoubleMu0_2HF_Cent30100_v', 
        'HLT_HIL1DoubleMu0_2HF_v', 
        'HLT_HIL1DoubleMu0_Cent30_v', 
        'HLT_HIL1DoubleMu0_v', 
        'HLT_HIL1DoubleMu10_v', 
        'HLT_HIL2DoubleMu0_2HF0_Cent30100_NHitQ_v', 
        'HLT_HIL2DoubleMu0_2HF_Cent30100_NHitQ_v', 
        'HLT_HIL2DoubleMu0_Cent30_NHitQ_v', 
        'HLT_HIL2DoubleMu0_Cent30_OS_NHitQ_v', 
        'HLT_HIL2DoubleMu0_NHitQ_2HF0_v', 
        'HLT_HIL2DoubleMu0_NHitQ_2HF_v', 
        'HLT_HIL2DoubleMu0_NHitQ_v', 
        'HLT_HIL2Mu15_2HF0_v', 
        'HLT_HIL2Mu15_2HF_v', 
        'HLT_HIL2Mu15_v', 
        'HLT_HIL2Mu20_2HF0_v', 
        'HLT_HIL2Mu20_2HF_v', 
        'HLT_HIL2Mu20_v', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton10Eta1p5_v', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton15Eta1p5_v', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton20Eta1p5_v', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton30Eta1p5_v', 
        'HLT_HIL2Mu3Eta2p5_HIPhoton40Eta1p5_v', 
        'HLT_HIL2Mu3Eta2p5_PuAK4CaloJet100Eta2p1_v', 
        'HLT_HIL2Mu3Eta2p5_PuAK4CaloJet40Eta2p1_v', 
        'HLT_HIL2Mu3Eta2p5_PuAK4CaloJet60Eta2p1_v', 
        'HLT_HIL2Mu3Eta2p5_PuAK4CaloJet80Eta2p1_v', 
        'HLT_HIL2Mu3_NHitQ10_2HF0_v', 
        'HLT_HIL2Mu3_NHitQ10_2HF_v', 
        'HLT_HIL2Mu5_NHitQ10_2HF0_v', 
        'HLT_HIL2Mu5_NHitQ10_2HF_v', 
        'HLT_HIL2Mu7_NHitQ10_2HF0_v', 
        'HLT_HIL2Mu7_NHitQ10_2HF_v', 
        'HLT_HIL3DoubleMu0_Cent30_OS_m2p5to4p5_v', 
        'HLT_HIL3DoubleMu0_Cent30_OS_m7to14_v', 
        'HLT_HIL3DoubleMu0_Cent30_v', 
        'HLT_HIL3DoubleMu0_OS_m2p5to4p5_v', 
        'HLT_HIL3DoubleMu0_OS_m7to14_v', 
        'HLT_HIL3Mu15_2HF0_v', 
        'HLT_HIL3Mu15_2HF_v', 
        'HLT_HIL3Mu15_v', 
        'HLT_HIL3Mu20_2HF0_v', 
        'HLT_HIL3Mu20_2HF_v', 
        'HLT_HIL3Mu20_v', 
        'HLT_HIL3Mu3_NHitQ15_2HF0_v', 
        'HLT_HIL3Mu3_NHitQ15_2HF_v', 
        'HLT_HIL3Mu5_NHitQ15_2HF0_v', 
        'HLT_HIL3Mu5_NHitQ15_2HF_v', 
        'HLT_HIL3Mu7_NHitQ15_2HF0_v', 
        'HLT_HIL3Mu7_NHitQ15_2HF_v', 
        'HLT_HIPuAK4CaloBJetCSV60_Eta2p1_v', 
        'HLT_HIPuAK4CaloBJetCSV80_Eta2p1_v', 
        'HLT_HIPuAK4CaloBJetSSV60_Eta2p1_v', 
        'HLT_HIPuAK4CaloBJetSSV80_Eta2p1_v', 
        'HLT_HIPuAK4CaloDJet60_Eta2p1_v', 
        'HLT_HIPuAK4CaloDJet80_Eta2p1_v', 
        'HLT_HIPuAK4CaloJet100_Eta5p1_Cent30_100_v', 
        'HLT_HIPuAK4CaloJet100_Eta5p1_Cent50_100_v', 
        'HLT_HIPuAK4CaloJet100_Eta5p1_v', 
        'HLT_HIPuAK4CaloJet100_Jet35_Eta0p7_v', 
        'HLT_HIPuAK4CaloJet100_Jet35_Eta1p1_v', 
        'HLT_HIPuAK4CaloJet110_Eta5p1_v', 
        'HLT_HIPuAK4CaloJet120_Eta5p1_v', 
        'HLT_HIPuAK4CaloJet150_Eta5p1_v', 
        'HLT_HIPuAK4CaloJet40_Eta5p1_Cent30_100_v', 
        'HLT_HIPuAK4CaloJet40_Eta5p1_Cent50_100_v', 
        'HLT_HIPuAK4CaloJet40_Eta5p1_v', 
        'HLT_HIPuAK4CaloJet60_Eta5p1_Cent30_100_v', 
        'HLT_HIPuAK4CaloJet60_Eta5p1_Cent50_100_v', 
        'HLT_HIPuAK4CaloJet60_Eta5p1_v', 
        'HLT_HIPuAK4CaloJet80_45_45_Eta2p1_v', 
        'HLT_HIPuAK4CaloJet80_Eta5p1_Cent30_100_v', 
        'HLT_HIPuAK4CaloJet80_Eta5p1_Cent50_100_v', 
        'HLT_HIPuAK4CaloJet80_Eta5p1_v', 
        'HLT_HIPuAK4CaloJet80_Jet35_Eta0p7_v', 
        'HLT_HIPuAK4CaloJet80_Jet35_Eta1p1_v', 
        'HLT_HISinglePhoton10_Eta1p5_Cent30_100_v', 
        'HLT_HISinglePhoton10_Eta1p5_Cent50_100_v', 
        'HLT_HISinglePhoton10_Eta1p5_v', 
        'HLT_HISinglePhoton10_Eta3p1_Cent30_100_v', 
        'HLT_HISinglePhoton10_Eta3p1_Cent50_100_v', 
        'HLT_HISinglePhoton10_Eta3p1_v', 
        'HLT_HISinglePhoton15_Eta1p5_Cent30_100_v', 
        'HLT_HISinglePhoton15_Eta1p5_Cent50_100_v', 
        'HLT_HISinglePhoton15_Eta1p5_v', 
        'HLT_HISinglePhoton15_Eta3p1_Cent30_100_v', 
        'HLT_HISinglePhoton15_Eta3p1_Cent50_100_v', 
        'HLT_HISinglePhoton15_Eta3p1_v', 
        'HLT_HISinglePhoton20_Eta1p5_Cent30_100_v', 
        'HLT_HISinglePhoton20_Eta1p5_Cent50_100_v', 
        'HLT_HISinglePhoton20_Eta1p5_v', 
        'HLT_HISinglePhoton20_Eta3p1_Cent30_100_v', 
        'HLT_HISinglePhoton20_Eta3p1_Cent50_100_v', 
        'HLT_HISinglePhoton20_Eta3p1_v', 
        'HLT_HISinglePhoton30_Eta1p5_Cent30_100_v', 
        'HLT_HISinglePhoton30_Eta1p5_Cent50_100_v', 
        'HLT_HISinglePhoton30_Eta1p5_v', 
        'HLT_HISinglePhoton30_Eta3p1_Cent30_100_v', 
        'HLT_HISinglePhoton30_Eta3p1_Cent50_100_v', 
        'HLT_HISinglePhoton30_Eta3p1_v', 
        'HLT_HISinglePhoton40_Eta1p5_Cent30_100_v', 
        'HLT_HISinglePhoton40_Eta1p5_Cent50_100_v', 
        'HLT_HISinglePhoton40_Eta1p5_v', 
        'HLT_HISinglePhoton40_Eta2p1_v', 
        'HLT_HISinglePhoton40_Eta3p1_Cent30_100_v', 
        'HLT_HISinglePhoton40_Eta3p1_Cent50_100_v', 
        'HLT_HISinglePhoton40_Eta3p1_v', 
        'HLT_HISinglePhoton50_Eta1p5_v', 
        'HLT_HISinglePhoton50_Eta3p1_v', 
        'HLT_HISinglePhoton60_Eta1p5_v', 
        'HLT_HISinglePhoton60_Eta3p1_v'),
    triggerResults = cms.InputTag("TriggerResults","","HLT")
)


process.inclusiveJetAnalyzer = cms.EDAnalyzer("HiInclusiveJetAnalyzer",
    L1gtReadout = cms.InputTag("gtDigis"),
    doHiJetID = cms.untracked.bool(True),
    doLifeTimeTagging = cms.untracked.bool(False),
    doStandardJetID = cms.untracked.bool(False),
    doSubEvent = cms.untracked.bool(False),
    eventInfoTag = cms.InputTag("generator"),
    fillGenJets = cms.untracked.bool(False),
    genjetTag = cms.InputTag("iterativeCone5HiGenJets"),
    hltTrgNames = cms.untracked.vstring('HLT_HIMinBiasHfOrBSC_Core', 
        'HLT_HIJet35U', 
        'HLT_HIJet35U_Core', 
        'HLT_HIJet50U_Core'),
    hltTrgResults = cms.untracked.string('TriggerResults::HLT'),
    isMC = cms.untracked.bool(False),
    jetTag = cms.InputTag("icPu5patJets"),
    matchTag = cms.untracked.InputTag("akPu3PFpatJets"),
    rParam = cms.double(0.5),
    trackQuality = cms.untracked.string('highPurity'),
    trackTag = cms.InputTag("hiTracks"),
    useCentrality = cms.untracked.bool(False),
    useHepMC = cms.untracked.bool(False),
    useQuality = cms.untracked.bool(True)
)


process.pfcandAnalyzer = cms.EDAnalyzer("HiPFCandAnalyzer",
    bkg = cms.InputTag("voronoiBackgroundPF"),
    doJets_ = cms.untracked.bool(False),
    doUEraw_ = cms.untracked.bool(True),
    doVS = cms.untracked.bool(True),
    etaBins = cms.int32(15),
    fourierOrder = cms.int32(5),
    genLabel = cms.InputTag("hiGenParticles"),
    genPtMin = cms.double(0.5),
    jetLabel = cms.InputTag("ak5patJets"),
    jetPtMin = cms.double(20.0),
    pfCandidateLabel = cms.InputTag("particleFlowTmp"),
    pfPtMin = cms.double(0),
    skipCharged = cms.untracked.bool(False),
    verbosity = cms.untracked.int32(0)
)


process.pixelTrack = cms.EDAnalyzer("TrackAnalyzer",
    associatorMap = cms.InputTag("tpRecoAssocHiGeneralTracks"),
    beamSpotSrc = cms.untracked.InputTag("offlineBeamSpot"),
    doMVA = cms.untracked.bool(True),
    doPFMatching = cms.untracked.bool(True),
    doSimTrack = cms.untracked.bool(False),
    doSimVertex = cms.untracked.bool(False),
    fillSimTrack = cms.untracked.bool(False),
    mvaSrc = cms.InputTag("hiGeneralTracks","MVAVals"),
    particleSrc = cms.InputTag("genParticles"),
    pfCandSrc = cms.InputTag("particleFlowTmp"),
    qualityString = cms.untracked.string('highPurity'),
    qualityStrings = cms.untracked.vstring('highPurity'),
    simTrackPtMin = cms.untracked.double(0.4),
    tpEffSrc = cms.untracked.InputTag("mix","MergedTrackTruth"),
    tpFakeSrc = cms.untracked.InputTag("mix","MergedTrackTruth"),
    trackPtMin = cms.untracked.double(0.4),
    trackSrc = cms.InputTag("hiGeneralAndPixelTracks"),
    useQuality = cms.untracked.bool(False),
    vertexSrc = cms.vstring('hiSelectedVertex')
)


process.ppTrack = cms.EDAnalyzer("TrackAnalyzer",
    associatorMap = cms.InputTag("tpRecoAssocHiGeneralTracks"),
    beamSpotSrc = cms.untracked.InputTag("offlineBeamSpot"),
    doMVA = cms.untracked.bool(True),
    doPFMatching = cms.untracked.bool(True),
    doSimTrack = cms.untracked.bool(False),
    doSimVertex = cms.untracked.bool(False),
    fillSimTrack = cms.untracked.bool(False),
    mvaSrc = cms.InputTag("generalTracks","MVAVals"),
    particleSrc = cms.InputTag("genParticles"),
    pfCandSrc = cms.InputTag("particleFlow"),
    qualityString = cms.untracked.string('highPurity'),
    qualityStrings = cms.untracked.vstring('highPurity', 
        'tight', 
        'loose'),
    simTrackPtMin = cms.untracked.double(0.4),
    tpEffSrc = cms.untracked.InputTag("mix","MergedTrackTruth"),
    tpFakeSrc = cms.untracked.InputTag("mix","MergedTrackTruth"),
    trackPtMin = cms.untracked.double(0.49),
    trackSrc = cms.InputTag("generalTracks"),
    useQuality = cms.untracked.bool(False),
    vertexSrc = cms.vstring('offlinePrimaryVertices')
)


process.skimanalysis = cms.EDAnalyzer("FilterAnalyzer",
    hltresults = cms.InputTag("TriggerResults","","HiForest"),
    superFilters = cms.vstring('superFilterPath')
)


process.tupel = cms.EDAnalyzer("Tupel",
    CalojetLabel = cms.untracked.InputTag("ak4CalopatJets"),
    elecMatch = cms.string('elecTriggerMatchHLTElecs'),
    electronSrc = cms.untracked.InputTag("patElectrons"),
    genSrc = cms.untracked.InputTag("genParticles"),
    gjetSrc = cms.untracked.InputTag("ak4HiGenJets"),
    jetSrc = cms.untracked.InputTag("akPu4PFpatJetsWithBtagging"),
    lheSource = cms.untracked.InputTag("source"),
    metSource = cms.VInputTag("slimmedMETs", "slimmedMETs", "slimmedMETs", "slimmedMETs"),
    metSrc = cms.untracked.InputTag("patMETsPF"),
    muonMatch = cms.string('muonTriggerMatchHLTMuons'),
    muonMatch2 = cms.string('muonTriggerMatchHLTMuons2'),
    muonSrc = cms.untracked.InputTag("patMuonsWithTrigger"),
    photonSrc = cms.untracked.InputTag("patPhotons"),
    trigger = cms.InputTag("patTrigger"),
    vtxSrc = cms.untracked.InputTag("offlinePrimaryVertices")
)


process.akVs4CaloJetBtaggingMu = cms.Sequence(process.akVs4CaloSoftPFMuonsTagInfos+process.akVs4CaloSoftPFMuonBJetTags+process.akVs4CaloSoftPFMuonByIP3dBJetTags+process.akVs4CaloSoftPFMuonByPtBJetTags+process.akVs4CaloNegativeSoftPFMuonByPtBJetTags+process.akVs4CaloPositiveSoftPFMuonByPtBJetTags)


process.akVs4PFJetBtaggingIP = cms.Sequence(process.akVs4PFImpactParameterTagInfos+process.akVs4PFTrackCountingHighEffBJetTags+process.akVs4PFTrackCountingHighPurBJetTags+process.akVs4PFJetProbabilityBJetTags+process.akVs4PFJetBProbabilityBJetTags+process.akVs4PFPositiveOnlyJetProbabilityBJetTags+process.akVs4PFNegativeOnlyJetProbabilityBJetTags+process.akVs4PFNegativeTrackCountingHighEffBJetTags+process.akVs4PFNegativeTrackCountingHighPurBJetTags+process.akVs4PFNegativeOnlyJetBProbabilityBJetTags+process.akVs4PFPositiveOnlyJetBProbabilityBJetTags)


process.trackSequencesPbPb = cms.Sequence(process.anaTrack)


process.hiReRecoCaloJets = cms.Sequence(process.akPu1CaloJets+process.akPu2CaloJets+process.akPu3CaloJets+process.akPu4CaloJets+process.akPu5CaloJets+process.akPu6CaloJets+process.akVs1CaloJets+process.akVs2CaloJets+process.akVs3CaloJets+process.akVs4CaloJets+process.akVs5CaloJets+process.akVs6CaloJets+process.ak1CaloJets+process.ak2CaloJets+process.ak3CaloJets+process.ak4CaloJets+process.ak5CaloJets+process.ak6CaloJets)


process.patJetFlavourId = cms.Sequence(process.patJetPartons+process.patJetFlavourAssociation)


process.akVs5CaloJetBtaggingSV = cms.Sequence(process.akVs5CaloImpactParameterTagInfos+process.akVs5CaloSecondaryVertexTagInfos+process.akVs5CaloSimpleSecondaryVertexHighEffBJetTags+process.akVs5CaloSimpleSecondaryVertexHighPurBJetTags+process.akVs5CaloCombinedSecondaryVertexBJetTags+process.akVs5CaloCombinedSecondaryVertexV2BJetTags)


process.akVs4PFPatJetFlavourIdLegacy = cms.Sequence(process.akVs4PFPatJetPartonAssociationLegacy+process.akVs4PFPatJetFlavourAssociationLegacy)


process.akVs3PFJetBtaggingSV = cms.Sequence(process.akVs3PFImpactParameterTagInfos+process.akVs3PFSecondaryVertexTagInfos+process.akVs3PFSimpleSecondaryVertexHighEffBJetTags+process.akVs3PFSimpleSecondaryVertexHighPurBJetTags+process.akVs3PFCombinedSecondaryVertexBJetTags+process.akVs3PFCombinedSecondaryVertexV2BJetTags)


process.hiRecoPFJets = cms.Sequence(process.PFTowers+process.akPu3PFJets+process.akPu4PFJets+process.akPu5PFJets+process.voronoiBackgroundPF+process.akVs3PFJets+process.akVs4PFJets+process.akVs5PFJets)


process.inclusiveCandidateVertexing = cms.Sequence(process.inclusiveCandidateVertexFinder+process.candidateVertexMerger+process.candidateVertexArbitrator+process.inclusiveCandidateSecondaryVertices)


process.akPu4CaloJetBtaggingMu = cms.Sequence(process.akPu4CaloSoftPFMuonsTagInfos+process.akPu4CaloSoftPFMuonBJetTags+process.akPu4CaloSoftPFMuonByIP3dBJetTags+process.akPu4CaloSoftPFMuonByPtBJetTags+process.akPu4CaloNegativeSoftPFMuonByPtBJetTags+process.akPu4CaloPositiveSoftPFMuonByPtBJetTags)


process.akPu3CaloJetBtaggingSV = cms.Sequence(process.akPu3CaloImpactParameterTagInfos+process.akPu3CaloSecondaryVertexTagInfos+process.akPu3CaloSimpleSecondaryVertexHighEffBJetTags+process.akPu3CaloSimpleSecondaryVertexHighPurBJetTags+process.akPu3CaloCombinedSecondaryVertexBJetTags+process.akPu3CaloCombinedSecondaryVertexV2BJetTags)


process.akVs3CaloJetBtaggingSV = cms.Sequence(process.akVs3CaloImpactParameterTagInfos+process.akVs3CaloSecondaryVertexTagInfos+process.akVs3CaloSimpleSecondaryVertexHighEffBJetTags+process.akVs3CaloSimpleSecondaryVertexHighPurBJetTags+process.akVs3CaloCombinedSecondaryVertexBJetTags+process.akVs3CaloCombinedSecondaryVertexV2BJetTags)


process.patTriggerMatchers1Mu = cms.Sequence(process.muonMatchHLTL2+process.muonMatchHLTL3+process.muonMatchHLTL3T)


process.akVs3CaloJetBtaggingNegSV = cms.Sequence(process.akVs3CaloImpactParameterTagInfos+process.akVs3CaloSecondaryVertexNegativeTagInfos+process.akVs3CaloNegativeSimpleSecondaryVertexHighEffBJetTags+process.akVs3CaloNegativeSimpleSecondaryVertexHighPurBJetTags+process.akVs3CaloNegativeCombinedSecondaryVertexBJetTags+process.akVs3CaloPositiveCombinedSecondaryVertexBJetTags)


process.akPu5CaloJetBtaggingNegSV = cms.Sequence(process.akPu5CaloImpactParameterTagInfos+process.akPu5CaloSecondaryVertexNegativeTagInfos+process.akPu5CaloNegativeSimpleSecondaryVertexHighEffBJetTags+process.akPu5CaloNegativeSimpleSecondaryVertexHighPurBJetTags+process.akPu5CaloNegativeCombinedSecondaryVertexBJetTags+process.akPu5CaloPositiveCombinedSecondaryVertexBJetTags)


process.patPhotonSequence = cms.Sequence(process.patPhotons)


process.pfBTagging = cms.Sequence(process.pfImpactParameterTagInfos+process.pfTrackCountingHighEffBJetTags+process.pfTrackCountingHighPurBJetTags+process.pfJetProbabilityBJetTags+process.pfJetBProbabilityBJetTags+process.pfSecondaryVertexTagInfos+process.pfSimpleSecondaryVertexHighEffBJetTags+process.pfSimpleSecondaryVertexHighPurBJetTags+process.pfCombinedSecondaryVertexBJetTags+process.pfCombinedSecondaryVertexV2BJetTags+process.inclusiveCandidateVertexing+process.pfInclusiveSecondaryVertexFinderTagInfos+process.pfCombinedInclusiveSecondaryVertexV2BJetTags+process.softPFMuonsTagInfos+process.softPFMuonBJetTags+process.softPFElectronsTagInfos+process.softPFElectronBJetTags+process.pfCombinedMVABJetTags+process.pfCombinedSecondaryVertexSoftLeptonBJetTags)


process.akVs5PFJetBtaggingSV = cms.Sequence(process.akVs5PFImpactParameterTagInfos+process.akVs5PFSecondaryVertexTagInfos+process.akVs5PFSimpleSecondaryVertexHighEffBJetTags+process.akVs5PFSimpleSecondaryVertexHighPurBJetTags+process.akVs5PFCombinedSecondaryVertexBJetTags+process.akVs5PFCombinedSecondaryVertexV2BJetTags)


process.akPu3CaloPatJetFlavourIdLegacy = cms.Sequence(process.akPu3CaloPatJetPartonAssociationLegacy+process.akPu3CaloPatJetFlavourAssociationLegacy)


process.akVs2PFJetBtaggingNegSV = cms.Sequence(process.akVs2PFImpactParameterTagInfos+process.akVs2PFSecondaryVertexNegativeTagInfos+process.akVs2PFNegativeSimpleSecondaryVertexHighEffBJetTags+process.akVs2PFNegativeSimpleSecondaryVertexHighPurBJetTags+process.akVs2PFNegativeCombinedSecondaryVertexBJetTags+process.akVs2PFPositiveCombinedSecondaryVertexBJetTags)


process.akVs2PFJetBtaggingMu = cms.Sequence(process.akVs2PFSoftPFMuonsTagInfos+process.akVs2PFSoftPFMuonBJetTags+process.akVs2PFSoftPFMuonByIP3dBJetTags+process.akVs2PFSoftPFMuonByPtBJetTags+process.akVs2PFNegativeSoftPFMuonByPtBJetTags+process.akVs2PFPositiveSoftPFMuonByPtBJetTags)


process.hfnegTowers = cms.Sequence(process.towersAboveThreshold+process.hfNegTowers)


process.akPu2CaloJetBtaggingMu = cms.Sequence(process.akPu2CaloSoftPFMuonsTagInfos+process.akPu2CaloSoftPFMuonBJetTags+process.akPu2CaloSoftPFMuonByIP3dBJetTags+process.akPu2CaloSoftPFMuonByPtBJetTags+process.akPu2CaloNegativeSoftPFMuonByPtBJetTags+process.akPu2CaloPositiveSoftPFMuonByPtBJetTags)


process.akPu4PFJetBtaggingNegSV = cms.Sequence(process.akPu4PFImpactParameterTagInfos+process.akPu4PFSecondaryVertexNegativeTagInfos+process.akPu4PFNegativeSimpleSecondaryVertexHighEffBJetTags+process.akPu4PFNegativeSimpleSecondaryVertexHighPurBJetTags+process.akPu4PFNegativeCombinedSecondaryVertexBJetTags+process.akPu4PFPositiveCombinedSecondaryVertexBJetTags)


process.akPu3PFJetBtaggingMu = cms.Sequence(process.akPu3PFSoftPFMuonsTagInfos+process.akPu3PFSoftPFMuonBJetTags+process.akPu3PFSoftPFMuonByIP3dBJetTags+process.akPu3PFSoftPFMuonByPtBJetTags+process.akPu3PFNegativeSoftPFMuonByPtBJetTags+process.akPu3PFPositiveSoftPFMuonByPtBJetTags)


process.akVs2PFJetBtaggingSV = cms.Sequence(process.akVs2PFImpactParameterTagInfos+process.akVs2PFSecondaryVertexTagInfos+process.akVs2PFSimpleSecondaryVertexHighEffBJetTags+process.akVs2PFSimpleSecondaryVertexHighPurBJetTags+process.akVs2PFCombinedSecondaryVertexBJetTags+process.akVs2PFCombinedSecondaryVertexV2BJetTags)


process.akPu3CaloJetBtaggingMu = cms.Sequence(process.akPu3CaloSoftPFMuonsTagInfos+process.akPu3CaloSoftPFMuonBJetTags+process.akPu3CaloSoftPFMuonByIP3dBJetTags+process.akPu3CaloSoftPFMuonByPtBJetTags+process.akPu3CaloNegativeSoftPFMuonByPtBJetTags+process.akPu3CaloPositiveSoftPFMuonByPtBJetTags)


process.akPu5PFJetBtaggingMu = cms.Sequence(process.akPu5PFSoftPFMuonsTagInfos+process.akPu5PFSoftPFMuonBJetTags+process.akPu5PFSoftPFMuonByIP3dBJetTags+process.akPu5PFSoftPFMuonByPtBJetTags+process.akPu5PFNegativeSoftPFMuonByPtBJetTags+process.akPu5PFPositiveSoftPFMuonByPtBJetTags)


process.akVs5PFPatJetFlavourIdLegacy = cms.Sequence(process.akVs5PFPatJetPartonAssociationLegacy+process.akVs5PFPatJetFlavourAssociationLegacy)


process.inclusiveCandidateVertexingCtagL = cms.Sequence(process.inclusiveCandidateVertexFinderCtagL+process.candidateVertexMergerCtagL+process.candidateVertexArbitratorCtagL+process.inclusiveCandidateSecondaryVerticesCtagL)


process.akPu2PFJetBtaggingSV = cms.Sequence(process.akPu2PFImpactParameterTagInfos+process.akPu2PFSecondaryVertexTagInfos+process.akPu2PFSimpleSecondaryVertexHighEffBJetTags+process.akPu2PFSimpleSecondaryVertexHighPurBJetTags+process.akPu2PFCombinedSecondaryVertexBJetTags+process.akPu2PFCombinedSecondaryVertexV2BJetTags)


process.akPu5CaloPatJetFlavourIdLegacy = cms.Sequence(process.akPu5CaloPatJetPartonAssociationLegacy+process.akPu5CaloPatJetFlavourAssociationLegacy)


process.hfCoincFilter = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter+process.hfNegFilter)


process.akPu2PFPatJetFlavourIdLegacy = cms.Sequence(process.akPu2PFPatJetPartonAssociationLegacy+process.akPu2PFPatJetFlavourAssociationLegacy)


process.akVs3PFJetBtaggingMu = cms.Sequence(process.akVs3PFSoftPFMuonsTagInfos+process.akVs3PFSoftPFMuonBJetTags+process.akVs3PFSoftPFMuonByIP3dBJetTags+process.akVs3PFSoftPFMuonByPtBJetTags+process.akVs3PFNegativeSoftPFMuonByPtBJetTags+process.akVs3PFPositiveSoftPFMuonByPtBJetTags)


process.hfnegFilter2 = cms.Sequence(process.hfnegTowers+process.hfNegFilter2)


process.hfnegFilter3 = cms.Sequence(process.hfnegTowers+process.hfNegFilter3)


process.akVs4CaloJetBtaggingNegSV = cms.Sequence(process.akVs4CaloImpactParameterTagInfos+process.akVs4CaloSecondaryVertexNegativeTagInfos+process.akVs4CaloNegativeSimpleSecondaryVertexHighEffBJetTags+process.akVs4CaloNegativeSimpleSecondaryVertexHighPurBJetTags+process.akVs4CaloNegativeCombinedSecondaryVertexBJetTags+process.akVs4CaloPositiveCombinedSecondaryVertexBJetTags)


process.hfnegFilter4 = cms.Sequence(process.hfnegTowers+process.hfNegFilter4)


process.akVs5CaloJetBtaggingIP = cms.Sequence(process.akVs5CaloImpactParameterTagInfos+process.akVs5CaloTrackCountingHighEffBJetTags+process.akVs5CaloTrackCountingHighPurBJetTags+process.akVs5CaloJetProbabilityBJetTags+process.akVs5CaloJetBProbabilityBJetTags+process.akVs5CaloPositiveOnlyJetProbabilityBJetTags+process.akVs5CaloNegativeOnlyJetProbabilityBJetTags+process.akVs5CaloNegativeTrackCountingHighEffBJetTags+process.akVs5CaloNegativeTrackCountingHighPurBJetTags+process.akVs5CaloNegativeOnlyJetBProbabilityBJetTags+process.akVs5CaloPositiveOnlyJetBProbabilityBJetTags)


process.inclusiveVertexing = cms.Sequence(process.inclusiveVertexFinder+process.vertexMerger+process.trackVertexArbitrator+process.inclusiveSecondaryVertices)


process.akVs2CaloJetBtaggingSV = cms.Sequence(process.akVs2CaloImpactParameterTagInfos+process.akVs2CaloSecondaryVertexTagInfos+process.akVs2CaloSimpleSecondaryVertexHighEffBJetTags+process.akVs2CaloSimpleSecondaryVertexHighPurBJetTags+process.akVs2CaloCombinedSecondaryVertexBJetTags+process.akVs2CaloCombinedSecondaryVertexV2BJetTags)


process.legacyBTagging = cms.Sequence(process.impactParameterTagInfos+process.trackCountingHighEffBJetTags+process.trackCountingHighPurBJetTags+process.jetProbabilityBJetTags+process.jetBProbabilityBJetTags+process.secondaryVertexTagInfos+process.simpleSecondaryVertexHighEffBJetTags+process.simpleSecondaryVertexHighPurBJetTags+process.combinedSecondaryVertexBJetTags+process.inclusiveSecondaryVertexFinderTagInfos+process.combinedInclusiveSecondaryVertexV2BJetTags+process.ghostTrackVertexTagInfos+process.ghostTrackBJetTags+process.softPFMuonsTagInfos+process.softPFMuonBJetTags+process.softPFElectronsTagInfos+process.softPFElectronBJetTags+process.combinedMVABJetTags)


process.hfnegFilter = cms.Sequence(process.hfnegTowers+process.hfNegFilter)


process.hfnegFilter5 = cms.Sequence(process.hfnegTowers+process.hfNegFilter5)


process.akPu2CaloJetBtaggingNegSV = cms.Sequence(process.akPu2CaloImpactParameterTagInfos+process.akPu2CaloSecondaryVertexNegativeTagInfos+process.akPu2CaloNegativeSimpleSecondaryVertexHighEffBJetTags+process.akPu2CaloNegativeSimpleSecondaryVertexHighPurBJetTags+process.akPu2CaloNegativeCombinedSecondaryVertexBJetTags+process.akPu2CaloPositiveCombinedSecondaryVertexBJetTags)


process.akVs3CaloJetBtaggingMu = cms.Sequence(process.akVs3CaloSoftPFMuonsTagInfos+process.akVs3CaloSoftPFMuonBJetTags+process.akVs3CaloSoftPFMuonByIP3dBJetTags+process.akVs3CaloSoftPFMuonByPtBJetTags+process.akVs3CaloNegativeSoftPFMuonByPtBJetTags+process.akVs3CaloPositiveSoftPFMuonByPtBJetTags)


process.akPu2PFJetBtaggingIP = cms.Sequence(process.akPu2PFImpactParameterTagInfos+process.akPu2PFTrackCountingHighEffBJetTags+process.akPu2PFTrackCountingHighPurBJetTags+process.akPu2PFJetProbabilityBJetTags+process.akPu2PFJetBProbabilityBJetTags+process.akPu2PFPositiveOnlyJetProbabilityBJetTags+process.akPu2PFNegativeOnlyJetProbabilityBJetTags+process.akPu2PFNegativeTrackCountingHighEffBJetTags+process.akPu2PFNegativeTrackCountingHighPurBJetTags+process.akPu2PFNegativeOnlyJetBProbabilityBJetTags+process.akPu2PFPositiveOnlyJetBProbabilityBJetTags)


process.akVs2PFJetBtaggingIP = cms.Sequence(process.akVs2PFImpactParameterTagInfos+process.akVs2PFTrackCountingHighEffBJetTags+process.akVs2PFTrackCountingHighPurBJetTags+process.akVs2PFJetProbabilityBJetTags+process.akVs2PFJetBProbabilityBJetTags+process.akVs2PFPositiveOnlyJetProbabilityBJetTags+process.akVs2PFNegativeOnlyJetProbabilityBJetTags+process.akVs2PFNegativeTrackCountingHighEffBJetTags+process.akVs2PFNegativeTrackCountingHighPurBJetTags+process.akVs2PFNegativeOnlyJetBProbabilityBJetTags+process.akVs2PFPositiveOnlyJetBProbabilityBJetTags)


process.akPu3PFJetBtaggingNegSV = cms.Sequence(process.akPu3PFImpactParameterTagInfos+process.akPu3PFSecondaryVertexNegativeTagInfos+process.akPu3PFNegativeSimpleSecondaryVertexHighEffBJetTags+process.akPu3PFNegativeSimpleSecondaryVertexHighPurBJetTags+process.akPu3PFNegativeCombinedSecondaryVertexBJetTags+process.akPu3PFPositiveCombinedSecondaryVertexBJetTags)


process.akVs2CaloJetBtaggingNegSV = cms.Sequence(process.akVs2CaloImpactParameterTagInfos+process.akVs2CaloSecondaryVertexNegativeTagInfos+process.akVs2CaloNegativeSimpleSecondaryVertexHighEffBJetTags+process.akVs2CaloNegativeSimpleSecondaryVertexHighPurBJetTags+process.akVs2CaloNegativeCombinedSecondaryVertexBJetTags+process.akVs2CaloPositiveCombinedSecondaryVertexBJetTags)


process.akPu4PFJetBtaggingSV = cms.Sequence(process.akPu4PFImpactParameterTagInfos+process.akPu4PFSecondaryVertexTagInfos+process.akPu4PFSimpleSecondaryVertexHighEffBJetTags+process.akPu4PFSimpleSecondaryVertexHighPurBJetTags+process.akPu4PFCombinedSecondaryVertexBJetTags+process.akPu4PFCombinedSecondaryVertexV2BJetTags)


process.ak5JTAExplicit = cms.Sequence(process.ak5JetTracksAssociatorExplicit)


process.akPu4CaloPatJetFlavourIdLegacy = cms.Sequence(process.akPu4CaloPatJetPartonAssociationLegacy+process.akPu4CaloPatJetFlavourAssociationLegacy)


process.hfposTowers = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers)


process.akPu5CaloJetBtaggingSV = cms.Sequence(process.akPu5CaloImpactParameterTagInfos+process.akPu5CaloSecondaryVertexTagInfos+process.akPu5CaloSimpleSecondaryVertexHighEffBJetTags+process.akPu5CaloSimpleSecondaryVertexHighPurBJetTags+process.akPu5CaloCombinedSecondaryVertexBJetTags+process.akPu5CaloCombinedSecondaryVertexV2BJetTags)


process.akPu5CaloJetBtaggingIP = cms.Sequence(process.akPu5CaloImpactParameterTagInfos+process.akPu5CaloTrackCountingHighEffBJetTags+process.akPu5CaloTrackCountingHighPurBJetTags+process.akPu5CaloJetProbabilityBJetTags+process.akPu5CaloJetBProbabilityBJetTags+process.akPu5CaloPositiveOnlyJetProbabilityBJetTags+process.akPu5CaloNegativeOnlyJetProbabilityBJetTags+process.akPu5CaloNegativeTrackCountingHighEffBJetTags+process.akPu5CaloNegativeTrackCountingHighPurBJetTags+process.akPu5CaloNegativeOnlyJetBProbabilityBJetTags+process.akPu5CaloPositiveOnlyJetBProbabilityBJetTags)


process.akVs2CaloJetBtaggingIP = cms.Sequence(process.akVs2CaloImpactParameterTagInfos+process.akVs2CaloTrackCountingHighEffBJetTags+process.akVs2CaloTrackCountingHighPurBJetTags+process.akVs2CaloJetProbabilityBJetTags+process.akVs2CaloJetBProbabilityBJetTags+process.akVs2CaloPositiveOnlyJetProbabilityBJetTags+process.akVs2CaloNegativeOnlyJetProbabilityBJetTags+process.akVs2CaloNegativeTrackCountingHighEffBJetTags+process.akVs2CaloNegativeTrackCountingHighPurBJetTags+process.akVs2CaloNegativeOnlyJetBProbabilityBJetTags+process.akVs2CaloPositiveOnlyJetBProbabilityBJetTags)


process.akVs4CaloJetBtaggingSV = cms.Sequence(process.akVs4CaloImpactParameterTagInfos+process.akVs4CaloSecondaryVertexTagInfos+process.akVs4CaloSimpleSecondaryVertexHighEffBJetTags+process.akVs4CaloSimpleSecondaryVertexHighPurBJetTags+process.akVs4CaloCombinedSecondaryVertexBJetTags+process.akVs4CaloCombinedSecondaryVertexV2BJetTags)


process.akVs3CaloPatJetFlavourIdLegacy = cms.Sequence(process.akVs3CaloPatJetPartonAssociationLegacy+process.akVs3CaloPatJetFlavourAssociationLegacy)


process.akPu3PFJetBtaggingSV = cms.Sequence(process.akPu3PFImpactParameterTagInfos+process.akPu3PFSecondaryVertexTagInfos+process.akPu3PFSimpleSecondaryVertexHighEffBJetTags+process.akPu3PFSimpleSecondaryVertexHighPurBJetTags+process.akPu3PFCombinedSecondaryVertexBJetTags+process.akPu3PFCombinedSecondaryVertexV2BJetTags)


process.akPu4PFPatJetFlavourIdLegacy = cms.Sequence(process.akPu4PFPatJetPartonAssociationLegacy+process.akPu4PFPatJetFlavourAssociationLegacy)


process.patTriggerMatchers2Mu = cms.Sequence(process.muonMatchHLTCtfTrack+process.muonMatchHLTCtfTrack2+process.muonMatchHLTTrackMu)


process.akVs2PFPatJetFlavourIdLegacy = cms.Sequence(process.akVs2PFPatJetPartonAssociationLegacy+process.akVs2PFPatJetFlavourAssociationLegacy)


process.akVs2CaloPatJetFlavourIdLegacy = cms.Sequence(process.akVs2CaloPatJetPartonAssociationLegacy+process.akVs2CaloPatJetFlavourAssociationLegacy)


process.akPu4PFJetBtaggingMu = cms.Sequence(process.akPu4PFSoftPFMuonsTagInfos+process.akPu4PFSoftPFMuonBJetTags+process.akPu4PFSoftPFMuonByIP3dBJetTags+process.akPu4PFSoftPFMuonByPtBJetTags+process.akPu4PFNegativeSoftPFMuonByPtBJetTags+process.akPu4PFPositiveSoftPFMuonByPtBJetTags)


process.ak5JTA = cms.Sequence(process.ak5JetTracksAssociatorAtVertexPF+process.ak5JetTracksAssociatorAtVertex+process.ak5JetTracksAssociatorAtCaloFace+process.ak5JetExtender)


process.akVs4CaloJetBtaggingIP = cms.Sequence(process.akVs4CaloImpactParameterTagInfos+process.akVs4CaloTrackCountingHighEffBJetTags+process.akVs4CaloTrackCountingHighPurBJetTags+process.akVs4CaloJetProbabilityBJetTags+process.akVs4CaloJetBProbabilityBJetTags+process.akVs4CaloPositiveOnlyJetProbabilityBJetTags+process.akVs4CaloNegativeOnlyJetProbabilityBJetTags+process.akVs4CaloNegativeTrackCountingHighEffBJetTags+process.akVs4CaloNegativeTrackCountingHighPurBJetTags+process.akVs4CaloNegativeOnlyJetBProbabilityBJetTags+process.akVs4CaloPositiveOnlyJetBProbabilityBJetTags)


process.caloTowersRec = cms.Sequence(process.towerMaker+process.towerMakerWithHO)


process.akVs2PFJetBtagging = cms.Sequence(process.akVs2PFJetBtaggingIP+process.akVs2PFJetBtaggingSV+process.akVs2PFJetBtaggingNegSV)


process.akVs4PFJetBtaggingMu = cms.Sequence(process.akVs4PFSoftPFMuonsTagInfos+process.akVs4PFSoftPFMuonBJetTags+process.akVs4PFSoftPFMuonByIP3dBJetTags+process.akVs4PFSoftPFMuonByPtBJetTags+process.akVs4PFNegativeSoftPFMuonByPtBJetTags+process.akVs4PFPositiveSoftPFMuonByPtBJetTags)


process.akPu5PFJetBtaggingNegSV = cms.Sequence(process.akPu5PFImpactParameterTagInfos+process.akPu5PFSecondaryVertexNegativeTagInfos+process.akPu5PFNegativeSimpleSecondaryVertexHighEffBJetTags+process.akPu5PFNegativeSimpleSecondaryVertexHighPurBJetTags+process.akPu5PFNegativeCombinedSecondaryVertexBJetTags+process.akPu5PFPositiveCombinedSecondaryVertexBJetTags)


process.hiRecoJets = cms.Sequence(process.caloTowersRec+process.caloTowers+process.iterativeConePu5CaloJets+process.akPu3CaloJets+process.akPu4CaloJets+process.akPu5CaloJets+process.voronoiBackgroundCalo+process.akVs2CaloJets+process.akVs3CaloJets+process.akVs4CaloJets+process.akVs5CaloJets)


process.akPu3CaloJetBtaggingNegSV = cms.Sequence(process.akPu3CaloImpactParameterTagInfos+process.akPu3CaloSecondaryVertexNegativeTagInfos+process.akPu3CaloNegativeSimpleSecondaryVertexHighEffBJetTags+process.akPu3CaloNegativeSimpleSecondaryVertexHighPurBJetTags+process.akPu3CaloNegativeCombinedSecondaryVertexBJetTags+process.akPu3CaloPositiveCombinedSecondaryVertexBJetTags)


process.akVs3PFJetBtaggingNegSV = cms.Sequence(process.akVs3PFImpactParameterTagInfos+process.akVs3PFSecondaryVertexNegativeTagInfos+process.akVs3PFNegativeSimpleSecondaryVertexHighEffBJetTags+process.akVs3PFNegativeSimpleSecondaryVertexHighPurBJetTags+process.akVs3PFNegativeCombinedSecondaryVertexBJetTags+process.akVs3PFPositiveCombinedSecondaryVertexBJetTags)


process.akVs3PFPatJetFlavourIdLegacy = cms.Sequence(process.akVs3PFPatJetPartonAssociationLegacy+process.akVs3PFPatJetFlavourAssociationLegacy)


process.akVs5CaloJetBtaggingNegSV = cms.Sequence(process.akVs5CaloImpactParameterTagInfos+process.akVs5CaloSecondaryVertexNegativeTagInfos+process.akVs5CaloNegativeSimpleSecondaryVertexHighEffBJetTags+process.akVs5CaloNegativeSimpleSecondaryVertexHighPurBJetTags+process.akVs5CaloNegativeCombinedSecondaryVertexBJetTags+process.akVs5CaloPositiveCombinedSecondaryVertexBJetTags)


process.akPu2CaloJetBtaggingIP = cms.Sequence(process.akPu2CaloImpactParameterTagInfos+process.akPu2CaloTrackCountingHighEffBJetTags+process.akPu2CaloTrackCountingHighPurBJetTags+process.akPu2CaloJetProbabilityBJetTags+process.akPu2CaloJetBProbabilityBJetTags+process.akPu2CaloPositiveOnlyJetProbabilityBJetTags+process.akPu2CaloNegativeOnlyJetProbabilityBJetTags+process.akPu2CaloNegativeTrackCountingHighEffBJetTags+process.akPu2CaloNegativeTrackCountingHighPurBJetTags+process.akPu2CaloNegativeOnlyJetBProbabilityBJetTags+process.akPu2CaloPositiveOnlyJetBProbabilityBJetTags)


process.patJetFlavourIdLegacy = cms.Sequence(process.patJetPartonsLegacy+process.patJetPartonAssociationLegacy+process.patJetFlavourAssociationLegacy)


process.akPu5PFJetBtaggingSV = cms.Sequence(process.akPu5PFImpactParameterTagInfos+process.akPu5PFSecondaryVertexTagInfos+process.akPu5PFSimpleSecondaryVertexHighEffBJetTags+process.akPu5PFSimpleSecondaryVertexHighPurBJetTags+process.akPu5PFCombinedSecondaryVertexBJetTags+process.akPu5PFCombinedSecondaryVertexV2BJetTags)


process.akVs4CaloPatJetFlavourIdLegacy = cms.Sequence(process.akVs4CaloPatJetPartonAssociationLegacy+process.akVs4CaloPatJetFlavourAssociationLegacy)


process.akVs5CaloJetBtaggingMu = cms.Sequence(process.akVs5CaloSoftPFMuonsTagInfos+process.akVs5CaloSoftPFMuonBJetTags+process.akVs5CaloSoftPFMuonByIP3dBJetTags+process.akVs5CaloSoftPFMuonByPtBJetTags+process.akVs5CaloNegativeSoftPFMuonByPtBJetTags+process.akVs5CaloPositiveSoftPFMuonByPtBJetTags)


process.akPu2PFJetBtaggingNegSV = cms.Sequence(process.akPu2PFImpactParameterTagInfos+process.akPu2PFSecondaryVertexNegativeTagInfos+process.akPu2PFNegativeSimpleSecondaryVertexHighEffBJetTags+process.akPu2PFNegativeSimpleSecondaryVertexHighPurBJetTags+process.akPu2PFNegativeCombinedSecondaryVertexBJetTags+process.akPu2PFPositiveCombinedSecondaryVertexBJetTags)


process.hiReRecoPFJets = cms.Sequence(process.akPu1PFJets+process.akPu2PFJets+process.akPu3PFJets+process.akPu4PFJets+process.akPu5PFJets+process.akPu6PFJets+process.akVs1PFJets+process.akVs2PFJets+process.akVs3PFJets+process.akVs4PFJets+process.akVs5PFJets+process.akVs6PFJets+process.ak1PFJets+process.ak2PFJets+process.ak3PFJets+process.ak4PFJets+process.ak5PFJets+process.ak6PFJets)


process.patElectronSequence = cms.Sequence(process.patElectrons)


process.hfCoincFilter5 = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter5+process.hfNegFilter5)


process.hfposFilter4 = cms.Sequence(process.hfposTowers+process.hfPosFilter4)


process.hfposFilter5 = cms.Sequence(process.hfposTowers+process.hfPosFilter5)


process.hfposFilter2 = cms.Sequence(process.hfposTowers+process.hfPosFilter2)


process.hfposFilter3 = cms.Sequence(process.hfposTowers+process.hfPosFilter3)


process.hfCoincFilter2 = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter2+process.hfNegFilter2)


process.akVs5PFJetBtaggingNegSV = cms.Sequence(process.akVs5PFImpactParameterTagInfos+process.akVs5PFSecondaryVertexNegativeTagInfos+process.akVs5PFNegativeSimpleSecondaryVertexHighEffBJetTags+process.akVs5PFNegativeSimpleSecondaryVertexHighPurBJetTags+process.akVs5PFNegativeCombinedSecondaryVertexBJetTags+process.akVs5PFPositiveCombinedSecondaryVertexBJetTags)


process.hfCoincFilter3 = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter3+process.hfNegFilter3)


process.akVs5CaloPatJetFlavourIdLegacy = cms.Sequence(process.akVs5CaloPatJetPartonAssociationLegacy+process.akVs5CaloPatJetFlavourAssociationLegacy)


process.hfCoincFilter4 = cms.Sequence(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter4+process.hfNegFilter4)


process.akPu3CaloJetBtaggingIP = cms.Sequence(process.akPu3CaloImpactParameterTagInfos+process.akPu3CaloTrackCountingHighEffBJetTags+process.akPu3CaloTrackCountingHighPurBJetTags+process.akPu3CaloJetProbabilityBJetTags+process.akPu3CaloJetBProbabilityBJetTags+process.akPu3CaloPositiveOnlyJetProbabilityBJetTags+process.akPu3CaloNegativeOnlyJetProbabilityBJetTags+process.akPu3CaloNegativeTrackCountingHighEffBJetTags+process.akPu3CaloNegativeTrackCountingHighPurBJetTags+process.akPu3CaloNegativeOnlyJetBProbabilityBJetTags+process.akPu3CaloPositiveOnlyJetBProbabilityBJetTags)


process.akPu4CaloJetBtaggingIP = cms.Sequence(process.akPu4CaloImpactParameterTagInfos+process.akPu4CaloTrackCountingHighEffBJetTags+process.akPu4CaloTrackCountingHighPurBJetTags+process.akPu4CaloJetProbabilityBJetTags+process.akPu4CaloJetBProbabilityBJetTags+process.akPu4CaloPositiveOnlyJetProbabilityBJetTags+process.akPu4CaloNegativeOnlyJetProbabilityBJetTags+process.akPu4CaloNegativeTrackCountingHighEffBJetTags+process.akPu4CaloNegativeTrackCountingHighPurBJetTags+process.akPu4CaloNegativeOnlyJetBProbabilityBJetTags+process.akPu4CaloPositiveOnlyJetBProbabilityBJetTags)


process.akVs5PFJetBtaggingMu = cms.Sequence(process.akVs5PFSoftPFMuonsTagInfos+process.akVs5PFSoftPFMuonBJetTags+process.akVs5PFSoftPFMuonByIP3dBJetTags+process.akVs5PFSoftPFMuonByPtBJetTags+process.akVs5PFNegativeSoftPFMuonByPtBJetTags+process.akVs5PFPositiveSoftPFMuonByPtBJetTags)


process.akVs2CaloJetBtagging = cms.Sequence(process.akVs2CaloJetBtaggingIP+process.akVs2CaloJetBtaggingSV+process.akVs2CaloJetBtaggingNegSV)


process.akPu3PFJetBtaggingIP = cms.Sequence(process.akPu3PFImpactParameterTagInfos+process.akPu3PFTrackCountingHighEffBJetTags+process.akPu3PFTrackCountingHighPurBJetTags+process.akPu3PFJetProbabilityBJetTags+process.akPu3PFJetBProbabilityBJetTags+process.akPu3PFPositiveOnlyJetProbabilityBJetTags+process.akPu3PFNegativeOnlyJetProbabilityBJetTags+process.akPu3PFNegativeTrackCountingHighEffBJetTags+process.akPu3PFNegativeTrackCountingHighPurBJetTags+process.akPu3PFNegativeOnlyJetBProbabilityBJetTags+process.akPu3PFPositiveOnlyJetBProbabilityBJetTags)


process.akPu2CaloPatJetFlavourIdLegacy = cms.Sequence(process.akPu2CaloPatJetPartonAssociationLegacy+process.akPu2CaloPatJetFlavourAssociationLegacy)


process.akPu5PFJetBtaggingIP = cms.Sequence(process.akPu5PFImpactParameterTagInfos+process.akPu5PFTrackCountingHighEffBJetTags+process.akPu5PFTrackCountingHighPurBJetTags+process.akPu5PFJetProbabilityBJetTags+process.akPu5PFJetBProbabilityBJetTags+process.akPu5PFPositiveOnlyJetProbabilityBJetTags+process.akPu5PFNegativeOnlyJetProbabilityBJetTags+process.akPu5PFNegativeTrackCountingHighEffBJetTags+process.akPu5PFNegativeTrackCountingHighPurBJetTags+process.akPu5PFNegativeOnlyJetBProbabilityBJetTags+process.akPu5PFPositiveOnlyJetBProbabilityBJetTags)


process.akPu4PFJetBtaggingIP = cms.Sequence(process.akPu4PFImpactParameterTagInfos+process.akPu4PFTrackCountingHighEffBJetTags+process.akPu4PFTrackCountingHighPurBJetTags+process.akPu4PFJetProbabilityBJetTags+process.akPu4PFJetBProbabilityBJetTags+process.akPu4PFPositiveOnlyJetProbabilityBJetTags+process.akPu4PFNegativeOnlyJetProbabilityBJetTags+process.akPu4PFNegativeTrackCountingHighEffBJetTags+process.akPu4PFNegativeTrackCountingHighPurBJetTags+process.akPu4PFNegativeOnlyJetBProbabilityBJetTags+process.akPu4PFPositiveOnlyJetBProbabilityBJetTags)


process.akPu2PFJetBtagging = cms.Sequence(process.akPu2PFJetBtaggingIP+process.akPu2PFJetBtaggingSV+process.akPu2PFJetBtaggingNegSV)


process.trackSequencesPP = cms.Sequence(process.ppTrack)


process.akPu2CaloJetBtaggingSV = cms.Sequence(process.akPu2CaloImpactParameterTagInfos+process.akPu2CaloSecondaryVertexTagInfos+process.akPu2CaloSimpleSecondaryVertexHighEffBJetTags+process.akPu2CaloSimpleSecondaryVertexHighPurBJetTags+process.akPu2CaloCombinedSecondaryVertexBJetTags+process.akPu2CaloCombinedSecondaryVertexV2BJetTags)


process.akVs4PFJetBtaggingSV = cms.Sequence(process.akVs4PFImpactParameterTagInfos+process.akVs4PFSecondaryVertexTagInfos+process.akVs4PFSimpleSecondaryVertexHighEffBJetTags+process.akVs4PFSimpleSecondaryVertexHighPurBJetTags+process.akVs4PFCombinedSecondaryVertexBJetTags+process.akVs4PFCombinedSecondaryVertexV2BJetTags)


process.akVs2CaloJetBtaggingMu = cms.Sequence(process.akVs2CaloSoftPFMuonsTagInfos+process.akVs2CaloSoftPFMuonBJetTags+process.akVs2CaloSoftPFMuonByIP3dBJetTags+process.akVs2CaloSoftPFMuonByPtBJetTags+process.akVs2CaloNegativeSoftPFMuonByPtBJetTags+process.akVs2CaloPositiveSoftPFMuonByPtBJetTags)


process.akPu4PFJetBtagging = cms.Sequence(process.akPu4PFJetBtaggingIP+process.akPu4PFJetBtaggingSV+process.akPu4PFJetBtaggingNegSV)


process.akVs2PFJetSequence_data = cms.Sequence(process.akVs2PFcorr+process.akVs2PFJetTracksAssociatorAtVertex+process.akVs2PFJetBtagging+process.akVs2PFpatJetsWithBtagging+process.akVs2PFJetAnalyzer)


process.akPu5PFPatJetFlavourIdLegacy = cms.Sequence(process.akPu5PFPatJetPartonAssociationLegacy+process.akPu5PFPatJetFlavourAssociationLegacy)


process.akPu4CaloJetBtaggingNegSV = cms.Sequence(process.akPu4CaloImpactParameterTagInfos+process.akPu4CaloSecondaryVertexNegativeTagInfos+process.akPu4CaloNegativeSimpleSecondaryVertexHighEffBJetTags+process.akPu4CaloNegativeSimpleSecondaryVertexHighPurBJetTags+process.akPu4CaloNegativeCombinedSecondaryVertexBJetTags+process.akPu4CaloPositiveCombinedSecondaryVertexBJetTags)


process.akPu4CaloJetBtaggingSV = cms.Sequence(process.akPu4CaloImpactParameterTagInfos+process.akPu4CaloSecondaryVertexTagInfos+process.akPu4CaloSimpleSecondaryVertexHighEffBJetTags+process.akPu4CaloSimpleSecondaryVertexHighPurBJetTags+process.akPu4CaloCombinedSecondaryVertexBJetTags+process.akPu4CaloCombinedSecondaryVertexV2BJetTags)


process.akPu2PFJetBtaggingMu = cms.Sequence(process.akPu2PFSoftPFMuonsTagInfos+process.akPu2PFSoftPFMuonBJetTags+process.akPu2PFSoftPFMuonByIP3dBJetTags+process.akPu2PFSoftPFMuonByPtBJetTags+process.akPu2PFNegativeSoftPFMuonByPtBJetTags+process.akPu2PFPositiveSoftPFMuonByPtBJetTags)


process.akVs2PFJetSequence_mc = cms.Sequence(process.akVs2PFmatch+process.akVs2PFparton+process.akVs2PFcorr+process.akVs2PFPatJetFlavourIdLegacy+process.akVs2PFJetTracksAssociatorAtVertex+process.akVs2PFJetBtagging+process.akVs2PFpatJetsWithBtagging+process.akVs2PFJetAnalyzer)


process.akVs4PFJetBtaggingNegSV = cms.Sequence(process.akVs4PFImpactParameterTagInfos+process.akVs4PFSecondaryVertexNegativeTagInfos+process.akVs4PFNegativeSimpleSecondaryVertexHighEffBJetTags+process.akVs4PFNegativeSimpleSecondaryVertexHighPurBJetTags+process.akVs4PFNegativeCombinedSecondaryVertexBJetTags+process.akVs4PFPositiveCombinedSecondaryVertexBJetTags)


process.akVs3CaloJetBtaggingIP = cms.Sequence(process.akVs3CaloImpactParameterTagInfos+process.akVs3CaloTrackCountingHighEffBJetTags+process.akVs3CaloTrackCountingHighPurBJetTags+process.akVs3CaloJetProbabilityBJetTags+process.akVs3CaloJetBProbabilityBJetTags+process.akVs3CaloPositiveOnlyJetProbabilityBJetTags+process.akVs3CaloNegativeOnlyJetProbabilityBJetTags+process.akVs3CaloNegativeTrackCountingHighEffBJetTags+process.akVs3CaloNegativeTrackCountingHighPurBJetTags+process.akVs3CaloNegativeOnlyJetBProbabilityBJetTags+process.akVs3CaloPositiveOnlyJetBProbabilityBJetTags)


process.akVs5PFJetBtaggingIP = cms.Sequence(process.akVs5PFImpactParameterTagInfos+process.akVs5PFTrackCountingHighEffBJetTags+process.akVs5PFTrackCountingHighPurBJetTags+process.akVs5PFJetProbabilityBJetTags+process.akVs5PFJetBProbabilityBJetTags+process.akVs5PFPositiveOnlyJetProbabilityBJetTags+process.akVs5PFNegativeOnlyJetProbabilityBJetTags+process.akVs5PFNegativeTrackCountingHighEffBJetTags+process.akVs5PFNegativeTrackCountingHighPurBJetTags+process.akVs5PFNegativeOnlyJetBProbabilityBJetTags+process.akVs5PFPositiveOnlyJetBProbabilityBJetTags)


process.akVs2CaloJetSequence_mc = cms.Sequence(process.akVs2Calomatch+process.akVs2Caloparton+process.akVs2Calocorr+process.akVs2CaloPatJetFlavourIdLegacy+process.akVs2CaloJetTracksAssociatorAtVertex+process.akVs2CaloJetBtagging+process.akVs2CalopatJetsWithBtagging+process.akVs2CaloJetAnalyzer)


process.patTriggerMatching = cms.Sequence(process.patTriggerFull+process.patTrigger+process.patTriggerMatchers1Mu+process.patTriggerMatchers2Mu+process.patMuonsWithTrigger)


process.akPu3PFJetBtagging = cms.Sequence(process.akPu3PFJetBtaggingIP+process.akPu3PFJetBtaggingSV+process.akPu3PFJetBtaggingNegSV)


process.akPu3PFPatJetFlavourIdLegacy = cms.Sequence(process.akPu3PFPatJetPartonAssociationLegacy+process.akPu3PFPatJetFlavourAssociationLegacy)


process.akPu5CaloJetBtaggingMu = cms.Sequence(process.akPu5CaloSoftPFMuonsTagInfos+process.akPu5CaloSoftPFMuonBJetTags+process.akPu5CaloSoftPFMuonByIP3dBJetTags+process.akPu5CaloSoftPFMuonByPtBJetTags+process.akPu5CaloNegativeSoftPFMuonByPtBJetTags+process.akPu5CaloPositiveSoftPFMuonByPtBJetTags)


process.akPu3PFJetSequence_mc = cms.Sequence(process.akPu3PFmatch+process.akPu3PFparton+process.akPu3PFcorr+process.akPu3PFPatJetFlavourIdLegacy+process.akPu3PFJetTracksAssociatorAtVertex+process.akPu3PFJetBtagging+process.akPu3PFpatJetsWithBtagging+process.akPu3PFJetAnalyzer)


process.akVs3PFJetBtaggingIP = cms.Sequence(process.akVs3PFImpactParameterTagInfos+process.akVs3PFTrackCountingHighEffBJetTags+process.akVs3PFTrackCountingHighPurBJetTags+process.akVs3PFJetProbabilityBJetTags+process.akVs3PFJetBProbabilityBJetTags+process.akVs3PFPositiveOnlyJetProbabilityBJetTags+process.akVs3PFNegativeOnlyJetProbabilityBJetTags+process.akVs3PFNegativeTrackCountingHighEffBJetTags+process.akVs3PFNegativeTrackCountingHighPurBJetTags+process.akVs3PFNegativeOnlyJetBProbabilityBJetTags+process.akVs3PFPositiveOnlyJetBProbabilityBJetTags)


process.akPu4PFJetSequence_mc = cms.Sequence(process.akPu4PFmatch+process.akPu4PFparton+process.akPu4PFcorr+process.akPu4PFPatJetFlavourIdLegacy+process.akPu4PFJetTracksAssociatorAtVertex+process.akPu4PFJetBtagging+process.akPu4PFpatJetsWithBtagging+process.akPu4PFJetAnalyzer)


process.pfCTagging = cms.Sequence(process.inclusiveCandidateVertexingCtagL+process.pfInclusiveSecondaryVertexFinderCtagLTagInfos+process.pfCombinedSecondaryVertexSoftLeptonCtagLJetTags)


process.btagging = cms.Sequence(process.legacyBTagging+process.pfBTagging)


process.akPu4CaloJetBtagging = cms.Sequence(process.akPu4CaloJetBtaggingIP+process.akPu4CaloJetBtaggingSV+process.akPu4CaloJetBtaggingNegSV)


process.akPu5PFJetBtagging = cms.Sequence(process.akPu5PFJetBtaggingIP+process.akPu5PFJetBtaggingSV+process.akPu5PFJetBtaggingNegSV)


process.akVs3PFJetBtagging = cms.Sequence(process.akVs3PFJetBtaggingIP+process.akVs3PFJetBtaggingSV+process.akVs3PFJetBtaggingNegSV)


process.akPu5PFJetSequence_data = cms.Sequence(process.akPu5PFcorr+process.akPu5PFJetTracksAssociatorAtVertex+process.akPu5PFJetBtagging+process.akPu5PFpatJetsWithBtagging+process.akPu5PFJetAnalyzer)


process.akPu4CaloJetSequence_data = cms.Sequence(process.akPu4Calocorr+process.akPu4CaloJetTracksAssociatorAtVertex+process.akPu4CaloJetBtagging+process.akPu4CalopatJetsWithBtagging+process.akPu4CaloJetAnalyzer)


process.akPu3PFJetSequence_jec = cms.Sequence(process.akPu3PFJetSequence_mc)


process.akPu4PFJetSequence_data = cms.Sequence(process.akPu4PFcorr+process.akPu4PFJetTracksAssociatorAtVertex+process.akPu4PFJetBtagging+process.akPu4PFpatJetsWithBtagging+process.akPu4PFJetAnalyzer)


process.akPu4PFJetSequence_jec = cms.Sequence(process.akPu4PFJetSequence_mc)


process.collisionEventSelectionAOD = cms.Sequence(process.hfCoincFilter3+process.primaryVertexFilter+process.clusterCompatibilityFilter)


process.akVs3CaloJetBtagging = cms.Sequence(process.akVs3CaloJetBtaggingIP+process.akVs3CaloJetBtaggingSV+process.akVs3CaloJetBtaggingNegSV)


process.collisionEventSelection = cms.Sequence(process.hfCoincFilter3+process.primaryVertexFilter+process.siPixelRecHits+process.hltPixelClusterShapeFilter)


process.akPu3PFJetSequence_data = cms.Sequence(process.akPu3PFcorr+process.akPu3PFJetTracksAssociatorAtVertex+process.akPu3PFJetBtagging+process.akPu3PFpatJetsWithBtagging+process.akPu3PFJetAnalyzer)


process.akVs2CaloJetSequence_data = cms.Sequence(process.akVs2Calocorr+process.akVs2CaloJetTracksAssociatorAtVertex+process.akVs2CaloJetBtagging+process.akVs2CalopatJetsWithBtagging+process.akVs2CaloJetAnalyzer)


process.akPu3CaloJetBtagging = cms.Sequence(process.akPu3CaloJetBtaggingIP+process.akPu3CaloJetBtaggingSV+process.akPu3CaloJetBtaggingNegSV)


process.patMuonsWithTriggerSequence = cms.Sequence(process.muonL1Info+process.patMuonsWithoutTrigger+process.patTriggerMatching)


process.akPu5PFJetSequence = cms.Sequence(process.akPu5PFJetSequence_data)


process.tupelPatSequence = cms.Sequence(process.patMuonsWithTriggerSequence+process.patPhotonSequence+process.patElectronSequence+process.tupel)


process.akPu4CaloJetSequence = cms.Sequence(process.akPu4CaloJetSequence_data)


process.akPu3PFJetSequence_mix = cms.Sequence(process.akPu3PFJetSequence_mc)


process.akPu4CaloJetSequence_mc = cms.Sequence(process.akPu4Calomatch+process.akPu4Caloparton+process.akPu4Calocorr+process.akPu4CaloPatJetFlavourIdLegacy+process.akPu4CaloJetTracksAssociatorAtVertex+process.akPu4CaloJetBtagging+process.akPu4CalopatJetsWithBtagging+process.akPu4CaloJetAnalyzer)


process.akVs3PFJetSequence_data = cms.Sequence(process.akVs3PFcorr+process.akVs3PFJetTracksAssociatorAtVertex+process.akVs3PFJetBtagging+process.akVs3PFpatJetsWithBtagging+process.akVs3PFJetAnalyzer)


process.akVs2CaloJetSequence_mix = cms.Sequence(process.akVs2CaloJetSequence_mc)


process.hfposFilter = cms.Sequence(process.hfposTowers+process.hfPosFilter)


process.akPu2PFJetSequence_mc = cms.Sequence(process.akPu2PFmatch+process.akPu2PFparton+process.akPu2PFcorr+process.akPu2PFPatJetFlavourIdLegacy+process.akPu2PFJetTracksAssociatorAtVertex+process.akPu2PFJetBtagging+process.akPu2PFpatJetsWithBtagging+process.akPu2PFJetAnalyzer)


process.akVs4PFJetBtagging = cms.Sequence(process.akVs4PFJetBtaggingIP+process.akVs4PFJetBtaggingSV+process.akVs4PFJetBtaggingNegSV)


process.akVs2PFJetSequence_jec = cms.Sequence(process.akVs2PFJetSequence_mc)


process.akPu4CaloJetSequence_jec = cms.Sequence(process.akPu4CaloJetSequence_mc)


process.akPu4PFJetSequence_mix = cms.Sequence(process.akPu4PFJetSequence_mc)


process.akPu4PFJetSequence = cms.Sequence(process.akPu4PFJetSequence_data)


process.akPu5CaloJetBtagging = cms.Sequence(process.akPu5CaloJetBtaggingIP+process.akPu5CaloJetBtaggingSV+process.akPu5CaloJetBtaggingNegSV)


process.akPu3PFJetSequence = cms.Sequence(process.akPu3PFJetSequence_data)


process.akVs2PFJetSequence_mix = cms.Sequence(process.akVs2PFJetSequence_mc)


process.akVs3PFJetSequence = cms.Sequence(process.akVs3PFJetSequence_data)


process.akVs5PFJetBtagging = cms.Sequence(process.akVs5PFJetBtaggingIP+process.akVs5PFJetBtaggingSV+process.akVs5PFJetBtaggingNegSV)


process.akPu2PFJetSequence_data = cms.Sequence(process.akPu2PFcorr+process.akPu2PFJetTracksAssociatorAtVertex+process.akPu2PFJetBtagging+process.akPu2PFpatJetsWithBtagging+process.akPu2PFJetAnalyzer)


process.akVs4PFJetSequence_mc = cms.Sequence(process.akVs4PFmatch+process.akVs4PFparton+process.akVs4PFcorr+process.akVs4PFPatJetFlavourIdLegacy+process.akVs4PFJetTracksAssociatorAtVertex+process.akVs4PFJetBtagging+process.akVs4PFpatJetsWithBtagging+process.akVs4PFJetAnalyzer)


process.hiRecoAllJets = cms.Sequence(process.caloTowersRec+process.caloTowers+process.iterativeConePu5CaloJets+process.ak1CaloJets+process.ak2CaloJets+process.ak3CaloJets+process.ak4CaloJets+process.ak5CaloJets+process.ak6CaloJets+process.ak7CaloJets+process.akPu1CaloJets+process.akPu2CaloJets+process.akPu3CaloJets+process.akPu4CaloJets+process.akPu5CaloJets+process.akPu6CaloJets+process.akPu7CaloJets+process.ktPu4CaloJets+process.ktPu6CaloJets+process.voronoiBackgroundCalo+process.akVs1CaloJets+process.akVs2CaloJets+process.akVs3CaloJets+process.akVs4CaloJets+process.akVs5CaloJets+process.akVs6CaloJets+process.akVs7CaloJets)


process.akVs2PFJetSequence = cms.Sequence(process.akVs2PFJetSequence_data)


process.akVs3CaloJetSequence_data = cms.Sequence(process.akVs3Calocorr+process.akVs3CaloJetTracksAssociatorAtVertex+process.akVs3CaloJetBtagging+process.akVs3CalopatJetsWithBtagging+process.akVs3CaloJetAnalyzer)


process.akVs5PFJetSequence_mc = cms.Sequence(process.akVs5PFmatch+process.akVs5PFparton+process.akVs5PFcorr+process.akVs5PFPatJetFlavourIdLegacy+process.akVs5PFJetTracksAssociatorAtVertex+process.akVs5PFJetBtagging+process.akVs5PFpatJetsWithBtagging+process.akVs5PFJetAnalyzer)


process.akVs5CaloJetBtagging = cms.Sequence(process.akVs5CaloJetBtaggingIP+process.akVs5CaloJetBtaggingSV+process.akVs5CaloJetBtaggingNegSV)


process.akPu3CaloJetSequence_mc = cms.Sequence(process.akPu3Calomatch+process.akPu3Caloparton+process.akPu3Calocorr+process.akPu3CaloPatJetFlavourIdLegacy+process.akPu3CaloJetTracksAssociatorAtVertex+process.akPu3CaloJetBtagging+process.akPu3CalopatJetsWithBtagging+process.akPu3CaloJetAnalyzer)


process.akVs4CaloJetBtagging = cms.Sequence(process.akVs4CaloJetBtaggingIP+process.akVs4CaloJetBtaggingSV+process.akVs4CaloJetBtaggingNegSV)


process.akVs2CaloJetSequence_jec = cms.Sequence(process.akVs2CaloJetSequence_mc)


process.akPu2CaloJetBtagging = cms.Sequence(process.akPu2CaloJetBtaggingIP+process.akPu2CaloJetBtaggingSV+process.akPu2CaloJetBtaggingNegSV)


process.akVs3CaloJetSequence_mc = cms.Sequence(process.akVs3Calomatch+process.akVs3Caloparton+process.akVs3Calocorr+process.akVs3CaloPatJetFlavourIdLegacy+process.akVs3CaloJetTracksAssociatorAtVertex+process.akVs3CaloJetBtagging+process.akVs3CalopatJetsWithBtagging+process.akVs3CaloJetAnalyzer)


process.akVs3CaloJetSequence_mix = cms.Sequence(process.akVs3CaloJetSequence_mc)


process.akPu2PFJetSequence = cms.Sequence(process.akPu2PFJetSequence_data)


process.akPu5CaloJetSequence_data = cms.Sequence(process.akPu5Calocorr+process.akPu5CaloJetTracksAssociatorAtVertex+process.akPu5CaloJetBtagging+process.akPu5CalopatJetsWithBtagging+process.akPu5CaloJetAnalyzer)


process.akPu4CaloJetSequence_mix = cms.Sequence(process.akPu4CaloJetSequence_mc)


process.akPu2CaloJetSequence_mc = cms.Sequence(process.akPu2Calomatch+process.akPu2Caloparton+process.akPu2Calocorr+process.akPu2CaloPatJetFlavourIdLegacy+process.akPu2CaloJetTracksAssociatorAtVertex+process.akPu2CaloJetBtagging+process.akPu2CalopatJetsWithBtagging+process.akPu2CaloJetAnalyzer)


process.akVs4PFJetSequence_mix = cms.Sequence(process.akVs4PFJetSequence_mc)


process.akVs4PFJetSequence_data = cms.Sequence(process.akVs4PFcorr+process.akVs4PFJetTracksAssociatorAtVertex+process.akVs4PFJetBtagging+process.akVs4PFpatJetsWithBtagging+process.akVs4PFJetAnalyzer)


process.akVs5CaloJetSequence_data = cms.Sequence(process.akVs5Calocorr+process.akVs5CaloJetTracksAssociatorAtVertex+process.akVs5CaloJetBtagging+process.akVs5CalopatJetsWithBtagging+process.akVs5CaloJetAnalyzer)


process.akPu5PFJetSequence_mc = cms.Sequence(process.akPu5PFmatch+process.akPu5PFparton+process.akPu5PFcorr+process.akPu5PFPatJetFlavourIdLegacy+process.akPu5PFJetTracksAssociatorAtVertex+process.akPu5PFJetBtagging+process.akPu5PFpatJetsWithBtagging+process.akPu5PFJetAnalyzer)


process.akPu5CaloJetSequence = cms.Sequence(process.akPu5CaloJetSequence_data)


process.akVs4CaloJetSequence_data = cms.Sequence(process.akVs4Calocorr+process.akVs4CaloJetTracksAssociatorAtVertex+process.akVs4CaloJetBtagging+process.akVs4CalopatJetsWithBtagging+process.akVs4CaloJetAnalyzer)


process.akVs3CaloJetSequence = cms.Sequence(process.akVs3CaloJetSequence_data)


process.akVs3PFJetSequence_mc = cms.Sequence(process.akVs3PFmatch+process.akVs3PFparton+process.akVs3PFcorr+process.akVs3PFPatJetFlavourIdLegacy+process.akVs3PFJetTracksAssociatorAtVertex+process.akVs3PFJetBtagging+process.akVs3PFpatJetsWithBtagging+process.akVs3PFJetAnalyzer)


process.akPu3CaloJetSequence_data = cms.Sequence(process.akPu3Calocorr+process.akPu3CaloJetTracksAssociatorAtVertex+process.akPu3CaloJetBtagging+process.akPu3CalopatJetsWithBtagging+process.akPu3CaloJetAnalyzer)


process.akVs3PFJetSequence_mix = cms.Sequence(process.akVs3PFJetSequence_mc)


process.akPu2CaloJetSequence_jec = cms.Sequence(process.akPu2CaloJetSequence_mc)


process.akPu5PFJetSequence_mix = cms.Sequence(process.akPu5PFJetSequence_mc)


process.akPu3CaloJetSequence_jec = cms.Sequence(process.akPu3CaloJetSequence_mc)


process.akVs4CaloJetSequence_mc = cms.Sequence(process.akVs4Calomatch+process.akVs4Caloparton+process.akVs4Calocorr+process.akVs4CaloPatJetFlavourIdLegacy+process.akVs4CaloJetTracksAssociatorAtVertex+process.akVs4CaloJetBtagging+process.akVs4CalopatJetsWithBtagging+process.akVs4CaloJetAnalyzer)


process.akVs3CaloJetSequence_jec = cms.Sequence(process.akVs3CaloJetSequence_mc)


process.akPu2CaloJetSequence_data = cms.Sequence(process.akPu2Calocorr+process.akPu2CaloJetTracksAssociatorAtVertex+process.akPu2CaloJetBtagging+process.akPu2CalopatJetsWithBtagging+process.akPu2CaloJetAnalyzer)


process.akVs4PFJetSequence = cms.Sequence(process.akVs4PFJetSequence_data)


process.akVs5CaloJetSequence_mc = cms.Sequence(process.akVs5Calomatch+process.akVs5Caloparton+process.akVs5Calocorr+process.akVs5CaloPatJetFlavourIdLegacy+process.akVs5CaloJetTracksAssociatorAtVertex+process.akVs5CaloJetBtagging+process.akVs5CalopatJetsWithBtagging+process.akVs5CaloJetAnalyzer)


process.akPu2CaloJetSequence = cms.Sequence(process.akPu2CaloJetSequence_data)


process.akVs4CaloJetSequence_mix = cms.Sequence(process.akVs4CaloJetSequence_mc)


process.akVs5CaloJetSequence = cms.Sequence(process.akVs5CaloJetSequence_data)


process.akVs5PFJetSequence_data = cms.Sequence(process.akVs5PFcorr+process.akVs5PFJetTracksAssociatorAtVertex+process.akVs5PFJetBtagging+process.akVs5PFpatJetsWithBtagging+process.akVs5PFJetAnalyzer)


process.akVs5PFJetSequence_jec = cms.Sequence(process.akVs5PFJetSequence_mc)


process.akVs5PFJetSequence = cms.Sequence(process.akVs5PFJetSequence_data)


process.akVs3PFJetSequence_jec = cms.Sequence(process.akVs3PFJetSequence_mc)


process.akVs2CaloJetSequence = cms.Sequence(process.akVs2CaloJetSequence_data)


process.akVs5PFJetSequence_mix = cms.Sequence(process.akVs5PFJetSequence_mc)


process.akPu3CaloJetSequence_mix = cms.Sequence(process.akPu3CaloJetSequence_mc)


process.akPu2PFJetSequence_jec = cms.Sequence(process.akPu2PFJetSequence_mc)


process.akVs4PFJetSequence_jec = cms.Sequence(process.akVs4PFJetSequence_mc)


process.akVs5CaloJetSequence_mix = cms.Sequence(process.akVs5CaloJetSequence_mc)


process.akPu5CaloJetSequence_mc = cms.Sequence(process.akPu5Calomatch+process.akPu5Caloparton+process.akPu5Calocorr+process.akPu5CaloPatJetFlavourIdLegacy+process.akPu5CaloJetTracksAssociatorAtVertex+process.akPu5CaloJetBtagging+process.akPu5CalopatJetsWithBtagging+process.akPu5CaloJetAnalyzer)


process.akPu2PFJetSequence_mix = cms.Sequence(process.akPu2PFJetSequence_mc)


process.akVs4CaloJetSequence_jec = cms.Sequence(process.akVs4CaloJetSequence_mc)


process.akPu5PFJetSequence_jec = cms.Sequence(process.akPu5PFJetSequence_mc)


process.akPu2CaloJetSequence_mix = cms.Sequence(process.akPu2CaloJetSequence_mc)


process.akPu3CaloJetSequence = cms.Sequence(process.akPu3CaloJetSequence_data)


process.akPu5CaloJetSequence_mix = cms.Sequence(process.akPu5CaloJetSequence_mc)


process.akVs5CaloJetSequence_jec = cms.Sequence(process.akVs5CaloJetSequence_mc)


process.akPu5CaloJetSequence_jec = cms.Sequence(process.akPu5CaloJetSequence_mc)


process.akVs4CaloJetSequence = cms.Sequence(process.akVs4CaloJetSequence_data)


process.jetSequences = cms.Sequence(process.voronoiBackgroundPF+process.voronoiBackgroundCalo+process.akPu2CaloJets+process.akPu2PFJets+process.akVs2CaloJets+process.akVs2PFJets+process.akVs3CaloJets+process.akVs3PFJets+process.akVs4CaloJets+process.akVs4PFJets+process.akPu5CaloJets+process.akPu5PFJets+process.akVs5CaloJets+process.akVs5PFJets+process.highPurityTracks+process.offlinePrimaryVertices+process.akPu2CaloJetSequence+process.akVs2CaloJetSequence+process.akVs2PFJetSequence+process.akPu2PFJetSequence+process.akPu3CaloJetSequence+process.akVs3CaloJetSequence+process.akVs3PFJetSequence+process.akPu3PFJetSequence+process.akPu4CaloJetSequence+process.akVs4CaloJetSequence+process.akVs4PFJetSequence+process.akPu4PFJetSequence+process.akPu5CaloJetSequence+process.akVs5CaloJetSequence+process.akVs5PFJetSequence+process.akPu5PFJetSequence)


process.ana_step = cms.Path(process.hltfilter+process.hltanalysis+process.hltobject+process.centralityBin+process.hiEvtAnalyzer+process.jetSequences+process.ggHiNtuplizer+process.ggHiNtuplizerGED+process.hcalNoise+process.pfcandAnalyzer+process.HiForest+process.trackSequencesPbPb+process.hcalNoise)


process.pcollisionEventSelection = cms.Path(process.hltfilter+process.collisionEventSelectionAOD)


process.pHBHENoiseFilterResultProducer = cms.Path(process.hltfilter+process.HBHENoiseFilterResultProducer)


process.HBHENoiseFilterResult = cms.Path(process.hltfilter+process.fHBHENoiseFilterResult)


process.HBHENoiseFilterResultRun1 = cms.Path(process.hltfilter+process.fHBHENoiseFilterResultRun1)


process.HBHENoiseFilterResultRun2Loose = cms.Path(process.hltfilter+process.fHBHENoiseFilterResultRun2Loose)


process.HBHENoiseFilterResultRun2Tight = cms.Path(process.hltfilter+process.fHBHENoiseFilterResultRun2Tight)


process.HBHEIsoNoiseFilterResult = cms.Path(process.hltfilter+process.fHBHEIsoNoiseFilterResult)


process.pprimaryVertexFilter = cms.Path(process.hltfilter+process.primaryVertexFilter)


process.phfCoincFilter1 = cms.Path(process.hltfilter+process.hfCoincFilter)


process.phfCoincFilter2 = cms.Path(process.hltfilter+process.hfCoincFilter2)


process.phfCoincFilter3 = cms.Path(process.hltfilter+process.hfCoincFilter3)


process.phfCoincFilter4 = cms.Path(process.hltfilter+process.hfCoincFilter4)


process.phfCoincFilter5 = cms.Path(process.hltfilter+process.hfCoincFilter5)


process.pclusterCompatibilityFilter = cms.Path(process.hltfilter+process.clusterCompatibilityFilter)


process.superFilterPath = cms.Path(process.hltfilter+process.hltfilter)


process.pAna = cms.EndPath(process.skimanalysis)


process.DQMStore = cms.Service("DQMStore",
    LSbasedMode = cms.untracked.bool(False),
    collateHistograms = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(False),
    forceResetOnBeginLumi = cms.untracked.bool(False),
    referenceFileName = cms.untracked.string(''),
    verbose = cms.untracked.int32(0),
    verboseQT = cms.untracked.int32(0)
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring('particleFlowDisplacedVertexCandidate'),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(987346)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(98765432)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(6541321)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(654321)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(234567)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    famosSimHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(13579)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(88776655)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(6453209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(54525)
    ),
    saveFileName = cms.untracked.string(''),
    siTrackerGaussianSmearingRecHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(24680)
    ),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11223344)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('HiForestAOD.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerConstituentsMapBuilder = cms.ESProducer("CaloTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz')
)


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer")


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(18268),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.SteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAlong'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(18268)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.candidateBoostedDoubleSecondaryVertexAK8Computer = cms.ESProducer("CandidateBoostedDoubleSecondaryVertexESProducer",
    R0 = cms.double(0.8),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(0.7),
    weightFile = cms.FileInPath('RecoBTag/SecondaryVertex/data/BoostedDoubleSV_AK8_BDT.weights.xml.gz')
)


process.candidateBoostedDoubleSecondaryVertexCA15Computer = cms.ESProducer("CandidateBoostedDoubleSecondaryVertexESProducer",
    R0 = cms.double(1.5),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(1.3),
    weightFile = cms.FileInPath('RecoBTag/SecondaryVertex/data/BoostedDoubleSV_CA15_BDT.weights.xml.gz')
)


process.candidateCombinedMVAComputer = cms.ESProducer("CombinedMVAJetTagESProducer",
    calibrationRecord = cms.string('CombinedMVA'),
    jetTagComputers = cms.VPSet(cms.PSet(
        discriminator = cms.bool(True),
        jetTagComputer = cms.string('candidateJetProbabilityComputer'),
        variables = cms.bool(False)
    ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('candidateCombinedSecondaryVertexV2Computer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('softPFMuonComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('softPFElectronComputer'),
            variables = cms.bool(False)
        )),
    useCategories = cms.bool(False)
)


process.candidateCombinedSecondaryVertexComputer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertex', 
        'CombinedSVPseudoVertex', 
        'CombinedSVNoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidateCombinedSecondaryVertexSoftLeptonComputer = cms.ESProducer("CandidateCombinedSecondaryVertexSoftLeptonESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLepton', 
        'CombinedSVPseudoVertexNoSoftLepton', 
        'CombinedSVNoVertexNoSoftLepton', 
        'CombinedSVRecoVertexSoftMuon', 
        'CombinedSVPseudoVertexSoftMuon', 
        'CombinedSVNoVertexSoftMuon', 
        'CombinedSVRecoVertexSoftElectron', 
        'CombinedSVPseudoVertexSoftElectron', 
        'CombinedSVNoVertexSoftElectron'),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidateCombinedSecondaryVertexSoftLeptonCtagLComputer = cms.ESProducer("CandidateCombinedSecondaryVertexSoftLeptonCtagLESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLeptonCtagL', 
        'CombinedSVPseudoVertexNoSoftLeptonCtagL', 
        'CombinedSVNoVertexNoSoftLeptonCtagL', 
        'CombinedSVRecoVertexSoftMuonCtagL', 
        'CombinedSVPseudoVertexSoftMuonCtagL', 
        'CombinedSVNoVertexSoftMuonCtagL', 
        'CombinedSVRecoVertexSoftElectronCtagL', 
        'CombinedSVPseudoVertexSoftElectronCtagL', 
        'CombinedSVNoVertexSoftElectronCtagL'),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidateCombinedSecondaryVertexV2Computer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidateJetBProbabilityComputer = cms.ESProducer("CandidateJetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateJetProbabilityComputer = cms.ESProducer("CandidateJetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeCombinedMVAComputer = cms.ESProducer("CombinedMVAJetTagESProducer",
    calibrationRecord = cms.string('CombinedMVA'),
    jetTagComputers = cms.VPSet(cms.PSet(
        discriminator = cms.bool(True),
        jetTagComputer = cms.string('candidateNegativeOnlyJetProbabilityComputer'),
        variables = cms.bool(False)
    ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('candidateNegativeCombinedSecondaryVertexComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('negativeSoftPFMuonComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('negativeSoftPFElectronComputer'),
            variables = cms.bool(False)
        )),
    useCategories = cms.bool(False)
)


process.candidateNegativeCombinedSecondaryVertexComputer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertex', 
        'CombinedSVPseudoVertex', 
        'CombinedSVNoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(True),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(-2.0),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(True)
)


process.candidateNegativeCombinedSecondaryVertexSoftLeptonComputer = cms.ESProducer("CandidateCombinedSecondaryVertexSoftLeptonESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLepton', 
        'CombinedSVPseudoVertexNoSoftLepton', 
        'CombinedSVNoVertexNoSoftLepton', 
        'CombinedSVRecoVertexSoftMuon', 
        'CombinedSVPseudoVertexSoftMuon', 
        'CombinedSVNoVertexSoftMuon', 
        'CombinedSVRecoVertexSoftElectron', 
        'CombinedSVPseudoVertexSoftElectron', 
        'CombinedSVNoVertexSoftElectron'),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(True),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(-2.0),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(True)
)


process.candidateNegativeCombinedSecondaryVertexSoftLeptonCtagLComputer = cms.ESProducer("CandidateCombinedSecondaryVertexSoftLeptonCtagLESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLeptonCtagL', 
        'CombinedSVPseudoVertexNoSoftLeptonCtagL', 
        'CombinedSVNoVertexNoSoftLeptonCtagL', 
        'CombinedSVRecoVertexSoftMuonCtagL', 
        'CombinedSVPseudoVertexSoftMuonCtagL', 
        'CombinedSVNoVertexSoftMuonCtagL', 
        'CombinedSVRecoVertexSoftElectronCtagL', 
        'CombinedSVPseudoVertexSoftElectronCtagL', 
        'CombinedSVNoVertexSoftElectronCtagL'),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(True),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(-2.0),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(True)
)


process.candidateNegativeCombinedSecondaryVertexV2Computer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(True),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(-2.0),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(True)
)


process.candidateNegativeOnlyJetBProbabilityComputer = cms.ESProducer("CandidateJetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeOnlyJetProbabilityComputer = cms.ESProducer("CandidateJetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeTrackCounting3D2ndComputer = cms.ESProducer("CandidateNegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeTrackCounting3D3rdComputer = cms.ESProducer("CandidateNegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.candidatePositiveCombinedMVAComputer = cms.ESProducer("CombinedMVAJetTagESProducer",
    calibrationRecord = cms.string('CombinedMVA'),
    jetTagComputers = cms.VPSet(cms.PSet(
        discriminator = cms.bool(True),
        jetTagComputer = cms.string('candidatePositiveOnlyJetProbabilityComputer'),
        variables = cms.bool(False)
    ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('candidatePositiveCombinedSecondaryVertexComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('positiveSoftPFMuonComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('positiveSoftPFElectronComputer'),
            variables = cms.bool(False)
        )),
    useCategories = cms.bool(False)
)


process.candidatePositiveCombinedSecondaryVertexComputer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertex', 
        'CombinedSVPseudoVertex', 
        'CombinedSVNoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidatePositiveCombinedSecondaryVertexSoftLeptonComputer = cms.ESProducer("CandidateCombinedSecondaryVertexSoftLeptonESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLepton', 
        'CombinedSVPseudoVertexNoSoftLepton', 
        'CombinedSVNoVertexNoSoftLepton', 
        'CombinedSVRecoVertexSoftMuon', 
        'CombinedSVPseudoVertexSoftMuon', 
        'CombinedSVNoVertexSoftMuon', 
        'CombinedSVRecoVertexSoftElectron', 
        'CombinedSVPseudoVertexSoftElectron', 
        'CombinedSVNoVertexSoftElectron'),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidatePositiveCombinedSecondaryVertexSoftLeptonCtagLComputer = cms.ESProducer("CandidateCombinedSecondaryVertexSoftLeptonCtagLESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLeptonCtagL', 
        'CombinedSVPseudoVertexNoSoftLeptonCtagL', 
        'CombinedSVNoVertexNoSoftLeptonCtagL', 
        'CombinedSVRecoVertexSoftMuonCtagL', 
        'CombinedSVPseudoVertexSoftMuonCtagL', 
        'CombinedSVNoVertexSoftMuonCtagL', 
        'CombinedSVRecoVertexSoftElectronCtagL', 
        'CombinedSVPseudoVertexSoftElectronCtagL', 
        'CombinedSVNoVertexSoftElectronCtagL'),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidatePositiveCombinedSecondaryVertexV2Computer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidatePositiveOnlyJetBProbabilityComputer = cms.ESProducer("CandidateJetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidatePositiveOnlyJetProbabilityComputer = cms.ESProducer("CandidateJetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateSimpleSecondaryVertex2TrkComputer = cms.ESProducer("CandidateSimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.candidateSimpleSecondaryVertex3TrkComputer = cms.ESProducer("CandidateSimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.candidateTrackCounting3D2ndComputer = cms.ESProducer("CandidateTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.candidateTrackCounting3D3rdComputer = cms.ESProducer("CandidateTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.combinedMVAComputer = cms.ESProducer("CombinedMVAJetTagESProducer",
    calibrationRecord = cms.string('CombinedMVA'),
    jetTagComputers = cms.VPSet(cms.PSet(
        discriminator = cms.bool(True),
        jetTagComputer = cms.string('jetProbabilityComputer'),
        variables = cms.bool(False)
    ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('softPFMuonComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('softPFElectronComputer'),
            variables = cms.bool(False)
        )),
    useCategories = cms.bool(False)
)


process.combinedSecondaryVertexComputer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertex', 
        'CombinedSVPseudoVertex', 
        'CombinedSVNoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.combinedSecondaryVertexSoftLeptonComputer = cms.ESProducer("CombinedSecondaryVertexSoftLeptonESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertexNoSoftLepton', 
        'CombinedSVPseudoVertexNoSoftLepton', 
        'CombinedSVNoVertexNoSoftLepton', 
        'CombinedSVRecoVertexSoftMuon', 
        'CombinedSVPseudoVertexSoftMuon', 
        'CombinedSVNoVertexSoftMuon', 
        'CombinedSVRecoVertexSoftElectron', 
        'CombinedSVPseudoVertexSoftElectron', 
        'CombinedSVNoVertexSoftElectron'),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.combinedSecondaryVertexV2Computer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.doubleVertex2TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    minVertices = cms.uint32(2),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.ghostTrackComputer = cms.ESProducer("GhostTrackESProducer",
    calibrationRecords = cms.vstring('GhostTrackRecoVertex', 
        'GhostTrackPseudoVertex', 
        'GhostTrackNoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True)
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    appendToDataLabel = cms.string(''),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.impactParameterMVAComputer = cms.ESProducer("GenericMVAJetTagESProducer",
    calibrationRecord = cms.string('ImpactParameterMVA'),
    useCategories = cms.bool(False)
)


process.jetBProbabilityComputer = cms.ESProducer("JetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.jetProbabilityComputer = cms.ESProducer("JetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.l1GtTriggerMaskTechTrig = cms.ESProducer("L1GtTriggerMaskTechTrigTrivialProducer",
    TriggerMask = cms.vuint32(0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 
        0, 0, 0, 0)
)


process.negativeCombinedMVAComputer = cms.ESProducer("CombinedMVAJetTagESProducer",
    calibrationRecord = cms.string('CombinedMVA'),
    jetTagComputers = cms.VPSet(cms.PSet(
        discriminator = cms.bool(True),
        jetTagComputer = cms.string('negativeOnlyJetProbabilityComputer'),
        variables = cms.bool(False)
    ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('negativeCombinedSecondaryVertexComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('negativeSoftPFMuonComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('negativeSoftPFElectronComputer'),
            variables = cms.bool(False)
        )),
    useCategories = cms.bool(False)
)


process.negativeCombinedSecondaryVertexComputer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertex', 
        'CombinedSVPseudoVertex', 
        'CombinedSVNoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(True),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(-2.0),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(True)
)


process.negativeCombinedSecondaryVertexV2Computer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(True),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(-2.0),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(True)
)


process.negativeOnlyJetBProbabilityComputer = cms.ESProducer("JetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.negativeOnlyJetProbabilityComputer = cms.ESProducer("JetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.negativeSoftPFElectronByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(False)
)


process.negativeSoftPFElectronByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(True)
)


process.negativeSoftPFElectronByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('negative')
)


process.negativeSoftPFElectronComputer = cms.ESProducer("ElectronTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFElectron_TMVA420_BDT_74X_v1'),
    ipSign = cms.string('negative'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)


process.negativeSoftPFMuonByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(False)
)


process.negativeSoftPFMuonByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(True)
)


process.negativeSoftPFMuonByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('negative')
)


process.negativeSoftPFMuonComputer = cms.ESProducer("MuonTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFMuon_TMVA420_BDT_74X_v1'),
    ipSign = cms.string('negative'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)


process.negativeTrackCounting3D2ndComputer = cms.ESProducer("NegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.negativeTrackCounting3D3rdComputer = cms.ESProducer("NegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.positiveCombinedMVAComputer = cms.ESProducer("CombinedMVAJetTagESProducer",
    calibrationRecord = cms.string('CombinedMVA'),
    jetTagComputers = cms.VPSet(cms.PSet(
        discriminator = cms.bool(True),
        jetTagComputer = cms.string('positiveOnlyJetProbabilityComputer'),
        variables = cms.bool(False)
    ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('positiveCombinedSecondaryVertexComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('positiveSoftPFMuonComputer'),
            variables = cms.bool(False)
        ), 
        cms.PSet(
            discriminator = cms.bool(True),
            jetTagComputer = cms.string('positiveSoftPFElectronComputer'),
            variables = cms.bool(False)
        )),
    useCategories = cms.bool(False)
)


process.positiveCombinedSecondaryVertexComputer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVRecoVertex', 
        'CombinedSVPseudoVertex', 
        'CombinedSVNoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.positiveCombinedSecondaryVertexV2Computer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    calibrationRecords = cms.vstring('CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.positiveOnlyJetBProbabilityComputer = cms.ESProducer("JetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.positiveOnlyJetProbabilityComputer = cms.ESProducer("JetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.positiveSoftPFElectronByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(False)
)


process.positiveSoftPFElectronByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(True)
)


process.positiveSoftPFElectronByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('positive')
)


process.positiveSoftPFElectronComputer = cms.ESProducer("ElectronTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFElectron_TMVA420_BDT_74X_v1'),
    ipSign = cms.string('positive'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)


process.positiveSoftPFMuonByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(False)
)


process.positiveSoftPFMuonByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(True)
)


process.positiveSoftPFMuonByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('positive')
)


process.positiveSoftPFMuonComputer = cms.ESProducer("MuonTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFMuon_TMVA420_BDT_74X_v1'),
    ipSign = cms.string('positive'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(cms.PSet(
        Label = cms.untracked.string(''),
        NormalizationFactor = cms.untracked.double(1.0),
        Record = cms.string('SiStripApvGainRcd')
    ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.simpleSecondaryVertex2TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.simpleSecondaryVertex3TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.softPFElectronByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(False)
)


process.softPFElectronByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(True)
)


process.softPFElectronByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('any')
)


process.softPFElectronComputer = cms.ESProducer("ElectronTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFElectron_TMVA420_BDT_74X_v1'),
    ipSign = cms.string('any'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)


process.softPFMuonByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(False)
)


process.softPFMuonByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(True)
)


process.softPFMuonByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('any')
)


process.softPFMuonComputer = cms.ESProducer("MuonTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFMuon_TMVA420_BDT_74X_v1'),
    ipSign = cms.string('any'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackCounting3D2ndComputer = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.trackCounting3D3rdComputer = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.BTagRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('JetTagComputerRecord')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    ),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('75X_dataRun2_v12'),
    toGet = cms.VPSet()
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.L1GtTriggerMaskTechTrigRcdSource = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('L1GtTriggerMaskTechTrigRcd')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HERecalibration = cms.bool(False),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalibration = cms.bool(False),
    HcalReLabel = cms.PSet(
        RelabelHits = cms.untracked.bool(False),
        RelabelRules = cms.untracked.PSet(
            CorrectPhi = cms.untracked.bool(False),
            Eta1 = cms.untracked.vint32(1, 2, 2, 2, 3, 
                3, 3, 3, 3, 3, 
                3, 3, 3, 3, 3, 
                3, 3, 3, 3),
            Eta16 = cms.untracked.vint32(1, 1, 2, 2, 2, 
                2, 2, 2, 2, 3, 
                3, 3, 3, 3, 3, 
                3, 3, 3, 3),
            Eta17 = cms.untracked.vint32(1, 1, 2, 2, 3, 
                3, 3, 4, 4, 4, 
                4, 4, 5, 5, 5, 
                5, 5, 5, 5)
        )
    ),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    ),
    iLumi = cms.double(-1.0),
    toGet = cms.untracked.vstring('GainWidths')
)


process.jec = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0)
    ),
    timetype = cms.string('runnumber'),
    toGet = cms.VPSet(cms.PSet(
        connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
        label = cms.untracked.string('AK1PF_offline'),
        record = cms.string('JetCorrectionsRecord'),
        tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK1PF_offline')
    ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK1Calo_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK1Calo_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK2PF_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK2PF_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK2Calo_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK2Calo_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK3Calo_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK3Calo_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK3PF_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK3PF_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK4PF_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK4PF_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK4Calo_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK4Calo_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK5Calo_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK5Calo_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK5PF_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK5PF_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK6Calo_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK6Calo_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK6PF_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK6PF_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AKPu1PF_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu1PF_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AKPu1Calo_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu1Calo_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AKPu2PF_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu2PF_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AKPu2Calo_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu2Calo_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AKPu3Calo_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu3Calo_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AKPu3PF_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu3PF_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AKPu4PF_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu4PF_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AKPu4Calo_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu4Calo_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AKPu5Calo_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu5Calo_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AKPu5PF_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu5PF_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AKPu6Calo_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu6Calo_offline')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AKPu6PF_offline'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu6PF_offline')
        ))
)


process.uetable = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0)
    ),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    timetype = cms.string('runnumber'),
    toGet = cms.VPSet(cms.PSet(
        label = cms.untracked.string('UETable_PF'),
        record = cms.string('JetCorrectionsRecord'),
        tag = cms.string('UETableCompatibilityFormat_PF_v02_offline')
    ), 
        cms.PSet(
            label = cms.untracked.string('UETable_Calo'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('UETableCompatibilityFormat_Calo_v02_offline')
        ))
)


process.prefer("es_hardcode")

process.prefer("jec")

process.prefer("uetable")

process.AnomalousCellParameters = cms.PSet(
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999)
)

process.CondDBCommon = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    ),
    connect = cms.string('protocol://db/schema')
)

process.CondDBSetup = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(60),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    )
)

process.HcalReLabel = cms.PSet(
    RelabelHits = cms.untracked.bool(False),
    RelabelRules = cms.untracked.PSet(
        CorrectPhi = cms.untracked.bool(False),
        Eta1 = cms.untracked.vint32(1, 2, 2, 2, 3, 
            3, 3, 3, 3, 3, 
            3, 3, 3, 3, 3, 
            3, 3, 3, 3),
        Eta16 = cms.untracked.vint32(1, 1, 2, 2, 2, 
            2, 2, 2, 2, 3, 
            3, 3, 3, 3, 3, 
            3, 3, 3, 3),
        Eta17 = cms.untracked.vint32(1, 1, 2, 2, 3, 
            3, 3, 4, 4, 4, 
            4, 4, 5, 5, 5, 
            5, 5, 5, 5)
    )
)

process.HiCaloJetDefaults = cms.PSet(
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('CaloJet'),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)

process.HiCaloJetParameters = cms.PSet(
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.4),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('CaloJet'),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puPtMin = cms.double(10),
    puWidth = cms.double(0.8),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("towerMaker"),
    srcPVs = cms.InputTag("offlinePrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)

process.HiPFJetDefaults = cms.PSet(
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetPtMin = cms.double(10),
    jetType = cms.string('PFJet'),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)

process.HiPFJetParameters = cms.PSet(
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    addNegative = cms.bool(True),
    addNegativesFromCone = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doOutputJets = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    dropZeros = cms.bool(True),
    infinitesimalPt = cms.double(0.005),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetPtMin = cms.double(10),
    jetType = cms.string('PFJet'),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(-5, -4, -3, -2, -1, 
        0, 1, 2, 3, 4, 
        5),
    puWidth = cms.double(0.8),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)

process.JetIDParams = cms.PSet(
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    hoRecHitsColl = cms.InputTag("horeco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    useRecHits = cms.bool(True)
)

process.MultipleAlgoIteratorBlock = cms.PSet(
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False)
)

process.ParametrizedSubtractorBlock = cms.PSet(
    interpolate = cms.bool(False),
    subtractorName = cms.string('ParametrizedSubtractorBlock'),
    sumRecHits = cms.bool(False)
)

process.combinedSecondaryVertexCommon = cms.PSet(
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)

process.ghostTrackCommon = cms.PSet(
    charmCut = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig')
)

process.ghostTrackVertexRecoBlock = cms.PSet(
    vertexReco = cms.PSet(
        finder = cms.string('gtvr'),
        fitType = cms.string('RefitGhostTrackWithVertices'),
        maxFitChi2 = cms.double(10.0),
        mergeThreshold = cms.double(3.0),
        primcut = cms.double(2.0),
        seccut = cms.double(4.0)
    )
)

process.j2tParametersCALO = cms.PSet(
    coneSize = cms.double(0.4),
    extrapolations = cms.InputTag("trackExtrapolator"),
    trackQuality = cms.string('goodIterative'),
    tracks = cms.InputTag("generalTracks")
)

process.j2tParametersVX = cms.PSet(
    coneSize = cms.double(0.4),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(

)

process.softPFElectronCommon = cms.PSet(
    gbrForestLabel = cms.string('btag_SoftPFElectron_TMVA420_BDT_74X_v1'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)

process.softPFMuonCommon = cms.PSet(
    gbrForestLabel = cms.string('btag_SoftPFMuon_TMVA420_BDT_74X_v1'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)

process.trackPseudoSelectionBlock = cms.PSet(
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)

process.trackSelectionBlock = cms.PSet(
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)

process.variableJTAPars = cms.PSet(
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5)
)

process.vertexCutsBlock = cms.PSet(
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    )
)

process.vertexRecoBlock = cms.PSet(
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    )
)

process.vertexSelectionBlock = cms.PSet(
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)

process.vertexTrackSelectionBlock = cms.PSet(
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    )
)

