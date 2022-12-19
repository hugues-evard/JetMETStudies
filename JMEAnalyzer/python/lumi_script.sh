cwd=`pwd`
#for dir in `ls -d crabworkarea_02nov2022_pnfs_bugfix/* crabworkarea_04nov2022_pnfs_bugfix/* crabworkarea_14nov2022_pnfs_bugfix/*`
#do
#    cd $cwd
#    echo $dir
#    crab report -d $dir
#    cd $dir/results
#    brilcalc lumi -b "STABLE BEAMS" -c web -i processedLumis.json -u /fb > brilcalc_output.txt
#done

lumi_file=$cwd/golden_lumis_16dec.txt
#touch golden_lumis.txt
touch $lumi_file

#for dir in `ls -d crabworkarea_02nov2022_pnfs_bugfix/*/results crabworkarea_04nov2022_pnfs_bugfix/*/results crabworkarea_14nov2022_pnfs_bugfix/*/results`
for dir in `ls -d crabworkarea_14dec2022/*`
do
    cd $cwd
    echo $dir >> $lumi_file
    crab report -d $dir
    cd $dir/results
    brilcalc lumi -b "STABLE BEAMS" -c web -i processedLumis.json -u /fb > brilcalc_output.txt
    #cat $dir/brilcalc_output.txt >> $lumi_file
    cat brilcalc_output.txt >> $lumi_file
done
