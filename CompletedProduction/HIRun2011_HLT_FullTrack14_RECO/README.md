# 2.76 TeV deleted skim reco production - HLT_HIFullTrack14

Required input: 
```bash
/HIHighPt/dgulhan-HIHighPt_HIRun2011_HLT_HIFullTrack14-9a51de932e7ef7c4280ba90e9fc423d7/USER
```

cmsDriver command:
```bash
cmsDriver.py step3 --conditions auto:run1_data -s RAW2DIGI,L1Reco,RECO -n 2 --eventcontent RECO --scenario HeavyIons --datatier RECO --repacked --filein file:step2.root --fileout file:RECO.root --no_exec
```

currently submitted 581 jobs on what's currently done

Oct 19, 2015

Dataset and location:

```bash
UPDATE DATASET

UPDATE LOCATION
```

Dataset expiry:

after the 2015 heavy ion run or when no longer needed

