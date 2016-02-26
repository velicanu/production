from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'RAWSkim_Pythia8_Dijet15_HLT_HIL1Centralityext70100MinimumumBiasHF1AND_v1'
config.section_('JobType')
config.JobType.psetName = 'skimRawHLT.py'
config.JobType.pluginName = 'Analysis'
# config.JobType.inputFiles = ['rssLimit']
# config.JobType.outputFiles = ['step2.root']
config.section_('Data')
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet15_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_DIGIRAW_757p1_PrivMC_v2-021e402d3455ab0dc5f18d54ade8599e/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 10
config.Data.totalUnits = -1
config.Data.publication = True
config.Data.outputDatasetTag = 'RAWSkim_Pythia8_Dijet15_HLT_HIL1Centralityext70100MinimumumBiasHF1AND_v1'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
