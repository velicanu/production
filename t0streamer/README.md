# HIRun2015 Streamer code

First set up forest as in https://github.com/velicanu/production/tree/master/HIRun2015ForestingSetup_v0

Then:

Submit job:
```bash
python submitForestStreamer.py -q cmscaf1nd -o /store/group/phys_heavyions/velicanu/PhysicsMinimumBias4/ -i 163.list --proxy=proxyforprod
```

This will attempt to run reco on the streamer, followed by a seperate cmsRun foresting job, and then will attempt to stage both. Even if the foresting step you will still get reco out


