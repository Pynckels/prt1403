#! /usr/bin/bash

set -x

../prt1403 -y -j TEST1   -u PRT1403 -s WIDE   -c GREEN -o testOut/test1.pdf testIn/test1.txt
../prt1403 -y -j PI      -u FRTRN77 -s SMALL  -c BLUE  -o testOut/test2.pdf testIn/test2.f77
../prt1403 -y -j TEST3   -u PRT1403 -s MEDIUM -c GRAY  -o testOut/test3.pdf testIn/test3.txt
../prt1403 -y -j BNCHMRK -u FRTRN90 -s SMALL  -c BLUE  -o testOut/test4_1.pdf testIn/test4.f90
../prt1403 -y -j BNCHMRK -u FRTRN90 -s SMALL  -c WHITE  -f FONT1403 -o testOut/test4_2.pdf testIn/test4.f90
../prt1403 -y -j BNCHMRK -u FRTRN90 -f '/usr/share/fonts/truetype/freefont/FreeMono.ttf' -p 12 -o testOut/test4_3.pdf testIn/test4.f90
../prt1403 -y -n -s SMALL  -c BLUE  -o testOut/test4_4.pdf testIn/test4.f90
