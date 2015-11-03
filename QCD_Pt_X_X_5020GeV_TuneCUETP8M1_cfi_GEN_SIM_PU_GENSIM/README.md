# Embedded production 

Auto pt-hat usage (with pthat 15 for example):
```bash
./pthat.sh 15 crabConfig.py QCD_TuneCUETP8M1_cfi_GEN_SIM.py
cd QCD_TuneCUETP8M1_cfi_GEN_SIM_15
crab submit -c crabConfig.py
```

Required input: 
```bash
/Hydjet_Quenched_MinBias_5020GeV_750/HiFall15-75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/GEN-SIM
```

cmsDriver command:
```bash
cmsDriver.py QCD_Pt_600_800_8TeV_TuneCUETP8M1_cfi --conditions 75X_mcRun2_HeavyIon_v1 -s GEN,SIM --pileup_input das:/Hydjet_Quenched_MinBias_5020GeV_750/HiFall15-75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/GEN-SIM -n 10 --eventcontent FEVTDEBUG --scenario HeavyIons --pileup HiMixGEN --datatier GEN-SIM --beamspot MatchHI --fileout file:step1.root --pileup_dasoption "--limit 0" --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI,Configuration/DataProcessing/Utils.addMonitoring --no_exec
```



Nov 2, 2015

Dataset and location:

```bash
/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/velicanu-Pythia8_Dijet15_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_PrivMC-43ed3f93605b389f7e16c341cac43cd9/USER
/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/velicanu-Pythia8_Dijet30_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_PrivMC-88facff7c6a644c9abf3aa43fe2039e9/USER
/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/velicanu-Pythia8_Dijet50_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_PrivMC-e63a4177030cf1877d777a03f8360e0e/USER
/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/velicanu-Pythia8_Dijet80_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_PrivMC-282baa650b1997daa0dd8689f6a69785/USER
/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/velicanu-Pythia8_Dijet120_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_PrivMC-0ec5ca09bf4a25cb4bbd0b389cd6a67c/USER

# Stored at MIT
/mnt/hadoop/cms/store/user/velicanu/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV
```

Dataset expiry:

after the 2015 heavy ion run or when no longer needed

