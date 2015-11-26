## Skim data from trigger 

Setup the environment as for forest (up one level readme)

### Run interactively

```bash
cmsRun skimTriggersEventContent.py maxEvents=100 inputFiles=root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_heavyions/velicanu/reco/HIPhysicsMinBiasUPC/v0/000/262/548/recoExpress_103.root outputFile=a
```

### Submit to cafqueue

```bash
# add --proxy=proxyforprod after you've ran this once, put your password, and see a new proxyforprod file in your directory
python submitskimTriggersEventContent.py -q cmscaf1nd -o /store/group/phys_heavyions/velicanu/eventsize/HIPhysicsMinBiasUPC/v2/ -i HIPhysicsMinBiasUPC.262548.list 
```
