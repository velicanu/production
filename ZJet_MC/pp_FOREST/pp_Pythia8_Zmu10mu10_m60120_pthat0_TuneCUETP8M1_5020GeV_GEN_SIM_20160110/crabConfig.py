from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'pp_Pythia8_Zmu10mu10_m60120_pthat0_TuneCUETP8M1_5020GeV_GEN_SIM_20160110_FOREST_v20'
config.section_('JobType')
config.JobType.psetName = 'runForestAOD_pp_MC_75X.py'
# config.JobType.maxMemoryMB = 3000 #default 2000
config.JobType.pluginName = 'Analysis'
# config.JobType.outputFiles = ['HiForestAOD.root']
config.section_('Data')
config.Data.inputDataset = '/pp_Pythia8_Zmu10mu10_m60120_pthat0_TuneCUETP8M1_5020GeV_GEN_SIM_20160110/twang-pp_Pythia8_Zmu10mu10_m60120_pthat0_TuneCUETP8M1_5020GeV_step3_20160110-9ef792173553b51399f38cbb33b2e565/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 5
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'pp_Pythia8_Zmu10mu10_m60120_pthat0_TuneCUETP8M1_5020GeV_GEN_SIM_20160110_FOREST_v20'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.blacklist = ['T2_US_Nebraska']
config.Site.storageSite = 'T2_US_MIT'
