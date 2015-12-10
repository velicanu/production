from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.section_('JobType')
config.JobType.psetName = 'Pythia8_Z30mumuJet_pthat30Norm_TuneCUETP8M1_5020GeV_cff_GEN_SIM.py'
config.JobType.pluginName = 'PrivateMC'
config.JobType.inputFiles = ['rssLimit']
config.JobType.outputFiles = ['step1.root']
config.section_('Data')
config.Data.outputPrimaryDataset = 'Pythia8_Z30mumuJet_pthat30Norm_TuneCUETP8M1_5020GeV_Hydjet_MinBias_5020GeV_PrivMC'
config.Data.splitting = 'EventBased'
config.Data.publication = True
config.Data.unitsPerJob = 100
NJOBS = 3000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
# config.Data.publishDataName = 'QCD_TuneCUETP8M1_cfi_GEN_SIM'
config.Data.outputDatasetTag = 'Pythia8_Z30mumuJet_pthat30Norm_TuneCUETP8M1_5020GeV_cff_GEN_SIM'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'