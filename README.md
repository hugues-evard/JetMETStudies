# JetMETStudies

```
cmsrel CMSSW_10_6_19_patch2
cd CMSSW_10_6_19_patch2/src
git cms-addpkg RecoMET/METFilters
git clone https://github.com/lathomas/JetMETStudies.git 
scram b -j4
```

To get the EGM scaling/smearing correction (enabled by default), the following is also needed, as instructed in: <br>
https://twiki.cern.ch/twiki/bin/viewauth/CMS/EgammaUL2016To2018
```
git cms-merge-topic jainshilpi:ULV1_backport10616_forUsers
git clone https://github.com/cms-egamma/EgammaPostRecoTools.git
mv EgammaPostRecoTools/python/EgammaPostRecoTools.py RecoEgamma/EgammaTools/python/.
git clone https://github.com/jainshilpi/EgammaAnalysis-ElectronTools.git -b UL2018 EgammaAnalysis/ElectronTools/data/
git cms-addpkg EgammaAnalysis/ElectronTools
```
N.B. You will get a conflict when trying to merge jainshilpi:ULV1_backport10616_forUsers but it is easy to solve.

Make sure you adapt the **runEra** string and the **UseSQLiteFiles** boolean in JMEanalysis.py. 
In general, when available, global tag should be preferred to SQLite files. For UL17, however, no global tag is currently available so one needs to rely on .db files. 

You can make test with a local input file currently on lxplus: 
'file:/afs/cern.ch/work/l/lathomas/public/qcdht1000to1500_1.root'

For that file, please set
```
runEra=MCUL2017
```
