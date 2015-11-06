from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.section_('JobType')
config.JobType.psetName = 'hlt_DATA_stage1.py'
config.JobType.pluginName = 'Analysis'
# config.JobType.inputFiles = ['rssLimit']
config.JobType.outputFiles = ['openHLT.root']
config.section_('Data')
config.Data.inputDataset = '/Hydjet_Quenched_MinBias_5020GeV/StoreResults-HydjetMB_740pre8_MCHI2_74_V3_53XBS_DIGI_RAW_6da45e4e90741bc03dbd9aec5f36c050-v1/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
# config.Data.publishDataName = 'Pythia8_Dijet_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_DIGIRAW_PrivMC'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
