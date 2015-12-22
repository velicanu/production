from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'zee_ppforest2_v6'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_pp_DATA_75X.py'
# config.JobType.maxMemoryMB = 3000 #default 2000
config.JobType.pluginName = 'Analysis'
config.section_('Data')
config.Data.inputDataset = '/HighPtPhoton30AndZ/azsigmon-Run2015E-PromptReco-AOD-DielectronSkim-262163-262273-v1-0d8b27ea5ddb998af72cec10f8b38257/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 20
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'PromptReco-AOD-DielectronSkim-262163-262273_ppFOREST_v5'
config.section_('User')
config.section_('Site')
# config.Site.whitelist = ['T2_US_MIT']
config.Site.blacklist = ['T2_US_Nebraska']
config.Site.storageSite = 'T2_US_MIT'
