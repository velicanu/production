from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'Hydjet_Quenched_MinBias_5020GeV_758p2_FOREST-v28'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_PbPb_MIX_75X.py'
# config.JobType.maxMemoryMB = 3000 #default 2000
config.JobType.pluginName = 'Analysis'
# config.JobType.outputFiles = ['HiForestAOD.root']
config.section_('Data')
config.Data.inputDataset = '/Hydjet_Quenched_MinBias_5020GeV_750/velicanu-Hydjet_Quenched_MinBias_5020GeV_758p2_RECODEBUG_v0-374be93f4012329d5cdc100aeee72e76/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "EventAwareLumiBased"
config.Data.unitsPerJob = 1000
config.Data.totalUnits = 100000
config.Data.publication = False
config.Data.outputDatasetTag = 'Hydjet_Quenched_MinBias_5020GeV_758p2_FOREST-v28'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.blacklist = ['T2_US_Nebraska']
config.Site.storageSite = 'T2_US_MIT'
