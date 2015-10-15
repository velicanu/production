# 2.76 TeV MB Hydjet production

Required input: 
```bash
/Hydjet1p8_TuneDrum_Quenched_MinBias_2760GeV/mnguyen-HydjetMB_2076GeV_740pre8_MCHI1_74_V3_53XBS_DIGI-RAW-357e79669a127c57ffb9feac23989f82/USER
```

cmsDriver command:
```bash
cmsDriver.py step3 --conditions auto:run1_mc_hi -s RAW2DIGI,L1Reco,RECO -n 2 --eventcontent RECODEBUG --scenario HeavyIons --datatier GEN-SIM-RECO --beamspot RealisticHI2011Collision --filein file:step2.root --fileout file:step3.root --no_exec
```

currently submitted 500 jobs of 50 events each as requested by Austin for tracking studies

Oct 10, 2015

Dataset location:

```bash
/mnt/hadoop/cms/store/user/velicanu/Hydjet1p8_TuneDrum_Quenched_MinBias_2760GeV/HydjetMB_2076GeV_RECODEBUG_753p1/776179b16aca4791f871800c4d86d9a6
```

Dataset expiry:

after the 2015 heavy ion run or when no longer needed

