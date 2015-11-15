cmsenv 75X 

to unpack:

```bash
cmsRun unpackT0Streamer.py
```

to get openHLT:

```bash
cmsRun openHLTfromStreamer.py
```

cmsDriver command used to generate RECO config: 
```bash
cmsDriver.py bubba  --conditions auto:run2_data -s RAW2DIGI,L1Reco,RECO --runUnscheduled  --process RECO --data  --eventcontent FEVT --scenario pp --datatier RECO --customise Configuration/DataProcessing/RecoTLR.customiseDataRun2Common_25ns -n -1 --no_exec --filein file:run261396_ls0002_streamExpress_StorageManager.root
```

to RECO:
```bash
cmsRun bubba_RAW2DIGI_L1Reco_RECO.py
```
