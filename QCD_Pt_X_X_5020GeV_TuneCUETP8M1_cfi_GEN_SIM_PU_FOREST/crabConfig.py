from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'Pythia8_Dijet_PTMINFLAG__pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_FOREST_758_PrivMC_v0'
config.section_('JobType')
config.JobType.psetName = '_PSETFLAG_'
config.JobType.pluginName = 'Analysis'
config.section_('Data')
config.Data.inputDataset = '_DATASETFLAG_'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.outputDatasetTag = 'Pythia8_Dijet_PTMINFLAG__pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_FOREST_758_PrivMC'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
# config.section_("Debug")
# config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
