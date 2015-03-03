#!/bin/bash
for i in {C4,C3,B2,D3,A3,D4,B4,B3,C4,A4,G5,C5,C4,G4,E4,C4,C4,G4,C4,F5,E5,E6,B5,C5,C4,G3,B3,C3,A3,B2,C2,G2};do play -qn synth 2 pluck $i& sleep .25; done