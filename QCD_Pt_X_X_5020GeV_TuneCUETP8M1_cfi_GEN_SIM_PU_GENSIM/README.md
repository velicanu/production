# Embedded production 

Required input: 
```bash

```

cmsDriver command:
```bash
cmsDriver.py QCD_Pt_600_800_8TeV_TuneCUETP8M1_cfi --conditions 75X_mcRun2_HeavyIon_v1 -s GEN,SIM --pileup_input das:/Hydjet_Quenched_MinBias_5020GeV_750/HiFall15-75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/GEN-SIM -n 10 --eventcontent FEVTDEBUG --scenario HeavyIons --pileup HiMixGEN --datatier GEN-SIM --beamspot MatchHI --fileout file:step1.root --pileup_dasoption "--limit 0" --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI,Configuration/DataProcessing/Utils.addMonitoring --no_exec
```



Nov 2, 2015

Dataset and location:

```bash
UPDATE DATASET

UPDATE LOCATION
```

Dataset expiry:

after the 2015 heavy ion run or when no longer needed

