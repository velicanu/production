if [ $# -ne 4 ]
then
  echo "Usage: ./pthat.sh <ptmin> <ptmax> <crab-filename> <python-filename>"
  exit 1
fi

basename=`echo $4 | awk -F '.' '{print $1}'`

mkdir ${basename}_${1}_${2}

sed "s/_PTMINFLAG_/${1}/g" $3 > tmp.crab
sed "s/_PTMAXFLAG_/${2}/g" tmp.crab > ${basename}_${1}_${2}/$3
rm tmp.crab

sed "s/_PTMINFLAG_/${1}/g" $4 > tmp.config
sed "s/_PTMAXFLAG_/${2}/g" tmp.config > ${basename}_${1}_${2}/${basename}_${1}_${2}.py
rm tmp.config

cp rssLimit ${basename}_${1}_${2}/
