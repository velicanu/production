from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'Neutrino_Hydjet_20160212_FOREST--v28'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_PbPb_MIX_75X.py'
# config.JobType.maxMemoryMB = 3000 #default 2000
config.JobType.pluginName = 'Analysis'
#config.JobType.outputFiles = ['HiForestAOD.root']
config.section_('Data')
config.Data.inputDataset = '/Neutrino_Hydjet/gsfs-Neutrino_Hydjet_RECO_20160212-00f741c0e90edc8e6e40dc7e8f945b31/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 4
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'Neutrino_Hydjet_20160212_FOREST--v28'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.blacklist = ['T2_US_Nebraska']
config.Site.storageSite = 'T2_US_MIT'
