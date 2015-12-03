## HIRun2015 Express Forest 

First iteration setup. 

## Setup environment:
```bash
cmsrel CMSSW_7_5_5_patch4
cd CMSSW_7_5_5_patch4/src
cmsenv
# Main forest
git cms-merge-topic -u CmsHI:forest_$CMSSW_VERSION
# RCT unpacker
git clone git@github.com:richard-cms/L1UpgradeAnalyzer.git Analyzers/L1UpgradeAnalyzer
# Dfinder
git clone -b Dfinder https://github.com/taweiXcms/Bfinder.git
git clone git@github.com:velicanu/production.git
scram build -j8

# grab submit scripts
cp production/HIRun2015ForestingSetup_v0/* .
```

## Run interactively:
```bash
cmsRun runOpenHLT_pp_DATA_75X_Express.py outputFile=openHLT.root maxEvents=10 inputFiles=/store/express/Run2015E/ExpressPhysics/FEVT/Express-v1/000/262/163/00000/C4717393-ED8E-E511-9F65-02163E0120F9.root

cmsRun runForest_pp_DATA_75X_Express.py outputFile=test.root maxEvents=10 inputFiles=/store/express/Run2015E/ExpressPhysics/FEVT/Express-v1/000/262/163/00000/C4717393-ED8E-E511-9F65-02163E0120F9.root
```

## Submit one run to caf queue
```bash
python submitOpenHLTExpress.py -q cmscaf1nd -o /store/group/phys_heavyions/velicanu/openhlt/Run2015E/ExpressPhysics/FEVT/ -i ExpressPhysics.262163.v2.list

python submitForestExpress.py -q cmscaf1nd -o /store/group/phys_heavyions/velicanu/forest/Run2015E/ExpressPhysics/FEVT/v2/ -i ExpressPhysics.262163.v2.list --proxy=proxyforprod
```

## Submit all runs in 'runstoprocess' to caf queue
```bash
./suballruns.sh v6
```

##############################################################

## How to run RECO on streamer (raw) files

```bash
cmsrel CMSSW_7_5_7_patch1
cd CMSSW_7_5_7_patch1/src
cmsenv
git cms-addpkg Configuration/DataProcessing
scram build -j8
git clone git@github.com:velicanu/production.git
cp production/HIRun2015ForestingSetup_v0/submitRunExpressProcessingCfg.py Configuration/DataProcessing/test/
cd Configuration/DataProcessing/test/

# you can look in run_CfgTest.sh to see different running configuration, I will show how to do Express PbPb on DAT
python RunExpressProcessing.py --scenario HeavyIonsRun2 --global-tag 75X_dataRun2_ExpressHI_v2 --lfn /some/path/ --fevt --alcareco TkAlMinBiasHI+SiStripCalMinBias
```
This will generate a RunExpressProcessingCfg.py config, make the following changes:
```python
# replace process.source block with this to read the streamer dat files 
process.source = cms.Source("NewEventStreamFileReader",
                            fileNames = cms.untracked.vstring('/store/t0streamer/Data/HIExpress/000/262/548/run262548_ls0333_streamHIExpress_StorageManager.dat')
)
```
Now just cmsRun RunExpressProcessingCfg.py to test it/run it interactively

To submit to lxbatch you need to make more changes.
```python
# add this at the top
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing('analysis')
options.register ('isPP',
                  False,
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.bool,
                  "Flag if this is a pp simulation")
options.parseArguments()

# replace the relevant blocks with these three

process.source = cms.Source("NewEventStreamFileReader",
    fileNames = cms.untracked.vstring(options.inputFiles[0])
)

# in process.write_FEVT = cms.OutputModule("PoolOutputModule",
fileName = cms.untracked.string(options.outputFile),

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)
```

You can test if the changes are properly made by trying the follwoing:
```bash
RunExpressProcessingCfg.py outputFile=step3_0.root maxEvents=3 inputFiles=root://cms-xrd-global.cern.ch//eos/cms/store/t0streamer/Data/HIPhysicsMinBiasUPC/000/262/548/run262548_ls0118_streamHIPhysicsMinBiasUPC_StorageManager.dat
```

Now you're ready to submit, to do that:
```bash
# the second time you run this add --proxy=proxyforprod to the following command , also set the outputpath/username
python submitRunExpressProcessingCfg.py -q cmscaf1nd -o /store/group/phys_heavyions/YOURUSERNAME/reco/HIPhysicsMinBiasUPC/v0/ -i HIPhysicsMinBiasUPC.262548.list 
```

That's it! bjobs to check job status and look in the path for those  /store/group/phys_heavyions/YOURUSERNAME/reco/HIPhysicsMinBiasUPC/v0/
