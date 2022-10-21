from datetime import datetime
import ROOT
import json
import os
import sys
import argparse



#In case you want to load an helper for C++ functions
ROOT.gInterpreter.Declare('#include "Helper.h"')
#Importing stuff from other python files
from helper import * 

def main():
    ###Arguments 
    parser = argparse.ArgumentParser(
        description='''L1 performance studies (turnons, scale/resolution/...)
        Based on ntuples produced from MINIAOD with a code adapted from:
        https://github.com/lathomas/JetMETStudies/blob/master/JMEAnalyzer/python/JMEanalysis.py''',
        usage='use "%(prog)s --help" for more information',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--maxEvents", dest="maxEvents", help="Maximum number of events to analyze. Default=-1 i.e. run on all events.", type=int, default=-1)
    parser.add_argument("-i", "--input", dest="inputFile", help="Input file", type=str, default='')
    parser.add_argument("-o", "--output", dest="outputFile", help="Output file", type=str, default='')
    parser.add_argument("-c", "--channel", dest="channel", help=
                        '''Set channel and analysis:
                        -PhotonJet: For L1 jet studies with events trigger with a SinglePhoton trigger
                        -MuonJet: For L1 jet studies with events trigger with a SingleMuon trigger
                        -ZToMuMu: For L1 muon studies with Z->mumu
                        -ZToEE: For L1 EG studies with Z->ee''', 
                        type=str, default='PhotonJet')
    args = parser.parse_args() 

    
    ###Define the RDataFrame from the input tree
    inputFile = args.inputFile
    if inputFile == '':
        if args.channel == 'PhotonJet':
            inputFile = '/user/lathomas/Public/L1Studies/PhotonJet.root'
        elif args.channel == 'MuonJet':
            inputFile = '/user/lathomas/Public/L1Studies/MuJet.root'
        elif args.channel == 'ZToMuMu':
            inputFile = '/user/lathomas/Public/L1Studies/ZToMuMu.root'
        elif args.channel == 'ZToEE':
            inputFile = '/user/lathomas/Public/L1Studies/ZToEE.root'


    df = ROOT.RDataFrame('jmeanalyzer/tree', inputFile)

    # filter events with run >= 359924
    #df = df.Filter("_runNb>=359924")

    nEvents = df.Count().GetValue()
    print('There are {} events'.format(nEvents))
    
    #Max events to run on 
    maxEvents = min(nEvents, args.maxEvents) if args.maxEvents >=0 else nEvents
    df = df.Range(0, maxEvents)
    #Next line to monitor event loop progress
    df = df.Filter('if(tdfentry_ %100000 == 0) {cout << "Event is  " << tdfentry_ << endl;} return true;')

    df = df.Filter('Flag_HBHENoiseFilter&&Flag_HBHENoiseIsoFilter&&Flag_goodVertices&&Flag_EcalDeadCellTriggerPrimitiveFilter&&Flag_BadPFMuonFilter&&Flag_BadPFMuonDzFilter')

    nbbins, runmin, runmax = RunNbLimits(df)
    
    if args.outputFile == '':
        args.outputFile = 'output_'+args.channel+'.root'
    out = ROOT.TFile(args.outputFile, "recreate")
    ####The sequence of filters/column definition starts here
    
    if args.channel not in ['PhotonJet','MuonJet','ZToMuMu','ZToEE']:
        print("Channel {} does not exist".format(args.channel))
        return 

    if args.channel == 'PhotonJet':
        df = SinglePhotonSelection(df) 
        
        df = CleanJets(df)
        
        df, histos_jets = AnalyzeCleanJets(df, 200, 100, nbbins, runmin, runmax) 
        
        df = PtBalanceSelection(df)
        
        df, histos_balance = AnalyzePtBalance(df, nbbins, runmin, runmax)
        
        df_report = df.Report()
        
        df, histos_hf = HFNoiseStudy(df, nbbins, runmin, runmax)
        #Selection is over. Now do some plotting
        
        for i in histos_jets:
            histos_jets[i].GetValue().Write()
            
        for i in histos_balance:
            histos_balance[i].GetValue().Write()
            
        for i in histos_hf:
            histos_hf[i].GetValue().Write()
        df_report.Print()

        
        
    if args.channel == 'MuonJet':
        df = MuonJet_MuonSelection(df) 
        
        df = CleanJets(df)
        
        df, histos_jets = AnalyzeCleanJets(df, 100, 50, nbbins, runmin, runmax) 
        
        df, histos_sum = EtSum(df)
        
        df_report = df.Report()
        
        #Selection is over. Now do some plotting
        
        for i in histos_jets:
            histos_jets[i].GetValue().Write()
            
        for i in histos_sum:
            histos_sum[i].GetValue().Write()
            
        df_report.Print()

    if args.channel == 'ZToEE':
        df = ZEE_EleSelection(df)
        df, histos = ZEE_Plots(df, nbbins, runmin, runmax)
        
        for i in histos:
            histos[i].GetValue().Write()

    if args.channel == 'ZToMuMu':
        df = ZMuMu_MuSelection(df)
        df, histos = ZMuMu_Plots(df, nbbins, runmin, runmax)

        for i in histos:
            histos[i].GetValue().Write()


if __name__ == '__main__':
    main()
