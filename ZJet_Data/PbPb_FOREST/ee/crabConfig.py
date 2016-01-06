from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'zee_HIPhoton40AndZforestjec_v8'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_PbPb_DATA_75X.py'
# config.JobType.maxMemoryMB = 3000 #default 2000
config.JobType.pluginName = 'Analysis'
# config.JobType.outputFiles = ['HiForestAOD.root']
config.section_('Data')
config.Data.inputDataset = '/HIPhoton40AndZ/HIRun2015-ZEE-PromptReco-v1/AOD'
config.Data.lumiMask = 'json_PbPb_262548-263322.txt'
# config.Data.inputDBS = 'global'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'HIPhoton40AndZ_HIRun2015-ZEE-PromptReco_FORESTjec_v8'
config.section_('User')
config.section_('Site')
# config.Site.whitelist = ['T2_US_MIT']
config.Site.blacklist = ['T2_US_Nebraska']
config.Site.storageSite = 'T2_US_MIT'
