#! /usr/bin/env python3

# Copyright 2025 Filip Pynckels
# See README.md at https://github.com/Pynckels/prt1403

# Acknowledgement
# The fonts are gathered from listings all around the place.
# Some characters are deduced from parts of other characters.

import base64
import json
import lzma
import re

def split_string(b64_string, line_length=91):
    return [b64_string[i:i+line_length] for i in range(0, len(b64_string)+1, line_length)]

def main():
    sepChars = re.split(r'--- \w+ ---', SEPFONT)[1:]            # Split at '--- ? ---'
    sepChars = [s.replace('\n\n', '') for s in sepChars]        # Remove '\n\n'
    sepChars = [s.split('\n') for s in sepChars]                # Make list of lists
    sepChars = [[s.rstrip() for s in l] for l in sepChars]      # Remove right white space
    sepChars = [[s for s in l if s != ''] for l in sepChars]    # Remove empty lines
    sepChars = [[s.ljust(9) for s in l ] for l in sepChars]     # Adjust to strings of 9 long

    sepDict  = {}
    for l in sepChars:
        char = next(c for c in l[0] if c != ' ')                # Find unique non-blank character
        sepDict[char] = l                                       # Add info to dictionary

    sepJson  = json.dumps(sepDict)                              # Convert to json
    sepLzm   = lzma.compress(sepJson.encode())                  # Compress
    sepB64   = split_string('SEPFONT = """' + base64.b64encode(sepLzm).decode('utf-8') + '"""')

    line = ['#------------------------------------------------------------------------------------------']
    code = line + sepB64 + line

    with open('SEPfont.inc', 'w') as f:
        f.write("\n".join(code) + "\n")

#------------------------------------------------------------------------------------------

SEPFONT = '''
--- A ---

   AAA
  AAAAA
 AA   AA
AA     AA
AA     AA
AAAAAAAAA
AAAAAAAAA
AA     AA
AA     AA
AA     AA
 
--- B ---

BBBBBBBB
BBBBBBBBB
BB     BB
BB     BB
BBBBBBBB
BBBBBBBB
BB     BB
BB     BB
BBBBBBBBB
BBBBBBBB

--- C ---

 CCCCCCC
CCCCCCCCC
CC     CC
CC
CC
CC
CC
CC     CC
CCCCCCCCC
 CCCCCCC

--- D ---

DDDDDDDD
DDDDDDDDD
DD     DD
DD     DD
DD     DD
DD     DD
DD     DD
DD     DD
DDDDDDDDD
DDDDDDDD

--- E ---

EEEEEEEEE
EEEEEEEEE
EE
EE
EEEEEEEEE
EEEEEEEEE
EE
EE
EEEEEEEEE
EEEEEEEEE

--- F ---

FFFFFFFFF
FFFFFFFFF
FF
FF
FFFFFFFFF
FFFFFFFFF
FF
FF
FF
FF

--- G ---

 GGGGGGG
GGGGGGGGG
GG     GG
GG
GG
GG   GGGG
GG   GGGG
GG     GG
GGGGGGGGG
 GGGGGGG

--- H ---

HH     HH
HH     HH
HH     HH
HH     HH
HHHHHHHHH
HHHHHHHHH
HH     HH
HH     HH
HH     HH
HH     HH

--- I ---

 IIIIII
 IIIIII
   II
   II
   II
   II
   II
   II
 IIIIII
 IIIIII

--- J ---

  JJJJJJ
  JJJJJJ
    JJ
    JJ
    JJ
    JJ
JJ  JJ
JJJJJJ
 JJJJ

--- K ---

KKKKKKKKK
KKKKKKKKK
KKKKKKKKK
KKKKKKKKK
KKKKKKKKK
KKKKKKKKK
KKKKKKKKK
KKKKKKKKK
KKKKKKKKK
KKKKKKKKK

--- L ---

LL
LL
LL
LL
LL
LL
LL
LL
LLLLLLLLL
LLLLLLLLL

--- M ---

M       M
MM     MM
MMM   MMM
MMMM MMMM
MM MMM MM
MM  M  MM
MM     MM
MM     MM
MM     MM
MM     MM

--- N ---

N      NN
NN     NN
NNN    NN
NNNN   NN
NN NN  NN
NN  NN NN
NN   NNNN
NN    NNN
NN     NN
NN      N

--- O ---

 OOOOOOO
OOOOOOOOO
OO     OO
OO     OO
OO     OO
OO     OO
OO     OO
OO     OO
OOOOOOOOO
 OOOOOOO

--- P ---

PPPPPPPP
PPPPPPPPP
PP     PP
PP     PP
PPPPPPPPP
PPPPPPPP
PP
PP
PP
PP

--- Q ---

QQQQQQQQQ
QQQQQQQQQ
QQQQQQQQQ
QQQQQQQQQ
QQQQQQQQQ
QQQQQQQQQ
QQQQQQQQQ
QQQQQQQQQ
QQQQQQQQQ
QQQQQQQQQ

--- R ---

RRRRRRRR
RRRRRRRRR
RR     RR
RR     RR
RRRRRRRRR
RRRRRRRR
RR  RR
RR   RR
RR    RR
RR     RR

--- S ---

 SSSSSSS
SSSSSSSSS
SS     SS
SS
SSSSSSSS
 SSSSSSSS
       SS
SS     SS
SSSSSSSSS
 SSSSSSS

--- T ---

TTTTTTTT
TTTTTTTT
   TT
   TT
   TT
   TT
   TT
   TT
   TT
   TT

--- U ---

UU     UU
UU     UU
UU     UU
UU     UU
UU     UU
UU     UU
UU     UU
UU     UU
UUUUUUUUU
 UUUUUUU

--- V ---

VV     VV
VV     VV
VV     VV
VV     VV
VV     VV
VV     VV
 VV   VV
  VVVVV
   VVV
    V

--- W ---

WW     WW
WW     WW
WW     WW
WW     WW
WW  W  WW
WW WWW WW
WWWW WWWW
WWW   WWW
WW     WW
W       W

--- X ---

XX    XX
XX    XX
XX    XX
 XX  XX
  XXXX
  XXXX
 XX  XX
XX    XX
XX    XX
XX    XX

--- Y ---

YY    YY
YY    YY
YY    YY
 YY  YY
  YYYY
   YY
   YY
   YY
   YY
   YY

--- Z ---

ZZZZZZZZZ
ZZZZZZZZZ
      ZZ
     ZZ
    ZZ
   ZZ
  ZZ
 ZZ
ZZZZZZZZZ
ZZZZZZZZZ

--- 0 ---

  00000
 0000000
00     00
00     00
00     00
00     00
00     00
00     00
 0000000
  00000

--- 1 ---

    1
   11
  111
   11
   11
   11
   11
   11
 111111
 111111

--- 2 ---

 2222222
222222222
22     22
      22
     22
    22
   22
  22
 22222222
222222222

--- 3 ---

 3333333
333333333
33     33
       33
     333
     333
       33
33     33
333333333
 3333333

--- 4 ---

444444444
444444444
444444444
444444444
444444444
444444444
444444444
444444444
444444444
444444444

--- 5 ---

555555555
555555555
55
55
55555555
555555555
       55
       55
555555555
55555555

--- 6 ---

 6666666
66666666
66
66
66666666
666666666
66     66
66     66
666666666
 6666666

--- 7 ---

777777777
777777777
       77
      77
     77
    77
   77
  77
 77
77

--- 8 ---

 8888888
888888888
88     88
88     88
 8888888
 8888888
88     88
88     88
888888888
 8888888

--- 9 ---

 9999999
999999999
99     99
99     99
999999999
 99999999
       99
       99
 99999999
 9999999
'''

#------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
