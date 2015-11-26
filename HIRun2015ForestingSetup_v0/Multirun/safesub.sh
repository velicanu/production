
for i in `seq 0 207`
do
  ./run_${i}.sh &> job_${i}.log &
  numrunning=`ps | wc -l`
  echo Submitted $i , $numrunning running jobs
  while [ $numrunning -gt 44 ]
  do
    echo waiting for jobs to finish, sleep 30 seconds...
    sleep 30
    numrunning=`ps | wc -l`
  done
done
