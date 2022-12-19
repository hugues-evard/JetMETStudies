#for dataset in "Cv1" "Dv1" "Dv2" "Ev1" "Fv1" "Gv1"
for dataset in "Cv1" "Dv1" "Dv2" "Ev1" "Fv1"
#for dataset in "Dv1" "Dv2" "Ev1"
#for dataset in "Cv1" "Dv2" "Ev1"
#for dataset in "Gv1"
do
    sh SubmitToCrab.sh /Muon/Run2022${dataset:0:1}-PromptReco-v${dataset:2:1}/MINIAOD muon_zmumu_2022"$dataset" 1 L1Study_ZToMuMu DataRun3
    sh SubmitToCrab.sh /Muon/Run2022${dataset:0:1}-PromptReco-v${dataset:2:1}/MINIAOD muon_mujet_2022$dataset 1 L1Study_SingleMuforJME DataRun3
    sh SubmitToCrab.sh /EGamma/Run2022${dataset:0:1}-PromptReco-v${dataset:2:1}/MINIAOD eg_zee_2022$dataset 1 L1Study_ZToEE DataRun3
    sh SubmitToCrab.sh /EGamma/Run2022${dataset:0:1}-PromptReco-v${dataset:2:1}/MINIAOD eg_photonjet_2022$dataset 1 L1Study_SinglePhotonforJME DataRun3
    #crab kill -d crabworkarea_02nov2022_pnfs_bugfix/crab_muon_zmumu_2022$dataset
    #crab kill -d crabworkarea_02nov2022_pnfs_bugfix/crab_muon_mujet_2022$dataset
    #crab kill -d crabworkarea_02nov2022_pnfs_bugfix/crab_eg_zee_2022$dataset
    #crab kill -d crabworkarea_02nov2022_pnfs_bugfix/crab_eg_photonjet_2022$dataset
done

sh SubmitToCrab.sh /SingleMuon/Run2022C-PromptReco-v1/MINIAOD muon_zmumu_2022Cv1_begin 1 L1Study_ZToMuMu DataRun3
sh SubmitToCrab.sh /SingleMuon/Run2022C-PromptReco-v1/MINIAOD muon_mujet_2022Cv1_begin 1 L1Study_SingleMuforJME DataRun3
