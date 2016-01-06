from CRABClient.UserUtilities import config
config = config()

#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "runForestAOD_PbPb_DATA_75X.py"

#### Data ####
config.Data.inputDataset = "/HIHighPt/velicanu-HIHighPt_HIRun2011_HLT_HISinglePhoton20_HISinglePhoton30_RECO_753p1-fd44351629dd155a25de2b4c109c824c/USER"
# config.Data.useParent = True
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1

config.Data.outLFNDirBase = "/store/user/velicanu/"
config.Data.publishDataName = "HIHighPt_HIRun2011_HLT_HISinglePhoton20_HISinglePhoton30_FOREST_753p1_v0"

#### Site ####
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT","T2_US_CERN","T2_US_Vanderbilt"]
config.Site.whitelist = ["T2_US_MIT"]
#config.Site.blacklist = ["T0","T1"].
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']

