#!/bin/bash

#cd /user/lathomas/L1Studies/SampleGeneration/SingleNeutrinoPU1/CMSSW_12_2_1/src
cd /user/hevard/CMSSW_12_4_8/src
cmsenv 
#cd /user/lathomas/MacrosforM/L1Studies/L1NtuplesAnalysis/SandBox
cd /user/hevard/CMSSW_12_4_8/src/JetMETStudies/Macros/L1scripts

python3 analyzel1.py --maxEvents -1 -i $1 -o $2 -c $3

