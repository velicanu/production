# How to run the L1 Emulator

Step 1 - Setup CMSSW and compile:

```bash
cmsrel CMSSW_7_5_4
cd CMSSW_7_5_4/src
cmsenv
git cms-merge-topic -u 12183
git cms-merge-topic 12130 #this is Michael's PR number
git clone git@github.com:richard-cms/L1UpgradeAnalyzer.git Analyzers/L1UpgradeAnalyzer
scram build -j4             # set 4 to the number of cores your machine has, if you don't know leave it at 4
```

Step 2 - Get the basic trigger config:
```bash
mkdir -p L1TriggerConfig/L1GtConfigProducers/data/Luminosity/startup/
curl -O http://takashi.web.cern.ch/takashi/l1menu/L1Menu_CollisionsHeavyIons2015.v3.xml
mv L1Menu_CollisionsHeavyIons2015.v3.xml L1TriggerConfig/L1GtConfigProducers/data/Luminosity/startup/
hltGetConfiguration /users/krajczar/HI2015/7_5_X/HIon/V25 --full --offline --mc --unprescale --process TEST --globaltag 75X_mcRun2_HeavyIon_v6 --l1-emulator 'stage1,gt' --l1Xml L1Menu_CollisionsHeavyIons2015.v3.xml --output none --max-events 50 --input /store/user/twang/Hydjet_Quenched_MinBias_5020GeV_750/Hydjet_Quenched_MinBias_5020GeV_750_HiFall15_step2_20151106/0e34df14ec22ccb8b9e974a58aa5d325/step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_1000_1_X6L.root >  hlt_MC_stage1.py
```

Step 3 - Modify the trigger config: 
comment out the two blocks correspondign to these producers
```python
process.SiStripGainESProducer = cms.ESProducer( "SiStripGainESProducer",

process.SiStripQualityESProducer = cms.ESProducer( "SiStripQualityESProducer",
```
add these lines to the end of the config:
```python

### CUSTOMIZATION

process.load('L1Trigger.L1TCalorimeter.caloConfigStage1HI_cfi')
process.load('L1Trigger.L1TCalorimeter.caloStage1Params_HI_cfi')
process.caloStage1Params.regionPUSType = cms.string("zeroWall")

### nominal
### Use HI FW algos
process.caloConfig.fwVersionLayer2 = cms.uint32(1)
### PUS mask
process.caloStage1Params.jetRegionMask = cms.int32(0b0000100000000000010000)
### EG 'iso' (eta) mask
process.caloStage1Params.egEtaCut = cms.int32(0b0000001111111111000000)
### Single track eta mask
process.caloStage1Params.tauRegionMask = cms.int32(0b1111111100000011111111)
### Centrality eta mask
process.caloStage1Params.centralityRegionMask = cms.int32(0b0000111111111111110000)
### jet seed threshold for 3x3 step of jet finding
process.caloStage1Params.jetSeedThreshold = cms.double(0)
### HTT settings
process.caloStage1Params.etSumEtThreshold        = cms.vdouble(0., 7.) #ET,HT
### Minimum Bias thresholds
process.caloStage1Params.minimumBiasThresholds = cms.vint32(4,4,6,6)
### Centrality LUT
process.caloStage1Params.centralityLUTFile = cms.FileInPath("L1Trigger/L1TCalorimeter/data/centrality_extended_LUT_preRun.txt")


process.caloStage1Params.regionPUSType = cms.string("zeroWall")

# replace 'TEST' with the process name of your hlt config
process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")
process.hltbitanalysis.HLTProcessName = cms.string('TEST')
process.hltbitanalysis.hltresults = cms.InputTag('TriggerResults','','TEST' )
process.hltbitanalysis.l1GtReadoutRecord =cms.InputTag('simGtDigis','','TEST')
process.hltbitanalysis.l1GctHFBitCounts = cms.InputTag('gctDigis','','TEST')
process.hltbitanalysis.l1GctHFRingSums = cms.InputTag('gctDigis','','TEST')
process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)
process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)
process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("openHLT.root"))
                                   
                                   
process.L1UpgradeAnalyzer = cms.EDAnalyzer('l1t::L1UpgradeAnalyzer',
                                           InputLayer2Collection = cms.InputTag("simCaloStage1FinalDigis"),
                                           InputLayer2TauCollection = cms.InputTag("simCaloStage1FinalDigis:rlxTaus"),
                                           InputLayer2HFBitCountCollection = cms.InputTag("caloStage1Digis:HFBitCounts"),
                                           InputLayer2IsoTauCollection = cms.InputTag("simCaloStage1FinalDigis:isoTaus"),
                                           InputLayer2CaloSpareCollection = cms.InputTag("simCaloStage1FinalDigis:HFRingSums"),
                                           InputLayer1Collection = cms.InputTag("simRctUpgradeFormatDigis"),
                                           legacyRCTDigis = cms.InputTag("simRctDigis")
)
process.L1UpgradeAnalyzerPath = cms.EndPath(process.L1UpgradeAnalyzer)
```

Step 4 - Run:

```bash
cmsRun hlt_MC_stage1.py
```

