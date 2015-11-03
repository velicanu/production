from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.section_('JobType')
config.JobType.psetName = '_PSETFLAG_'
config.JobType.pluginName = 'Analysis'
config.JobType.inputFiles = ['rssLimit']
config.JobType.outputFiles = ['step2.root']
config.section_('Data')
config.Data.inputDataset = '_DATASETFLAG_'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = True
config.Data.publishDataName = 'Pythia8_Dijet_PTMINFLAG__pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_DIGIRAW_PrivMC'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
