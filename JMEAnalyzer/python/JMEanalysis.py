import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(20000) )  

from PhysicsTools.PatAlgos.tools.helpers import getPatAlgosToolsTask
patAlgosToolsTask = getPatAlgosToolsTask(process)


process.source = cms.Source("PoolSource",
                                fileNames = cms.untracked.vstring(
#                                    '/store/mc/PhaseIITDRSpring19MiniAOD/TTbar_14TeV_TuneCP5_Pythia8/MINIAODSIM/PU200_106X_upgrade2023_realistic_v3_ext1-v3/60000/E73765BC-F41D-6349-9394-2858D7CF81E1.root'
#'/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext2-v1/50000/EE271696-E60F-1743-8DB2-AC50FD899528.root'
#'/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/90000/EA38FF5C-D444-E811-BFA6-001E6779262E.root'
#'/store/mc/RunIIAutumn18MiniAOD/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/20000/0E772C3C-0A8F-8341-886E-21A550D8E283.root'
#'/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/90000/FD805C2C-92E0-4044-8061-770C77462EBC.root'
#'/store/mc/RunIIAutumn18MiniAOD/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/20000/435256CF-C2B1-4646-B28A-EE1A23DFD4DC.root'
#'/store/mc/RunIIAutumn18MiniAOD/TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/014F2D77-CD31-8348-B6CC-B09134F7E8E4.root'
'/store/mc/RunIISummer19UL17MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/FCBBCC59-954C-3143-9634-DF8825F76369.root'
#'/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/270000/FC03A7B5-7FC0-E811-99BA-B496910A9A2C.root'
#'/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-15to7000_TuneCP5_Flat_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v1/110000/EC1F3053-63C3-6245-814E-74759808D0C7.root'
        )
                            )

process.TFileService = cms.Service("TFileService", fileName = cms.string("outputttbarht.root") )

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag.globaltag="102X_dataRun2_v8"

process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")


process.load('Configuration.StandardSequences.Reconstruction_cff')


ISMC=False
runEra="MCUL2017"
UseSQLiteFiles=True


if "MC" in runEra:
    ISMC=True


EleVetoWP=''
EleTightWP=''
PhotonTightWP=''


if "Data2018" in runEra:
    if "2018D" in runEra: 
        process.GlobalTag.globaltag="102X_dataRun2_Prompt_v16" #2018D
    else:
        process.GlobalTag.globaltag="102X_dataRun2_v13" #2018ABC
    EleVetoWP='cutBasedElectronID-Fall17-94X-V1-veto'
    EleTightWP='mvaEleID-Fall17-iso-V2-wp90'
    PhotonTightWP='mvaPhoID-RunIIFall17-v1p1-wp80'

if "Data2017" in runEra:
    process.GlobalTag.globaltag="102X_dataRun2_v13" #2017      
    EleVetoWP='cutBasedElectronID-Fall17-94X-V1-veto'
    EleTightWP='mvaEleID-Fall17-iso-V1-wp90'
    PhotonTightWP='mvaPhoID-RunIIFall17-v1p1-wp80'

if "DataUL2017" in runEra:
    process.GlobalTag.globaltag="102X_dataRun2_v13" #2017      
    EleVetoWP='cutBasedElectronID-Fall17-94X-V1-veto'
    EleTightWP='mvaEleID-Fall17-iso-V1-wp90'
    PhotonTightWP='mvaPhoID-RunIIFall17-v1p1-wp80'


if "Data2016" in runEra:
    process.GlobalTag.globaltag="102X_dataRun2_v13" #2016
    EleVetoWP='cutBasedElectronID-Fall17-94X-V1-veto'
    EleTightWP='mvaEleID-Fall17-iso-V1-wp90'
    PhotonTightWP='mvaPhoID-RunIIFall17-v1p1-wp80'
    


if "MC2018" in runEra:
    process.GlobalTag.globaltag="102X_upgrade2018_realistic_v21" #2018     
    EleVetoWP='cutBasedElectronID-Fall17-94X-V1-veto'
    EleTightWP='mvaEleID-Fall17-iso-V2-wp90'
    PhotonTightWP='mvaPhoID-RunIIFall17-v1p1-wp80'

if "MC2017" in runEra:
    process.GlobalTag.globaltag="102X_mc2017_realistic_v8" #2017
    EleVetoWP='cutBasedElectronID-Fall17-94X-V1-veto'
    EleTightWP='mvaEleID-Fall17-iso-V1-wp90'
    PhotonTightWP='mvaPhoID-RunIIFall17-v1p1-wp80'

if "MC2016" in runEra:
    process.GlobalTag.globaltag="102X_mcRun2_asymptotic_v8" #2016
    EleVetoWP='cutBasedElectronID-Fall17-94X-V1-veto'
    EleTightWP='mvaEleID-Fall17-iso-V1-wp90'
    PhotonTightWP='mvaPhoID-RunIIFall17-v1p1-wp80'

if "MCUL2017" in runEra:
    process.GlobalTag.globaltag="102X_mc2017_realistic_v8" #2017
    EleVetoWP='cutBasedElectronID-Fall17-94X-V1-veto'
    EleTightWP='mvaEleID-Fall17-iso-V1-wp90'
    PhotonTightWP='mvaPhoID-RunIIFall17-v1p1-wp80'


process.jmeanalyzer = cms.EDAnalyzer('JMEAnalyzer',
                                     METFiltersPAT = cms.InputTag("TriggerResults::PAT"),
                                     METFiltersRECO = cms.InputTag("TriggerResults::RECO"),
                                     ECALBadCalibFilterUpdate=cms.InputTag("ecalBadCalibReducedMINIAOD2019Filter"),
                                     ECALLaserCorrFilterUpdate=cms.InputTag("ecalLaserCorrFilter"),
                                     ECALDeadCellBoundaryEnergyFilterUpdate=cms.InputTag("ecalDeadCellBoundaryEnergyFilterUpdate"),
                                     BadChargedCandidateFilterUpdate=cms.InputTag("BadChargedCandidateFilterUpdate"),
                                     Vertices=cms.InputTag("offlineSlimmedPrimaryVertices"),
                                     Jets=cms.InputTag("updatedPatJetsUpdatedJEC"),
#                                     JetsPuppi=cms.InputTag("updatedPatJetsUpdatedJECPuppi"),
                                     JetsPuppi=cms.InputTag("slimmedJetsPuppi"),
                                     pileupJetIdDiscriminantUpdate = cms.InputTag('pileupJetIdUpdate:fullDiscriminant'),
                                     pileupJetIdDiscriminantUpdate2017 = cms.InputTag('pileupJetIdUpdate2017:fullDiscriminant'),
                                     pileupJetIdDiscriminantUpdate2018 = cms.InputTag('pileupJetIdUpdate2018:fullDiscriminant'),
                                     pileupJetIdVariablesUpdate = cms.InputTag('pileupJetIdUpdate'),
                                     QuarkGluonLikelihood = cms.InputTag('QGTagger:qgLikelihood'),
                                     PFCandCollection=cms.InputTag("packedPFCandidates"),
                                     PULabel = cms.InputTag("slimmedAddPileupInfo"),
                                     Triggers = cms.InputTag("TriggerResults::HLT"),
                                     GenParticles=cms.InputTag("prunedGenParticles"),
                                     GenInfo=cms.InputTag("generator"),
                                     LHELabel = cms.InputTag("externalLHEProducer"),
                                     LHELabelALT = cms.InputTag("source"),
                                     PFMet=cms.InputTag("slimmedMETs"),
                                     PuppiMet=cms.InputTag("slimmedMETsPuppi"),
                                     Electrons=cms.InputTag("slimmedElectrons"),
                                     Muons=cms.InputTag("slimmedMuons"),
                                     Photons=cms.InputTag("slimmedPhotons"),
                                     JetPtCut=cms.double(100),
                                     ElectronPtCut=cms.double(20),
                                     ElectronVetoWorkingPoint=cms.string(EleVetoWP),
                                     ElectronTightWorkingPoint=cms.string(EleTightWP),
                                     MuonPtCut=cms.double(20),
                                     PhotonPtCut=cms.double(20),
                                     PhotonTightWorkingPoint=cms.string(PhotonTightWP),
                                     PFCandPtCut=cms.double(200),
                                     SaveTree=cms.bool(True),
                                     IsMC=cms.bool(ISMC),
                                     SavePUIDVariables=cms.bool(True),
                                     DropUnmatchedJets=cms.bool(False),
                                     DropBadJets=cms.bool(False),
#                                     Skim=cms.string("ZToEEorMuMu"),
                                     Skim=cms.string(""),
                                     Debug=cms.bool(False)
                              )

#Rerunning the ecalbadcalibration filter
from RecoMET.METFilters.ecalBadCalibFilter_cfi import ecalBadCalibFilter

baddetEcallistnew2019 = cms.vuint32(
    [872439604,872422825,872420274,872423218,872423215,872416066,872435036,872439336,
     872420273,872436907,872420147,872439731,872436657,872420397,872439732,872439339,
     872439603,872422436,872439861,872437051,872437052,872420649,872421950,872437185,
     872422564,872421566,872421695,872421955,872421567,872437184,872421951,872421694,
     872437056,872437057,872437313,872438182,872438951,872439990,872439864,872439609,
     872437181,872437182,872437053,872436794,872436667,872436536,872421541,872421413,
     872421414,872421031,872423083,872421439,872423224,872421438,872420397,872421566,
     872422589,872423096,872422717,872423214,872421415,872422311,872421926,872439469,
     872438567,872436659,872439731,872438311,872438078,872438438,872439601,872437951,
     872437950,872439729,872436792,872438183,872439468,872436663,872439728,872439727,
     872437694,872437823,872438845,872438973,872439354,872438566,872439733,872436530,
     872436655,872439600,872439730]
    )

process.ecalBadCalibReducedMINIAOD2019Filter = ecalBadCalibFilter.clone(
    EcalRecHitSource = cms.InputTag("reducedEgamma:reducedEERecHits"),
    ecalMinEt        = cms.double(50.),
    baddetEcal    = baddetEcallistnew2019,
    taggingMode = cms.bool(True),
    debug = cms.bool(False)
    )

#Rerunning the laser correction filter
process.load('RecoMET.METFilters.ecalLaserCorrFilter_cfi')
process.ecalLaserCorrFilter = cms.EDFilter(
    "EcalLaserCorrFilter",
    EBRecHitSource = cms.InputTag("reducedEgamma:reducedEBRecHits"),
    EERecHitSource = cms.InputTag("reducedEgamma:reducedEERecHits"),
    EBLaserMIN     = cms.double(0.3),
    EELaserMIN     = cms.double(0.3),
    EBLaserMAX     = cms.double(5.0), #this was updated wrt default
    EELaserMAX     = cms.double(100.0), #this was updated wrt default
    EBEnegyMIN     = cms.double(10.0),
    EEEnegyMIN     = cms.double(10.0),
    taggingMode    = cms.bool(True), #updated wrt default
    Debug          = cms.bool(False)
    )

#Rerunning EcalDeadCellBoundaryEnergyFilter
from RecoMET.METFilters.EcalDeadCellBoundaryEnergyFilter_cfi import EcalDeadCellBoundaryEnergyFilter
process.ecalDeadCellBoundaryEnergyFilterUpdate=EcalDeadCellBoundaryEnergyFilter.clone(
    recHitsEB = cms.InputTag("reducedEgamma:reducedEBRecHits"),
    recHitsEE = cms.InputTag("reducedEgamma:reducedEERecHits"),
    cutBoundEnergyDeadCellsEE=cms.untracked.double(10),
    taggingMode    = cms.bool(True)
    )

#Rerunning BadChargedCandidateFilter
from RecoMET.METFilters.BadChargedCandidateFilter_cfi import BadChargedCandidateFilter 
process.BadChargedCandidateFilterUpdate=BadChargedCandidateFilter.clone(
    muons = cms.InputTag("slimmedMuons"),
    PFCandidates = cms.InputTag("packedPFCandidates"),
    taggingMode    = cms.bool(True)
)



import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes
process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
JSONfile = 'Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'
myLumis = LumiList.LumiList(filename = JSONfile).getCMSSWString().split(',')
#process.source.lumisToProcess.extend(myLumis)


#Updating JECs
JECsVersion=""
if "MC2018" in runEra:
    JECsVersion='Autumn18_V19_MC'
if "MC2017" in runEra:
    JECsVersion='Fall17_17Nov2017_V32_102X_MC'
if "MC2016" in runEra:
    JECsVersion='Summer16_07Aug2017_V11_MC'

if "Data2018" in runEra:
    JECsVersion='Autumn18_RunABCD_V19_DATA'
if "Data2017" in runEra:
    JECsVersion='Fall17_17Nov2017_V32_102X_DATA'
if "Data2016" in runEra:
    JECsVersion='Summer16_07Aug2017All_V11_DATA'



if "MCUL2017" in runEra:
    JECsVersion='Summer19UL17_V5_MC'
if "DataUL2017B" in runEra:
    JECsVersion='Summer19UL17_RunB_V5_DATA'
if "DataUL2017C" in runEra:
    JECsVersion='Summer19UL17_RunC_V5_DATA'
if "DataUL2017D" in runEra:
    JECsVersion='Summer19UL17_RunD_V5_DATA'
if "DataUL2017E" in runEra:
    JECsVersion='Summer19UL17_RunE_V5_DATA'
if "DataUL2017F" in runEra:
    JECsVersion='Summer19UL17_RunF_V5_DATA'



SQLiteFile='sqlite:'+JECsVersion+'.db'

TagForAK4CHSJet='JetCorrectorParametersCollection_'+JECsVersion+'_AK4PFchs'
TagForAK4PuppiJet='JetCorrectorParametersCollection_'+JECsVersion+'_AK4PFPuppi'

from CondCore.DBCommon.CondDBSetup_cfi import CondDBSetup


process.jec = cms.ESSource('PoolDBESSource',
                           CondDBSetup,
                           connect = cms.string(SQLiteFile),
                           toGet = cms.VPSet(
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string(TagForAK4CHSJet),
            label  = cms.untracked.string('AK4PFchs')
            ),
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string(TagForAK4PuppiJet),
            label  = cms.untracked.string('AK4PFPuppi')
            ) 
        )
                           )

# Add an ESPrefer to override JEC that might be available from the global tag
if UseSQLiteFiles:
    process.es_prefer_jec = cms.ESPrefer('PoolDBESSource', 'jec')
else:
    process.es_prefer_jec = cms.ESPrefer('PoolDBESSource', 'GlobalTag')


JERVersion=''

if "MC2018" in runEra:
    JERVersion='Autumn18_V7b_MC'
if "MC2017" in runEra:
    JERVersion='Fall17_V3b_MC'
if "MC2016" in runEra:
    JERVersion='Summer16_25nsV1b_MC'

if "Data2018" in runEra:
    JERVersion='Autumn18_V7b_DATA'
if "Data2017" in runEra:
    JERVersion='Fall17_V3b_DATA'
if "Data2016" in runEra:
    JERVersion='Summer16_25nsV1b_DATA'

if "MCUL2017" in runEra:
    JERVersion='Summer19UL17_JRV2_MC'
if "DataUL2017" in runEra:
    JERVersion='Summer19UL17_JRV2_DATA'


SQLiteFileJER='sqlite:'+JERVersion+'.db'


print SQLiteFileJER
process.jer = cms.ESSource("PoolDBESSource",
                           CondDBSetup,
                           toGet = cms.VPSet(
        cms.PSet(
            record = cms.string('JetResolutionRcd'),
            tag    = cms.string('JR_'+JERVersion+'_PtResolution_AK4PFchs'),
            label  = cms.untracked.string('AK4PFchs_pt')
            ),
        cms.PSet(
            record = cms.string('JetResolutionScaleFactorRcd'),
            tag    = cms.string('JR_'+JERVersion+'_SF_AK4PFchs'),
            label  = cms.untracked.string('AK4PFchs')
            ),
#        cms.PSet(                                                                                                                                                                                            
#            record = cms.string('JetResolutionRcd'),                                                                                                                                                         
#            tag    = cms.string('JR_'+JERVersion+'_PtResolution_AK4PFPuppi'),
#            label  = cms.untracked.string('AK4PFPuppi_pt')                                                                                                                                                   
#            ),                                                                                                                                                                                               
#        cms.PSet(                                                                                                                                                                                            
#            record = cms.string('JetResolutionScaleFactorRcd'),                                                                                                                                              
#            tag    = cms.string('JR_'+JERVersion+'_SF_AK4PFPuppi'),                                                                                                                                    
#            label  = cms.untracked.string('AK4PFPuppi')                                                                                                                                                      
#            ),                                                                                                                                                                                               
        ),
                           connect = cms.string(SQLiteFileJER)
                           )

if UseSQLiteFiles: 
    process.es_prefer_jer = cms.ESPrefer('PoolDBESSource', 'jer')
else:
    process.es_prefer_jer = cms.ESPrefer('PoolDBESSource', 'GlobalTag')


from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection

updateJetCollection(
    process,
    jetSource = cms.InputTag('slimmedJets'),
    labelName = 'UpdatedJEC',
    jetCorrections = ('AK4PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']), 'None')  
)

updateJetCollection(
    process,
    jetSource = cms.InputTag('slimmedJetsPuppi'),
    labelName = 'UpdatedJEC',
    postfix = 'Puppi',
    jetCorrections = ('AK4PFPuppi', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']), 'None') 
)
process.jecSequence = cms.Sequence(process.patJetCorrFactorsUpdatedJEC * process.updatedPatJetsUpdatedJEC * process.patJetCorrFactorsUpdatedJECPuppi * process.updatedPatJetsUpdatedJECPuppi)


#Update MET
from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD

#Recompute PFMET (with updated JECs)
runMetCorAndUncFromMiniAOD (
    process,
    isData = not ISMC
)



'''
#Rerunning PUPPI (standard approach, default tuning)
from PhysicsTools.PatAlgos.slimming.puppiForMET_cff import makePuppiesFromMiniAOD
makePuppiesFromMiniAOD( process, True );
#Set to false if you want to recompute PUPPI weights
process.puppiNoLep.useExistingWeights = True
process.puppi.useExistingWeights = True

#Recompute PUPPI MET (with updated JECs and possibly updated PUPPI weights)
runMetCorAndUncFromMiniAOD(process,
                           jetCollUnskimmed="updatedPatJetsUpdatedJECPuppi",
                           isData= not ISMC,
                           metType="Puppi",
                           postfix="Puppi",
                           jetFlavor="AK4PFPuppi",
                           reapplyJEC = False
                           )
'''

#Rerunning PUPPi with v14-Chihuahua tune
from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
process.ak4PuppiJets  = ak4PFJets.clone (src = 'puppi', doAreaFastjet = True, jetPtMin = 2.)

from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
addJetCollection(process,labelName = 'Puppi', jetSource = cms.InputTag('ak4PuppiJets'), algo = 'AK', rParam=0.4, genJetCollection=cms.InputTag('slimmedGenJets'), jetCorrections = ('AK4PFPuppi', ['L1FastJet', 'L2Relative', 'L3Absolute','L2L3Residual'], 'None'),pfCandidates = cms.InputTag('packedPFCandidates'),
                 pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
                 svSource = cms.InputTag('slimmedSecondaryVertices'),
                 muSource =cms.InputTag( 'slimmedMuons'),
                 elSource = cms.InputTag('slimmedElectrons'),
                 genParticles= cms.InputTag('prunedGenParticles'),
                 getJetMCFlavour=ISMC
)

process.patJetsPuppi.addGenPartonMatch = cms.bool(ISMC)
process.patJetsPuppi.addGenJetMatch = cms.bool(ISMC)

from CommonTools.PileupAlgos.customizePuppiTune_cff import UpdatePuppiTuneV14

patAlgosToolsTask.add(process.ak4PuppiJets)
UpdatePuppiTuneV14(process,ISMC)



#Recompute pile up ID
from RecoJets.JetProducers.PileupJetID_cfi import  _chsalgos_81x, _chsalgos_94x, _chsalgos_102x
process.load("RecoJets.JetProducers.PileupJetID_cfi")
process.pileupJetIdUpdate = process.pileupJetId.clone()
process.pileupJetIdUpdate.jets = cms.InputTag("updatedPatJetsUpdatedJEC")
process.pileupJetIdUpdate.inputIsCorrected = True
process.pileupJetIdUpdate.applyJec = False
process.pileupJetIdUpdate.vertexes = cms.InputTag("offlineSlimmedPrimaryVertices")
process.pileupJetIdUpdate.algos = cms.VPSet(_chsalgos_81x) 


process.pileupJetIdUpdate2017 = process.pileupJetId.clone()
process.pileupJetIdUpdate2017.jets = cms.InputTag("updatedPatJetsUpdatedJEC")
process.pileupJetIdUpdate2017.inputIsCorrected = True
process.pileupJetIdUpdate2017.applyJec = False
process.pileupJetIdUpdate2017.vertexes = cms.InputTag("offlineSlimmedPrimaryVertices")
process.pileupJetIdUpdate2017.algos = cms.VPSet(_chsalgos_94x)

process.pileupJetIdUpdate2018 = process.pileupJetId.clone()
process.pileupJetIdUpdate2018.jets = cms.InputTag("updatedPatJetsUpdatedJEC")
process.pileupJetIdUpdate2018.inputIsCorrected = True
process.pileupJetIdUpdate2018.applyJec = False
process.pileupJetIdUpdate2018.vertexes = cms.InputTag("offlineSlimmedPrimaryVertices")
process.pileupJetIdUpdate2018.algos = cms.VPSet(_chsalgos_102x)


#Compute QGL 
process.load('RecoJets.JetProducers.QGTagger_cfi')
process.QGTagger.srcJets          = cms.InputTag('updatedPatJetsUpdatedJEC')
process.QGTagger.jetsLabel        = cms.string('QGL_AK4PFchs')   



process.ApplyPatAlgos  = cms.Path(process.patAlgosToolsTask)
process.applyjecs =  cms.Path( process.jecSequence )
process.computepuppimet = cms.Path( process.puppiMETSequence  )
process.computepfmetanduncties = cms.Path( process.fullPatMetSequence )
process.computepuppimetanduncties = cms.Path( process.fullPatMetSequencePuppi)
process.rerunmetfilters = cms.Path( process.ecalBadCalibReducedMINIAOD2019Filter * process.ecalLaserCorrFilter * process.ecalDeadCellBoundaryEnergyFilterUpdate * process.BadChargedCandidateFilterUpdate ) 
process.computepuid = cms.Path(process.pileupJetIdUpdate )
process.computeqgl = cms.Path(process.QGTagger)
process.endpath = cms.EndPath( process.jmeanalyzer)


#
