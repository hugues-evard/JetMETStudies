#!/bin/bash
for run in 'C1' 'D1' 'D2' 'E1' 'F1' 'G1'
#for run in 'G1'
#for run in 'C1' 'D1' 'D2' 'E1' 'G1'
do
    for skim in "Muon","ZToMuMu" "Muon","SingleMuforJME" "EGamma","ZToEE" "EGamma","SinglePhotonforJME"
    #for skim in "Muon","SingleMuforJME"
    #for skim in "Muon","ZToMuMu" "EGamma","ZToEE" "EGamma","SinglePhotonforJME"
    do 
        IFS=","
        set $skim
        dir=`ls -d1 /pnfs/iihe/cms/store/user/hevard/$1/Run2022${run:0:1}_PromptReco_v${run:1:1}_DataRun3_L1Study_$2/* | tail -n 1`

        case $2 in
            "ZToMuMu")
                condor_skim="ZToMuMu"
                ;;

            "SingleMuforJME")
                condor_skim="MuonJet"
                ;;

            "ZToEE")
                condor_skim="ZToEE"
                ;;

            "SinglePhotonforJME")
                condor_skim="PhotonJet"
                ;;
        esac

        #case ${run:0:1} in
        #    "G")
        #        outdir="2022Run${run:0:1}v${run:1:1}"
        #        ;;
        #    *)
        #        outdir="2022Run${run:0:1}v${run:1:1}_golden"
        #
        #esac
        outdir="2022Run${run:0:1}v${run:1:1}_golden"

        ./submit.sh $condor_skim "$dir/*/*.root" $outdir/outputcondor_$condor_skim


    done
done

./submit.sh ZToMuMu "/pnfs/iihe/cms/store/user/hevard/SingleMuon/Run2022C_PromptReco_v1_DataRun3_L1Study_ZToMuMu/221214_155554/*/*.root" 2022RunCv1_golden/outputcondor_SingleMuon_ZToMuMu
./submit.sh MuonJet "/pnfs/iihe/cms/store/user/hevard/SingleMuon/Run2022C_PromptReco_v1_DataRun3_L1Study_SingleMuforJME/221214_155734/*/*.root" 2022RunCv1_golden/outputcondor_SingleMuon_MuonJet

#sh SubmitToCondor.sh MuonJet_2018D MuonJet /pnfs/iihe/cms/store/user/lathomas/SingleMuon/Run2018D_UL2018_MiniAODv2_v3_DataUL2018D_L1Study_SingleMuforJME/220923_115303/0000/\*.root
#sh SubmitToCondor.sh ZToMuMu_2018D ZToMuMu /pnfs/iihe/cms/store/user/lathomas/SingleMuon/Run2018D_UL2018_MiniAODv2_v3_DataUL2018D_L1Study_ZToMuMu/220923_114505/0000/\*.root
#sh SubmitToCondor.sh ZToEE_2018D ZToEE /pnfs/iihe/cms/store/user/lathomas/EGamma/Run2018D_UL2018_MiniAODv2_v2_DataRun3_L1Study_ZToEE/220913_203229/000\*/\*.root
#sh SubmitToCondor.sh PhotonJet_2018D PhotonJet /pnfs/iihe/cms/store/user/lathomas/EGamma/Run2018D_UL2018_MiniAODv2_v2_DataUL2018D_L1Study_SinglePhotonforJME/220923_120114/000\*/\*.root

#./submit.sh MuonJet "/pnfs/iihe/cms/store/user/lathomas/SingleMuon/Run2018D_UL2018_MiniAODv2_v3_DataUL2018D_L1Study_SingleMuforJME/220923_115303/0000/*.root" 2018D/outputcondor_MuonJet
#./submit.sh ZToMuMu "/pnfs/iihe/cms/store/user/lathomas/SingleMuon/Run2018D_UL2018_MiniAODv2_v3_DataUL2018D_L1Study_ZToMuMu/220923_114505/0000/*.root" 2018D/outputcondor_ZToMuMu
#./submit.sh ZToEE "/pnfs/iihe/cms/store/user/lathomas/EGamma/Run2018D_UL2018_MiniAODv2_v2_DataRun3_L1Study_ZToEE/220913_203229/000*/*.root" 2018D/outputcondor_ZToEE
#./submit.sh PhotonJet "/pnfs/iihe/cms/store/user/lathomas/EGamma/Run2018D_UL2018_MiniAODv2_v2_DataUL2018D_L1Study_SinglePhotonforJME/220923_120114/000*/*.root" 2018D/outputcondor_PhotonJet

