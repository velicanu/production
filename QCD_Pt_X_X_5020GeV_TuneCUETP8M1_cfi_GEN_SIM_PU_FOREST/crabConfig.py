from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.section_('JobType')
config.JobType.psetName = '_PSETFLAG_'
config.JobType.pluginName = 'Analysis'
config.JobType.inputFiles = ['rssLimit','HI_PythiaCUETP8M1_5020GeV_753p1_v4.db']
config.JobType.outputFiles = ['HiForest.root']
config.section_('Data')
config.Data.inputDataset = '_DATASETFLAG_'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.publication = False
config.Data.unitsPerJob = 200
config.Data.publishDataName = 'HiForest_HIReco_PYTHIA_QCD_PTMINFLAG__TuneCUETP8M1_cfi_5020GeV_tag_HiForestPPSignalJECv3_dbJECv4'
# config.Data.outputDatasetTag = 'HiForest_HIReco_PYTHIA_QCD_PTMINFLAG__TuneCUETP8M1_cfi_5020GeV_tag_HiForestPPSignalJECv3_dbJECv4'
config.section_('User')
config.section_('Site')
#config.Site.whitelist = ['T2_CH_CERN']
config.Site.storageSite = 'T2_US_MIT'
config.section_("Debug")
# config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
