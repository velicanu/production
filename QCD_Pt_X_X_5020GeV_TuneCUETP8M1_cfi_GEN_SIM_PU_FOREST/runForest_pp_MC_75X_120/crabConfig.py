from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.section_('JobType')
config.JobType.psetName = 'runForest_pp_MC_75X.py'
config.JobType.pluginName = 'Analysis'
config.JobType.inputFiles = ['rssLimit','HI_PythiaCUETP8M1_5020GeV_753p1_v4.db']
config.JobType.outputFiles = ['HiForest.root']
config.section_('Data')
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-PYTHIA_QCD_120_TuneCUETP8M1_cfi_HI_RECODEBUG_5020GeV_20151010-5a929d7059f4b993e3119764421f52bf/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.publication = False
config.Data.unitsPerJob = 200
config.Data.publishDataName = 'HiForest_HIReco_PYTHIA_QCD120_TuneCUETP8M1_cfi_5020GeV_tag_HiForestPPSignalJECv3_dbJECv4'
# config.Data.outputDatasetTag = 'HiForest_HIReco_PYTHIA_QCD120_TuneCUETP8M1_cfi_5020GeV_tag_HiForestPPSignalJECv3_dbJECv4'
config.section_('User')
config.section_('Site')
#config.Site.whitelist = ['T2_CH_CERN']
config.Site.storageSite = 'T2_US_MIT'
config.section_("Debug")
# config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
