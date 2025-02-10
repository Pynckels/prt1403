#! /usr/bin/bash

set -x

../prt1403 -j TEST1   -y -u PRT1403 -s WIDE   -c GREEN -o testOut/test1.pdf testIn/test1.txt
../prt1403 -j PI      -y -u FRTRN77 -s SMALL  -c BLUE  -o testOut/test2.pdf testIn/test2.f77
../prt1403 -j TEST3   -y -u PRT1403 -s MEDIUM -c GRAY  -o testOut/test3.pdf testIn/test3.txt
../prt1403 -j BNCHMRK -y -u FRTRN90 -s SMALL  -c BLUE  -o testOut/test4_1.pdf testIn/test4.f90
../prt1403 -j BNCHMRK -y -u FRTRN90 -s SMALL  -c WHITE  -f FONT1403 -o testOut/test4_2.pdf testIn/test4.f90
../prt1403 -y -f '/usr/share/fonts/truetype/freefont/FreeMono.ttf' -p 12 -o testOut/test4_3.pdf testIn/test4.f90
