# 2.76 TeV deleted skim reco production - HLT_HIFullTrack14

Required input: 
```bash
/HIHighPt/velicanu-HIHighPt_HIRun2011_HLT_HISinglePhoton20_HISinglePhoton30_RECO_753p1-fd44351629dd155a25de2b4c109c824c/USER
```

standard 75x foresting setup:
```
cmsrel CMSSW_7_5_3_patch1
cd CMSSW_7_5_3_patch1/src
cmsenv
git cms-merge-topic -u CmsHI:forest_$CMSSW_VERSION
scram build -j4
```

Oct 19, 2015

Dataset and location:

```bash
Forest datasets do not get published

/mnt/hadoop/cms/store/user/velicanu/HIHighPt/HIHighPt_HIRun2011_HLT_HISinglePhoton20_HISinglePhoton30_FOREST_753p1_v0/151019_172910/0000
```

Dataset expiry:

after the 2015 heavy ion run or when no longer needed

