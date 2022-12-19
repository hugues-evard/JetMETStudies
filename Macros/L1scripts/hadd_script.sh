#!/bin/sh

#for dir in "2022RunCv1_golden" "2022RunDv1_golden" "2022RunDv2_golden" "2022RunEv1_golden"
#for dir in "2022RunCv1_golden_ptcut3" "2022RunDv1_golden_ptcut3" "2022RunDv2_golden_ptcut3" "2022RunEv1_golden_ptcut3"
#for dir in "2022RunCv1_golden" "2022RunDv1_golden" "2022RunDv2_golden" "2022RunEv1_golden" "2022RunFv1_golden" "2022RunGv1"
#for dir in "2022RunGv1_golden"
for dir in "2022RunCv1_golden" "2022RunDv1_golden" "2022RunDv2_golden" "2022RunEv1_golden" "2022RunFv1_golden" "2022RunGv1_golden" "2018D"
#for dir in "2018D"
do
    hadd -f $dir/all_zmumu.root $dir/outputcondor_*ZToMuMu/*.root
    hadd -f $dir/all_zee.root $dir/outputcondor_ZToEE/*.root
    hadd -f $dir/all_mujet.root $dir/outputcondor_*MuonJet/*.root
    hadd -f $dir/all_photonjet.root $dir/outputcondor_PhotonJet/*.root

    #hadd -f $dir/all_zmumu.root $dir/output*.root
done

