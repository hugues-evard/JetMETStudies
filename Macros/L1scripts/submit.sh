#!/bin/bash

# usage: ./submit.sh channel "input" output
# input has to be in quotes to not automaticly expand when using wildcards

channel=$1
input=$2
output=$3
#echo "channel: $channel input: $input output: $output"

# array of valid channel
channel_array=("ZToMuMu" "ZToEE" "MuonJet" "PhotonJet")

# check that channel is correct
if [[ ! " ${channel_array[*]} " =~ " ${channel} " ]]; then
    # whatever you want to do when array doesn't contain value
    #echo "Error: channel \"$channel\" is invalid. Usage: ./submit.sh channel \"input\" output"
    echo "Error: channel \"$channel\" is invalid. Valid channel are:"
    echo "ZToMuMu ZToEE MuonJet PhotonJet"
    exit
fi

# set input/output var (default, unless set)
if [[ -z "$input" ]]; then
    case $channel in
        "MuonJet")
            input="/pnfs/iihe/cms/store/user/lathomas/*Muon*/Run2022*_DataRun3_L1Study_Single*forJME/220908*/*/*.root";;
        "PhotonJet")
            input="/pnfs/iihe/cms/store/user/lathomas/EGamma/Run2022*_DataRun3_L1Study_SinglePhotonforJME/220908*/*/*.root";;
        "ZToEE")
            input="/pnfs/iihe/cms/store/user/lathomas/EGamma*/*_PromptReco_v*_DataRun3_L1Study_ZToEE/220909*/*/*.root";;
        "ZToMuMu")
            input="/pnfs/iihe/cms/store/user/lathomas/*Muon*/*_PromptReco_v*_DataRun3_L1Study_ZToMuMu/220909*/*/*.root";;
        *)
            echo "Error: channel \"$channel\" is invalid. Valid channel are:"
            echo "ZToMuMu ZToEE MuonJet PhotonJet"
            exit
    esac

    echo "No input file provided, setting to default for $channel:"
    echo "$input"
fi

# check if input files exist
arr=($input)
if  test -f "${arr[0]}" ; then
    echo "Using input file(s):" 
    echo "$input"
else
    echo "Error: no files found using input \"$input\""
    exit
fi

# check if output exists, otherwise create it
if [[ -z "$output" ]]; then
    echo "No output directory provided, setting to default."
    output="outputcondor$channel"
fi
echo "Using output directory:"
echo $output

if [[ ! -d "$output" ]]; then
    echo "Output directory $output does not exist. Creating it"
    mkdir "$output"
    mkdir "$output/log"
fi
outfiles="$output/log/scriptcondor_\$(Process)"
# empty output
# submit

# print .sub source  to stdin, then pipe in condor
echo "executable = scriptcondor.sh
output = $outfiles.out
error = $outfiles.err
log = $outfiles.log

transfer_input_files = \$(filename)
arguments            = \$(filename) $output/output_\$(Process).root $channel

# File transfer behavior
#should_transfer_files = no
#when_to_transfer_output = ON_EXIT

# Resource requests
#request_cpus   = 4
request_memory = 100MB
request_disk   = 100MB

# Optional resource requests
#+xcount = 4            # Request 4 cores
#+maxMemory = 4000      # Request 4GB of RAM
#+maxWallTime = 120     # Request 2 hrs of wall clock time
#+remote_queue = "osg"  # Request the OSG queue

# Run job
queue filename matching files $input
#queue 100" | condor_submit -file -

#echo "condor_submit -dry-run -file $input output=$outfiles.out error=$outfiles.err log=$outfiles.log arguments=\"\$(filename) $output/output_\$(Process).root $channel\" condor.sub"
