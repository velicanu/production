from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.section_('JobType')
config.JobType.psetName = 'step3_RAW2DIGI_L1Reco_RECO.py'
config.JobType.pluginName = 'Analysis'
# config.JobType.inputFiles = ['rssLimit']
# config.JobType.outputFiles = ['step2.root']
config.section_('Data')
# config.Data.inputDataset = '/MinBias_TuneCUETP8M1_5p02TeV-pythia8/twang-MinBias_TuneCUETP8M1_5p02TeV_pythia8_pp502Fall15_MCRUN2_71_V1_v1_step2_CMSSW_7_4_15_20151105-792724e95bc6b3667ad91f57fcdd4eac/USER'
config.Data.inputDataset = '/Hydjet_Quenched_MinBias_5020GeV_750/twang-Hydjet_Quenched_MinBias_5020GeV_750_HiFall15_step2_20151106-0e34df14ec22ccb8b9e974a58aa5d325/USER'
# config.Data.inputDBS = 'phys03'
config.Data.inputDBS = 'global'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = True
config.Data.publishDataName = 'Hydjet_Quenched_MinBias_5020GeV_750_RECODEBUG_v0'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
