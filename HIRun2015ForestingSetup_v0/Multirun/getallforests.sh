#!/bin/bash
if [ $# -lt 1 ]
then
  echo "Usage: ./getallforests.sh <version>"
  exit 1
fi

base=262
rm ~/runall
for i in `/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select ls /store/group/phys_heavyions/velicanu/forest/Run2015E/ExpressPhysics/FEVT/${1}/000/$base/` 
do
  echo mkdir $base$i >> ~/runall 
  echo cd $base$i >> ~/runall 
  for j in `/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select ls /store/group/phys_heavyions/velicanu/forest/Run2015E/ExpressPhysics/FEVT/${1}/000/$base/$i`
  do
    echo cmsStage /store/group/phys_heavyions/velicanu/forest/Run2015E/ExpressPhysics/FEVT/${1}/000/$base/$i/$j . >> ~/runall 
  done 
  echo cd .. >> ~/runall
done

