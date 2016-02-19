# Instructions for running forest in CMSSW_7_5_8

1) One time setup cmmsw directory and check out the foresting branch
```bash
cmsrel CMSSW_7_5_8
cd CMSSW_7_5_8/src
cmsenv
git cms-merge-topic -u CmsHI:forest_CMSSW_7_5_8
git remote add cmshi git@github.com:CmsHI/cmssw.git
scram build -j8
```

2) From now on you just have to do the following before making forest from this directory.
```bash
cd CMSSW_7_5_8/src
cmsenv
```

If you want to pick up new foresting changes from the main branch
```bash
git pull cmshi forest_CMSSW_7_5_8
scram build -j8
```

3) Set up crab
```bash
voms-proxy-init --valid 168:00 -voms cms 
voms-proxy-info --all
source /cvmfs/cms.cern.ch/crab3/crab.sh
```

4) Prepare the crabConfig.py, I will use the one in this directory as an example

```python
# The following sets the name of the task in the crab monitoring page
config.General.requestName = 'Hydjet_Quenched_MinBias_5020GeV_758p2_FOREST-v28'

# The following sets which python flie to run, in our case run the foresting for PbPb MC
config.JobType.psetName = 'runForestAOD_PbPb_MIX_75X.py'

# This sets which dataset to run on, inputDBS will be phys03 for private samples and global (or commented out) for official
config.Data.inputDataset = '/Hydjet_Quenched_MinBias_5020GeV_750/velicanu-Hydjet_Quenched_MinBias_5020GeV_758p2_RECODEBUG_v0-374be93f4012329d5cdc100aeee72e76/USER'
config.Data.inputDBS = 'phys03'

# This sets how many events per job and how many total jobs to do, another common way to do it for data is FileBased or LumiBased splitting.
config.Data.splitting = "EventAwareLumiBased"
config.Data.unitsPerJob = 1000
config.Data.totalUnits = 100000

# This sets the ouptut directory ( will be your hadoop dir/head of input dataset (Hydjet_Quenched_MinBias_5020GeV_750)/outputDatasetTag
# Only EDM files get published (gensim, reco, etc) , forests do not
config.Data.publication = False
config.Data.outputDatasetTag = 'Hydjet_Quenched_MinBias_5020GeV_758p2_FOREST-v28'

# This tells crab where to or not to run. Whitelist forces the jobs to run at MIT.
# blacklist should prevent the jobs from running at that site although currently crab doesn't support this but may in the future. and 
# storageSite states where to put the output, usually MTI or CERN for what we'll be running. 
config.Site.whitelist = ['T2_US_MIT']
config.Site.blacklist = ['T2_US_Nebraska']
config.Site.storageSite = 'T2_US_MIT'
```

5) Now that the crabConfig is ready grab the latest runForest config if you did an update.
```bash
cp $CMSSW_BASE/src/HeavyIonsAnalysis/JetAnalysis/test/runForestAOD_PbPb_MIX_75X.py .
```
Edit it to run interactively on 10 events in one of the files from the dataset you plan to submit on. This is good to catch most run time errors and will also give you an idea how long the full production will run. 
```bash
cmsRun runForestAOD_PbPb_MIX_75X.py
```
If it runs without problem and the output looks reasonable then you are ready to submit.

6) Now submit the crab job.
```bash
crab submit -c crabConfig.py
```
after several minutes you can check the status
```
crab status -d crab_nameOfFolder
```
You should see something like Queued or Running. If you see SubmitFailed then you need to fix the crabConfig and try again. You can see the status of your jobs on a page like this, with your name in the place of mine:
dashb-cms-job.cern.ch/dashboard/templates/task-analysis/#user=Dragos+Velicanu&refresh=0&table=Mains&p=1&records=25&activemenu=2&pattern=&task=&from=&till=&timerange=lastWeek

7) Once the forest has completed running you can choose to merge it if the output is not too big, a merging setup I use is here:
https://github.com/velicanu/mergeforests



