from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.section_('JobType')
config.JobType.psetName = 'QCD_TuneCUETP8M1_cfi_GEN_SIM_PTMINFLAG___PTMAXFLAG_.py'
config.JobType.pluginName = 'PrivateMC'
config.JobType.inputFiles = ['rssLimit']
config.JobType.outputFiles = ['step1.root']
config.section_('Data')
config.Data.primaryDataset = 'PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV'
config.Data.splitting = 'EventBased'
config.Data.publication = True
config.Data.unitsPerJob = 100
NJOBS = 3000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
# config.Data.publishDataName = 'QCD_TuneCUETP8M1_cfi_GEN_SIM'
config.Data.publishDataName = 'Pythia8_Dijet_PTMINFLAG__pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_PrivMC'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'