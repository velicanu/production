
## How to run RECO on RAW files

```bash
cmsrel CMSSW_7_5_7_patch1
cd CMSSW_7_5_7_patch1/src
cmsenv
git cms-addpkg Configuration/DataProcessing
scram build -j8
cd Configuration/DataProcessing/test/
git clone git@github.com:velicanu/production.git

# you can look in run_CfgTest.sh to see different running configuration, I will show how to do Express PbPb on DAT
python RunExpressProcessing.py --scenario HeavyIonsRun2 --global-tag 75X_dataRun2_ExpressHI_v2 --lfn /some/path/ --fevt --alcareco TkAlMinBiasHI+SiStripCalMinBias
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

process.source = cms.Source("PoolSource",
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
