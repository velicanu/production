from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'zmumu_forest_v3'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_PbPb_MIX_75X.py'
config.JobType.maxMemoryMB = 3000 #default 2000
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['HiForestAOD.root']
config.section_('Data')
config.Data.inputDataset = '/Pythia8_Z30mumuJet_pthat30Norm_TuneCUETP8M1_5020GeV_Hydjet_MinBias_5020GeV_PrivMC/velicanu-Pythia8_Z30mumuJet_pthat30Norm_TuneCUETP8M1_5020GeV_cff_RECODEBUG_PrivMC_v1-3f9e938105987729b38aad4c8dc3c7c0/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'Pythia8_Z30mumuJet_pthat30Norm_TuneCUETP8M1_5020GeV_cff_FOREST_PrivMC_v3'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.blacklist = ['T2_US_Nebraska']
config.Site.storageSite = 'T2_US_MIT'
