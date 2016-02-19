# Instructions for running forest in CMSSW_7_5_8

1.
One time setup cmmsw directory and check out the foresting branch
```bash
cmsrel CMSSW_7_5_8
cd CMSSW_7_5_8/src
cmsenv
git cms-merge-topic -u CmsHI:forest_CMSSW_7_5_8
git remote add cmshi git@github.com:CmsHI/cmssw.git
scram build -j8
```

2.
From now on you just have to do the following before making forest from this directory.
```bash
cd CMSSW_7_5_8/src
cmsenv
```

If you want to pick up new foresting changes from the main branch
```bash
git pull cmshi forest_CMSSW_7_5_8
scram build -j8
```

3.
Set up crab
```bash
voms-proxy-init --valid 168:00 -voms cms 
voms-proxy-info --all
source /cvmfs/cms.cern.ch/crab3/crab.sh
```

4. 
pre
