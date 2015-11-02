if [ $# -ne 3 ]
then
  echo "Usage: ./pthat.sh <pthat> <crab-filename> <python-filename>"
  exit 1
fi

basename=`echo $3 | awk -F '.' '{print $1}'`

mkdir ${basename}_${1}

sed "s/_PTMINFLAG_/${1}/g" $2 > ${basename}_${1}/$2

sed "s/_PTMINFLAG_/${1}/g" $3 > ${basename}_${1}/${basename}_${1}.py

cp rssLimit ${basename}_${1}/
