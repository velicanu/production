# 2.76 TeV deleted skim reco production - HLT_HISinglePhoton20 HLT_HISinglePhoton30

Required input: 
```bash
/HIHighPt/dgulhan-HIHighPt_HIRun2011_HLT_HISinglePhoton20_HISinglePhoton30-94b0666b91c951da4a167e1b3165750b/USER
```

cmsDriver command:
```bash
cmsDriver.py step3 --conditions auto:run1_data -s RAW2DIGI,L1Reco,RECO -n 2 --eventcontent RECO --scenario HeavyIons --datatier RECO --repacked --filein file:step2.root --fileout file:RECO.root --no_exec
```

currently submitted 581 jobs on what's currently done

Oct 16, 2015

Dataset and location:

```bash
/HIHighPt/velicanu-HIHighPt_HIRun2011_HLT_HISinglePhoton20_HISinglePhoton30_RECO_753p1-fd44351629dd155a25de2b4c109c824c/USER

/mnt/hadoop/cms/store/user/velicanu/HIHighPt/HIHighPt_HIRun2011_HLT_HISinglePhoton20_HISinglePhoton30_RECO_753p1/fd44351629dd155a25de2b4c109c824c
```

Dataset expiry:

after the 2015 heavy ion run or when no longer needed

