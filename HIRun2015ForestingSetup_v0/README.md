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
cd HeavyIonsAnalysis/JetAnalysis/test/
```

Customize forest config.

Run on this file (pp):
```bash
/store/express/Run2015E/ExpressPhysics/FEVT/Express-v1/000/261/544/00000//22D08F8A-2E8D-E511-BF87-02163E011965.root
```

Apply this customization for L1 : https://twiki.cern.ch/twiki/bin/view/CMS/HiForestSetupWithUnpacker#Customization

Apply this customization for dfinder:
```python
AddCaloMuon = False
runOnMC = False
HIFormat = False
UseGenPlusSim = False
VtxLabel = "offlinePrimaryVerticesWithBS"
TrkLabel = "generalTracks"
from Bfinder.finderMaker.finderMaker_75X_cff import finderMaker_75X
finderMaker_75X(process, AddCaloMuon, runOnMC, HIFormat, UseGenPlusSim, VtxLabel, TrkLabel)
```
and add process.finder to ana_step path




