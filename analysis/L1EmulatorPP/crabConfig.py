# from WMCore.Configuration import Configuration
# config = Configuration()
from CRABClient.UserUtilities import config
config = config()

config.section_('General')
config.General.transferOutputs = True
config.section_('JobType')
config.JobType.psetName = 'hlt_MC_stage1.py'
config.JobType.pluginName = 'Analysis'
# config.JobType.inputFiles = ['rssLimit']
config.JobType.maxMemoryMB = 3500 #default 2000
config.JobType.outputFiles = ['openHLT.root']
config.section_('Data')
config.Data.inputDataset = '/STARLIGHTProd/kjung-STARLIGHT_RAW_kjung_100kTest-237f2877ab396a5cd88221670e02a64e/USER'
config.Data.inputDBS = 'global'
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.publishDataName = 'Hydjet_Quenched_MinBias_5020GeV_L1Emulator_hlt_MC_stage1_v1'
config.Data.outLFNDirBase = '/store/group/phys_heavyions/velicanu/L1EmulatorTests/'
config.section_('User')
config.section_('Site')
# config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
# config.Site.whitelist = ['T2_US_MIT']
# config.Site.storageSite = 'T2_US_MIT'
config.Site.storageSite = 'T2_CH_CERN'

