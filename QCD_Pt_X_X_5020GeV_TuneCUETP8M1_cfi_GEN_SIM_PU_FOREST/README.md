# production

How to make the dijet forest for all pthats:

## 1. Setup cmssw for forest, follow these instructions: https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiForestSetup#Setup_for_7_5_X 

## 2. In this production dir, copy the latest runForest configs:
```bash
cp $CMSSW_BASE/src/HeavyIonsAnalysis/JetAnalysis/test/runForestAOD_pp_MC_75X.py .
cp $CMSSW_BASE/src/HeavyIonsAnalysis/JetAnalysis/test/runForestAOD_PbPb_MIX_75X.py .
```

## 3. If we want simtracks, the make the following edit to the runForest config:
```python
#########################
# Track Analyzer                                                                       
#########################
process.load('HeavyIonsAnalysis.JetAnalysis.ExtraTrackReco_cff')
# process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_cff')

# Use this instead for track corrections
process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_Corr_cff')
```

*4. Edit the crabConfig.py for the current production, these lines specifically, make sure to KEEP \_PTMINFLAG_ which is automatically set later :
```python
config.General.requestName = 'Pythia8_Dijet_PTMINFLAG__pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_FOREST_758_PrivMC_v0'
config.Data.outputDatasetTag = 'Pythia8_Dijet_PTMINFLAG__pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_FOREST_758_PrivMC'
```

*5. run pthat.sh to create all the pthat production dirs
```bash
./pthat.sh crabConfig.py runForestAOD_PbPb_MIX_75X.py datasets.txt
```

*6. submit all the pthats to crab 
```bash
# setup crab first 
pthats=( 15 30 50 80 120 170 220 280 370 460 540 )
crab submit -c runForestAOD_PbPb_MIX_75X_15/crabConfig.py # run this alone to make sure the crab job starts ok, may ask for password
# if the above submitted succesfully and there's no problem then submit the rest with the following command
for i in `seq 1 10` ; do crab submit -c runForestAOD_PbPb_MIX_75X_${pthats[$((i))]}/crabConfig.py; done
```

*7. once the jobs finish running, merge them with hadd and document the samples on the HiForest twiki: https://twiki.cern.ch/twiki/bin/view/CMS/HiForest2015 
