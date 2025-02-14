#! /usr/bin/bash

../prt1403 -y    -j TEST1   -u PRT1403 -s WIDE   -c GREEN -o testOut/test1.pdf testIn/test1.txt
../prt1403 -y    -j PI      -u FRTRN77 -s SMALL  -c BLUE  -o testOut/test2.pdf testIn/test2.f77
../prt1403 -y    -j TEST3   -u PRT1403 -s MEDIUM -c GRAY  -o testOut/test3.pdf testIn/test3.txt
../prt1403 -y    -j BNCHMRK -u FRTRN90 -s SMALL  -c BLUE  -o testOut/test4_1.pdf testIn/test4.f90
../prt1403 -y    -j BNCHMRK -u FRTRN90 -s SMALL  -c WHITE -f FONT1403 -o testOut/test4_2.pdf testIn/test4.f90
../prt1403 -y    -j BNCHMRK -u FRTRN90 -s WIDE   -c GREEN -f '/usr/share/fonts/truetype/freefont/FreeMono.ttf' -p 12 -o testOut/test4_3.pdf testIn/test4.f90
../prt1403 -y    -j BNCHMRK -u FRTRN90 -s SMALL  -c GREEN -f '/usr/share/fonts/truetype/Jellyka_Estrya_Handwriting/Jellyka_Estrya_Handwriting.ttf' -p 38 -o testOut/test4_4.pdf  testIn/test4.f90
../prt1403 -y -n                       -s SMALL  -c BLUE  -o testOut/test4_5.pdf testIn/test4.f90
../prt1403 -y -e -j BNCHMRK -u FRTRN90 -s SMALL  -f FONT1403 -o testOut/test4_6.pdf testIn/test4.f90
../prt1403 -y -e -j BNCHMRK -u FRTRN90 -s MEDIUM -o testOut/test4_7.pdf testIn/test4.f90
../prt1403 -y -e -j BNCHMRK -u FRTRN90 -s WIDE   -o testOut/test4_8.pdf testIn/test4.f90
../prt1403 -y -e -u PYNCKELS -j PERFORM -o testOut/test5.pdf - < testIn/test5.asc
(cat testIn/test6.py; echo -n -e '\x1C'; cat testIn/test6.f90; echo -n -e '\x1C'; cat testIn/test6.c) | ../prt1403 -y -e -u MAINT -j PERFORM -o testOut/test6_1.pdf -
(cat testIn/test4.f90; echo -n -e '\x1C'; cat testIn/test6.f90) | ../prt1403 -y -e -u OPERATOR -j FORTRAN -o testOut/test6_2.pdf -
