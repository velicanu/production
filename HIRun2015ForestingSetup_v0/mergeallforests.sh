#!/bin/bash
if [ $# -lt 1 ]
then
  echo "Usage: ./mergeallforests.sh <tag>"
  exit 1
fi

rm ~/haddall
for i in `cat allruns` 
do
    echo "hadd -f ExpressHiForest_run${i}_.root ${i}/HiForest_*" >> ~/haddall
    echo "nevents=\`~/testforest/getentries.sh ExpressHiForest_run${i}_.root 1 | grep entries | awk '{print \$4}'\`" >> ~/haddall
    echo "echo \$nevents > n$i.txt" >> ~/haddall
    # echo "nevents=\`cat n$i.txt\`" >> ~/haddall
    echo "mv ExpressHiForest_run${i}_.root /data/velicanu/store/group/phys_heavyions/velicanu/forest/Run2015E/ExpressPhysics/Merged/ExpressHiForest_run${i}_\${nevents}_$1.root" >> ~/haddall
    echo "cmsStage /data/velicanu/store/group/phys_heavyions/velicanu/forest/Run2015E/ExpressPhysics/Merged/ExpressHiForest_run${i}_\${nevents}_$1.root /store/group/phys_heavyions/velicanu/forest/Run2015E/ExpressPhysics/Merged/ExpressHiForest_run${i}_\${nevents}_$1.root" >> ~/haddall
done

echo "echo \"################ Making Table ################\"" >> ~/haddall

for i in `cat allruns` 
do
  echo "nevents=\`cat n$i.txt\`" >> ~/haddall
  echo "nsize=\`ls -sh /data/velicanu/store/group/phys_heavyions/velicanu/forest/Run2015E/ExpressPhysics/Merged/ExpressHiForest_run${i}_\${nevents}_$1.root | awk '{print \$1}'\`" >> ~/haddall
  echo "echo \"| $i | HiForest | \$nevents | /store/group/phys_heavyions/velicanu/forest/Run2015E/ExpressPhysics/Merged/ExpressHiForest_run${i}_\${nevents}_$1.root | \$nsize | $1 |\""  >> ~/haddall
done
