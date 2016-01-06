from CRABClient.UserUtilities import config
config = config()

#### JobType ####
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "step3_RAW2DIGI_L1Reco_RECO.py"

#### Data ####
config.Data.inputDataset = "/HIHighPt/dgulhan-HIHighPt_HIRun2011_HLT_HIFullTrack14-9a51de932e7ef7c4280ba90e9fc423d7/USER"
# config.Data.useParent = True
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1

config.Data.outLFNDirBase = "/store/user/velicanu/"
config.Data.publishDataName = "HIHighPt_HIRun2011_HLT_HIFullTrack14_RECO_753p1"

#### Site ####
config.Site.storageSite = "T2_US_MIT"
#config.Site.whitelist = ["T2_US_MIT","T2_US_CERN","T2_US_Vanderbilt"]
config.Site.whitelist = ["T2_US_MIT"]
#config.Site.blacklist = ["T0","T1"].
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']

