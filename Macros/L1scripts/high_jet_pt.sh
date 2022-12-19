#cat test_out.out | awk '
#cat 2022RunCv1_golden/outputcondor_SingleMuon_MuonJet/log/scriptcondor_1.out | awk '
#cat 2022Run?v?_golden/outputcondor_*Jet/log/scriptcondor_*.out | awk '
cat 2022Run?v?_golden/outputcondor_*Jet/log/scriptcondor_*.out | awk '
    BEGIN { 
            #print "runNb,\t\teventNb,\tlumiBlock,\tpT,\t\teta,\t\tphi,\t\tCHEF,\t\tNHEF,\t\tNEEF,\t\tCEEF,\t\tMUEF";
            print "runNb, eventNb, lumiBlock, idxL1jet, pT, eta, phi, CHEF, NHEF, NEEF, CEEF, MUEF";
            runNb = 0;
            eventNb = 0;
            lumiBlock = 0;
            L1idx = 0;
            pT = 0;
            eta = 0;
            phi = 0;
            CHEF = 0;
            NHEF = 0;
            NEEF = 0;
            CEEF = 0;
            MUEF = 0;
            N = 14;
            print_next = False;
    }

    /High pT clean Jet/ { N = 0 }

    { 
        switch(N) {
            case 0:
                runNb = 0;
                eventNb = 0;
                lumiBlock = 0;
                L1idx = 0;
                pT = 0;
                eta = 0;
                phi = 0;
                CHEF = 0;
                NHEF = 0;
                NEEF = 0;
                CEEF = 0;
                MUEF = 0;
                N++;
                break;

            case 1:
                runNb = $2;
                N++;
                break;

            case 2:
                eventNb = $2;
                N++;
                break;

            case 3:
                lumiBlock = $2;
                N++;
                break;

            case 4:
                L1idx = $4;
                N++;
                break;

            case 5:
                pT = $2;
                N++;
                break;

            case 6:
                eta = $2;
                N++;
                break;

            case 7:
                phi = $2;
                N++;
                break;

            case 8:
                CHEF = $2;
                N++;
                break;

            case 9:
                NHEF = $2;
                N++;
                break;

            case 10:
                NEEF = $2;
                N++;
                break;

            case 11:
                CEEF = $2;
                N++;
                break;

            case 12:
                MUEF = $2;
                print_next = True;
                #print runNb",\t\t"eventNb",\t"lumiBlock",\t\t"pT",\t"eta",\t"phi",\t"CHEF",\t"NHEF",\t"NEEF",\t"CEEF",\t"MUEF;
                print runNb", "eventNb", "lumiBlock", "L1idx", "pT", "eta", "phi", "CHEF", "NHEF", "NEEF", "CEEF", "MUEF;
                N++;
                break;
        }
    }' > high_pt_jets.csv
