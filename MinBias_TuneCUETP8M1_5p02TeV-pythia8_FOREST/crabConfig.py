from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.section_('JobType')
config.JobType.psetName = 'runForest_pp_MC_75X.py'
config.JobType.pluginName = 'Analysis'
# config.JobType.inputFiles = ['rssLimit']
# config.JobType.outputFiles = ['step2.root']
config.section_('Data')
config.Data.inputDataset = '/MinBias_TuneCUETP8M1_5p02TeV-pythia8/velicanu-MinBias_TuneCUETP8M1_5p02TeV-pythia8_RECO-293233b47c975745974a349c6c961571/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = True
config.Data.publishDataName = 'MinBias_TuneCUETP8M1_5p02TeV-pythia8_FOREST'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
