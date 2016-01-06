if [ $# -ne 3 ]
then
  echo "Usage: ./pthat.sh <crab-filename> <python-filename> <dataset-list>"
  exit 1
fi

basename=`echo $2 | awk -F '.' '{print $1}'`

pthats=( 15 30 50 80 120 170 220 280 370 460 540 )

for i in `seq 0 10` 
  do
  rm -rf ${basename}_${pthats[$((i))]}  
  dataset=`cat $3 | head -n$((i+1)) | tail -n1`
  mkdir ${basename}_${pthats[$((i))]}  
  sed "s/_PTMINFLAG_/${pthats[$((i))]}/g ; s@_DATASETFLAG_@${dataset}@g ; s/_PSETFLAG_/${2}/g " $1 > ${basename}_${pthats[$((i))]}/$1
  cp $2 ${basename}_${pthats[$((i))]}
  echo done ${pthats[$((i))]} 
done
