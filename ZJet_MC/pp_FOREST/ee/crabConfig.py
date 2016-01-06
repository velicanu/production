from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'Pythia8_Z30eeJet_pthat30Norm_TuneCUETP8M1_5020GeV_cff_ppFOREST_PrivMCjec_v8'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_pp_MC_75X.py'
config.JobType.maxMemoryMB = 3000 #default 2000
config.JobType.pluginName = 'Analysis'
config.section_('Data')
config.Data.inputDataset = '/Pythia8_Z30eeJet_pthat30Norm_TuneCUETP8M1_5020GeV_GEN_SIM/dgulhan-Pythia8_Z30eeJet_pthat30Norm_TuneCUETP8M1_5020GeV_RECODEBUG_758-eca985b12211699dc9125db438586ff6/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'Pythia8_Z30eeJet_pthat30Norm_TuneCUETP8M1_5020GeV_cff_ppFOREST_PrivMCjec_v8'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.blacklist = ['T2_US_Nebraska']
config.Site.storageSite = 'T2_US_MIT'
