# HIRun2015 Express Forest 

First iteration setup. 

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
```


