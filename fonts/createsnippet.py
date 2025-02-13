#! /usr/bin/env python3

# Copyright 2025 Filip Pynckels
# See README.md at https://github.com/Pynckels/prt1403

# Acknowledgement
# IBM font   : https://github.com/Pynckels/prt1403/fonts/IBMPlexMono-Regular.license
# 1403 font  : https://ibm-1401.info/1403Fonts.html#Fonts

import base64
import lzma

def compress(bin_bytes):
    return lzma.compress(bin_bytes)

def split_string(b64_string, line_length=91):
    return [b64_string[i:i+line_length] for i in range(0, len(b64_string)+1, line_length)]

with open('IBMPlexMono-Regular.ttf', 'rb') as f:
    bin_1 = f.read()
    com_1 = compress(bin_1)
    b64_1 = split_string( 'IBMPlexMono = """' + base64.b64encode(com_1).decode('utf-8') + '"""' )

with open('IBM140310Pitch-Regular-MRW.ttf', 'rb') as f:
    bin_2 = f.read()
    com_2 = compress(bin_2)
    b64_2 = split_string( 'IBM1403 = """' + base64.b64encode(com_2).decode('utf-8') + '"""')

line = ['#------------------------------------------------------------------------------------------']
code = line + b64_1 + line + b64_2 + line

with open('snippet.inc', 'w') as f:
    f.write("\n".join(code) + "\n")
