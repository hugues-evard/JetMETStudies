#!/bin/bash

cd /user/hevard/CMSSW_12_4_8/src/JetMETStudies/Macros/L1scripts
cmsenv 

python3 analyzel1.py --maxEvents -1 -i $1 -o $2 -c $3
