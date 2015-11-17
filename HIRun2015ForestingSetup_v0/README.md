# HIRun2015 Express Forest 

First iteration setup. 

Setup environment:
```bash
cmsrel CMSSW_7_5_5_patch2
cd CMSSW_7_5_5_patch2/src
cmsenv
# Main forest
git cms-merge-topic -u CmsHI:forest_$CMSSW_VERSION
# RCT unpacker
git clone git@github.com:richard-cms/L1UpgradeAnalyzer.git Analyzers/L1UpgradeAnalyzer
# Dfinder
git clone -b Dfinder https://github.com/taweiXcms/Bfinder.git
scram build -j8

cp HeavyIonsAnalysis/JetAnalysis/test/runForestAOD_PbPb_DATA_75X.py .
cp ./HeavyIonsAnalysis/JetAnalysis/test/dbFiles/HI_PythiaCUETP8M1_5020GeV_753p1_v3.db .
```

Customize forest config.

Run on this file:
```bash
/store/group/phys_heavyions/velicanu/store/t0streamer/Data/Express/000/261/396/RECO/step3_0.root
```



