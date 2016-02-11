from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'Pythia8_Dijet80_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_FOREST_758_PrivMC_vstest_v1'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_PbPb_MIX_75X.py'
config.JobType.pluginName = 'Analysis'
config.section_('Data')
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet80_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_758_PrivMC-3e72696a43b93eac877e11bff9ae8846/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.outputDatasetTag = 'Pythia8_Dijet80_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_FOREST_758_PrivMC_vstest_v1'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
# config.section_("Debug")
# config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
