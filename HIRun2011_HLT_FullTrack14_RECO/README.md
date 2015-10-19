# 2.76 TeV deleted skim reco production - HLT_HISinglePhoton20 HLT_HISinglePhoton30

Required input: 
```bash
/HIHighPt/dgulhan-HIHighPt_HIRun2011_HLT_HIFullTrack14-9a51de932e7ef7c4280ba90e9fc423d7/USER
```

cmsDriver command:
```bash
cmsDriver.py step3 --conditions auto:run1_data -s RAW2DIGI,L1Reco,RECO -n 2 --eventcontent RECO --scenario HeavyIons --datatier RECO --repacked --filein file:step2.root --fileout file:RECO.root --no_exec
```

currently submitted 581 jobs on what's currently done

Oct 16, 2015

Dataset and location:

```bash
/Hydjet1p8_TuneDrum_Quenched_MinBias_2760GeV/velicanu-HydjetMB_2076GeV_RECODEBUG_753p1-776179b16aca4791f871800c4d86d9a6/USER

/mnt/hadoop/cms/store/user/velicanu/Hydjet1p8_TuneDrum_Quenched_MinBias_2760GeV/HydjetMB_2076GeV_RECODEBUG_753p1/776179b16aca4791f871800c4d86d9a6
```

Dataset expiry:

after the 2015 heavy ion run or when no longer needed

