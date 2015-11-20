for i in `cat runstoprocess ` 
do
  das_client.py --limit 0 --query "file dataset=/ExpressPhysics/Run2015E-Express-v1/FEVT run=$i" > raw$i.list
  cat raw$i.list | awk -F "/000/" '{print "root://eoscms//eos/cms"$1"/000/"$2}' > ExpressPhysics.$i.v4.list
done

for i in `cat runstoprocess` 
do
  python submitForestExpress.py -q cmscaf1nd -o /store/group/phys_heavyions/velicanu/forest/Run2015E/ExpressPhysics/FEVT/v4/ -i ExpressPhysics.$i.v4.list --proxy=proxyforprod
done
