if [ $# -ne 0 ]
then
  echo "Usage: ./run.sh"
  exit 1
fi


count=0
for i in `seq 1 8`
do
  num=$((count*23+23))
  for i in `head -n${num} 261445.txt | tail -n23`
  do
    sed "s@_inputfileflag_@${i}@g ; s@_outputfileflag_@OpenHLT_Lumi${count}.root@g " openHLTfromStreamer.py > run${count}.py
    cmsRun run${count}.py &> run${count}.py.log &
    count=$((count+1))
    exit
  done

  while [ `ps | wc -l` -gt 10 ]
  do
    sleep 30
    
  done

done