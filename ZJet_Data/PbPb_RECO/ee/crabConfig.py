from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'zee_reco_timeslew_v4'
config.section_('JobType')
config.JobType.psetName = 'step3_RAW2DIGI_L1Reco_RECO_PU.py'
config.JobType.maxMemoryMB = 3500 #default 2000
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['step3.root']
config.section_('Data')
config.Data.inputDataset = '/Pythia8_Z30eeJet_pthat30Norm_TuneCUETP8M1_5020GeV_Hydjet_MinBias_5020GeV_PrivMC/velicanu-Pythia8_Z30eeJet_pthat30Norm_TuneCUETP8M1_5020GeV_cff_GEN_SIM_DIGIRAW_PrivMC_v1-021e402d3455ab0dc5f18d54ade8599e/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = True
config.Data.outputDatasetTag = 'Pythia8_Z30eeJet_pthat30Norm_TuneCUETP8M1_5020GeV_cff_RECODEBUG_PrivMC_v4'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.blacklist = ['T2_US_Nebraska']
config.Site.storageSite = 'T2_US_MIT'
