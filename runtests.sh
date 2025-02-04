#! /usr/bin/bash

set -x

rm testOut/test1.pdf
./prt1403.py -j TEST1   -u PRT1403 -s WIDE   -c GREEN -o testOut/test1.pdf testIn/test1.txt

rm testOut/test2.pdf
./prt1403.py -j PI      -u FRTRN77 -s SMALL  -c BLUE  -o testOut/test2.pdf testIn/test2.f77

rm testOut/test3.pdf
./prt1403.py -j TEST3   -u PRT1403 -s MEDIUM -c GRAY  -o testOut/test3.pdf testIn/test3.txt

rm testOut/test4_1.pdf
./prt1403.py -j BNCHMRK -u FRTRN90 -s SMALL  -c BLUE  -o testOut/test4_1.pdf testIn/test4.f90

rm testOut/test4_2.pdf
./prt1403.py -j BNCHMRK -u FRTRN90 -s SMALL  -c WHITE  -f FONT1403 -o testOut/test4_2.pdf testIn/test4.f90
