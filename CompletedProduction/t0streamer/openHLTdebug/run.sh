if [ $# -ne 1 ]
then
  # echo "Usage: ./run.sh </path/to/t0streamer/files>"
  # echo "Example: ./run.sh /store/t0streamer/Data/Express/000/261/396"
  echo "Usage: ./run.sh <inputlist>"
  echo "Example: ./run.sh 261445.txt"
  exit 1
fi

nfiles=`wc -l $1 | awk '{print $1}'`
ntimes=$((${nfiles}/23+1))
count=0
for i in `seq 1 ${ntimes}`
do
  num=$((count*23+23))
  for i in `head -n${num} $1 | tail -n23`
  do
    sed "s@_inputfileflag_@${i}@g ; s@_outputfileflag_@OpenHLT_Lumi${count}.root@g " openHLTfromStreamer.py > run${count}.py
    cmsRun run${count}.py &> run${count}.py.log &
    count=$((count+1))
  done

  while [ `ps | wc -l` -gt 10 ]
  do
    sleep 30
    
  done

done