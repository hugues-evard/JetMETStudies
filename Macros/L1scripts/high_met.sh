#!/bin/bash

#files=2022RunDv2_golden/outputcondor_MuonJet/log/scriptcondor_51.out 
#files="2022RunFv1_golden/outputcondor_MuonJet/log/scriptcondor_149.out 2022RunFv1_golden/outputcondor_MuonJet/log/scriptcondor_908.out"
files="2022Run?v?_golden/outputcondor_*MuonJet/log/scriptcondor_*.out 2022RunGv1/outputcondor_MuonJet/log/scriptcondor_*.out"
cat $files | awk '
    BEGIN { 
            print "runNb, eventNb, lumiBlock, MET, jetNb, pT, eta, phi, CHEF, NHEF, NEEF, CEEF, MUEF";
            runNb = 0;
            eventNb = 0;
            lumiBlock = 0;
            MET = 0;
            jetNb = 0;
            pT = 0;
            eta = 0;
            phi = 0;
            CHEF = 0;
            NHEF = 0;
            NEEF = 0;
            CEEF = 0;
            MUEF = 0;

            first_high_met_event = 1;
            first_jet_of_event = 1;
    }

    /High MET event/ { 
        if(first_high_met_event == 1) { 
            first_high_met_event = 0;
        }
        else { 
            print runNb", "eventNb", "lumiBlock", "MET", "jetNb", "pT", "eta", "phi", "CHEF", "NHEF", "NEEF", "CEEF", "MUEF;
            first_jet_of_event = 1;
        }
    }

    /runNb/ {runNb = $2};
    /eventNb/ {eventNb = $2};
    /lumiBlock/ {lumiBlock = $2};
    /MET/ {MET = $2};
    /nb of jets/ {jetNb = 0};

    /Jet #/ {
        if(first_jet_of_event == 1) {
            first_jet_of_event = 0;
            jetNb = 0;
        }
        else {
            print runNb", "eventNb", "lumiBlock", "MET", "jetNb", "pT", "eta", "phi", "CHEF", "NHEF", "NEEF", "CEEF", "MUEF;
            jetNb++;
        }
    }
    /pT/ {pT = $2};
    /eta/ {eta = $2};
    /phi/ {phi = $2};
    /CHEF/ {CHEF = $2};
    /NHEF/ {NHEF = $2};
    /NEEF/ {NEEF = $2};
    /CEEF/ {CEEF = $2};
    /MUEF/ {MUEF = $2};

    END {
        print runNb", "eventNb", "lumiBlock", "MET", "jetNb", "pT", "eta", "phi", "CHEF", "NHEF", "NEEF", "CEEF", "MUEF;
    }'  > high_met.csv
