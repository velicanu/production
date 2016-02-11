from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'HIHardProbesPeripheral-HIRun2015-PromptReco-v1-FOREST-hcalnoise-v23'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_PbPb_DATA_75X.py'
# config.JobType.maxMemoryMB = 3000 #default 2000
config.JobType.pluginName = 'Analysis'
# config.JobType.outputFiles = ['HiForestAOD.root']
config.section_('Data')
config.Data.inputDataset = '/HIHardProbesPeripheral/HIRun2015-PromptReco-v1/AOD'
# config.Data.inputDBS = 'global'
config.Data.lumiMask = 'Cert_262548-263757_PromptReco_HICollisions15_JSON.txt'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'HIHardProbesPeripheral-HIRun2015-PromptReco-v1-FOREST-hcalnoise-v23'
config.section_('User')
config.section_('Site')
# config.Site.whitelist = ['T2_US_MIT']
config.Site.blacklist = ['T2_US_Nebraska']
config.Site.storageSite = 'T2_US_MIT'
