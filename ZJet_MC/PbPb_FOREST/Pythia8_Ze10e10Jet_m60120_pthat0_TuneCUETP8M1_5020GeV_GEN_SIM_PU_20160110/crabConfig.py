from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'Pythia8_Ze10e10Jet_m60120_pthat0_TuneCUETP8M1_5020GeV_GEN_SIM_PU_20160110_FOREST_v11'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_PbPb_MIX_75X.py'
# config.JobType.maxMemoryMB = 3000 #default 2000
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['HiForestAOD.root']
config.section_('Data')
config.Data.inputDataset = '/Pythia8_Ze10e10Jet_m60120_pthat0_TuneCUETP8M1_5020GeV_GEN_SIM_PU_20160110/twang-Pythia8_Ze10e10Jet_m60120_pthat0_TuneCUETP8M1_5020GeV_step3_20160110-7268d177294694b3762cc51e73fbc45b/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 5
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'Pythia8_Ze10e10Jet_m60120_pthat0_TuneCUETP8M1_5020GeV_GEN_SIM_PU_20160110_FOREST_v11'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.blacklist = ['T2_US_Nebraska']
config.Site.storageSite = 'T2_US_MIT'
