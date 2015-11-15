# Embedded production 

Auto pt-hat usage (with pthat 15 for example):
```bash
./pthat.sh crabConfig.py step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_PU.py datasets.txt
cd step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_PU_15
crab submit -c crabConfig.py
```

Required input: see datasets.txt

cmsDriver command:
```bash
cmsDriver.py step2 --conditions 75X_mcRun2_HeavyIon_v7 --scenario HeavyIons --pileup_input das:/Hydjet_Quenched_MinBias_5020GeV_750/HiFall15-75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/GEN-SIM -n 2 --eventcontent FEVTDEBUGHLT -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:HIon,RAW2DIGI,L1Reco --beamspot NominalHICollision2015 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --pileup HiMix --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI --filein file:step1.root --fileout file:step2.root --pileup_dasoption --limit 0 --no_exec
```



Nov 2, 2015

Dataset and location:

```bash
UPDATE DATASET

UPDATE LOCATION
```

Dataset expiry:

after the 2015 heavy ion run or when no longer needed

