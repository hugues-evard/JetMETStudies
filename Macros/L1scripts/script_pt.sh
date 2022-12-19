#!/bin/bash
cmsenv

echo test2
root -l $1 <<-EOF
jmeanalyzer->cd()
tree->Scan("_lPt","abs(_lpdgId)==13&_lPt<10")
EOF

