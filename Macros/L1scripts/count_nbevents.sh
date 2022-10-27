#!/bin/bash

: """
log_cat=`cat -n test_nbevents/outputcondor_ZToMuMu/log/scriptcondor_*.out | grep "There are"`
nb_total=`echo "$log_cat" | grep "events$" | awk '{ sum+=$3 } END { print sum }' - `
nb_unpre_initial=`echo "$log_cat" | grep "initially$" | awk '{ sum+=$3 } END { print sum }' - `
nb_unpre_filters=`echo "$log_cat" | grep "filters$" | awk '{ sum+=$3 } END { print sum }' - `
nb_unpre_select=`echo "$log_cat" | grep "ZMuMu_MuSelection$" | awk '{ sum+=$3 } END { print sum }' - `
nb_probe=`echo "$log_cat" | grep "ZMuMu_MuSelection$" | awk '{ sum+=$3 } END { print sum }' - `
nb_probe_qual12=`echo "$log_cat" | grep "ZMuMu_MuSelection$" | awk '{ sum+=$3 } END { print sum }' - `
nb_unpre_probe=`echo "$log_cat" | grep "ZMuMu_MuSelection$" | awk '{ sum+=$3 } END { print sum }' - `
nb_unpre_probe_qual12=`echo "$log_cat" | grep "ZMuMu_MuSelection$" | awk '{ sum+=$3 } END { print sum }' - `
"""

#log_cat=`cat -n test_nbevents/outputcondor_ZToMuMu/log/scriptcondor_*.out`
#cat test_nbevents/outputcondor_ZToMuMu/log/scriptcondor_*.out | grep "There are" | head #| cat -n - | awk '{ print $1" "$4 }' - | head
#cat -n test_nbevents/outputcondor_ZToMuMu/log/scriptcondor_*.out | awk '
#NR % 17 == 

total=""
unpre_initial=""
unpre_filters=""
unpre_select=""
probe=""
unpre_probe=""
probe_qual12=""
unpre_probe_qual12=""

# array: total, unpre_initial, unpre_filters, unpre_select, probe, unpre_probe, probe_qual12, unpre_probe_qual12
arr=( "" "" "" "" "" "" "" "" )

for f in `ls test_nbevents/outputcondor_ZToMuMu/log/scriptcondor_*.out`
do
    for i in ${!arr[@]}
    do
        l=$(($i+10)) 
        arr[$i]="${arr[$i]}
        "`sed -n "$l"p $f`
    done

done

for i in ${!arr[@]}
do
    arr[$i]=`echo "${arr[$i]}" | sed -e '/^[[:space:]]*$/d' - | awk '{ sum+=$3 } END { print sum }' - `
    #echo "${arr[$i]}"
done

echo "Total events:                            ${arr[0]}
Total unprefirable events:               ${arr[1]}
After first filters:                     ${arr[2]}
After MuSelection:                       ${arr[3]}
8 < probe_Pt < 25:                       ${arr[4]}
8 < probe_Pt < 25, unprefirable:         ${arr[5]}
8 < probe_Pt < 25, Qual12:               ${arr[6]}
8 < probe_Pt < 25, Qual12, unprefirable: ${arr[7]}"
