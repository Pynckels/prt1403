# prt1403

Print a text file to PDF in IBM 1403 retro style

![Fortran source code](tests/testOut/test2.png)

### Note

This is a work in progress, constructive comments are appreciated.

### Installing

#### Linux

The easiest way to install prt1403 is as follows.

    mkdir -p ~/.local/bin
    git clone https://github.com/Pynckels/prt1403.git
    pip install -r ./prt1403/requirements.txt
    mv ./prt1403/prt1403 ~/.local/bin/prt1403
    chmod +x ~/.local/bin/prt1403
    rm -r prt1403

If running the program does not function, logging out and back in can help to update your $PATH.

#### Mac & Windows

Contact me and we'll cook something up together.

### Syntax

To get the command line syntax the -h and the --help option can be used.

    prt1403 --help

This results in the following information.

    usage: prt1403 [-h] [-c {BLUE,GRAY,GREEN,WHITE}] [-f FONT] [-j jobID] [-o <Output file>] [-p PITCH]
                   [-s {SMALL,MEDIUM,WIDE}] [-u userID] [-v] [-y]
                   <Input file>
    
    Print a text file to PDF in IBM 1403 retro style
    
    positional arguments:
      <Input file>          File to process.
    
    options:
      -h, --help            show this help message and exit
      -c {BLUE,GRAY,GREEN,WHITE}, --color {BLUE,GRAY,GREEN,WHITE}
                            Color of form preprint. Text color is black.
      -f FONT, --font FONT  Choose between FONT1403, FONTMONO or an installed font.
      -j jobID, --jobid jobID
                            Job identifier (1 to 8 alphanumeric characters).
      -o <Output file>, --outfile <Output file>
                            Output file name.
      -p PITCH, --pitch PITCH
                            Size of font in points (e.g. 10). Not used for FONT1403 or FONTMONO.
      -s {SMALL,MEDIUM,WIDE}, --size {SMALL,MEDIUM,WIDE}
                            Paper width 9.5", 12" or 14.5". Paper height is 11"
      -u userID, --userid userID
                            User identifier (1 to 8 alphanumeric characters).
      -v, --version         Show program version and exit.
      -y, --overwrite       Overwrite output file.

### Fonts

The default font is `FONTMONO` (IBMPlexMono-Regular.ttf). This font comes with this program.

    prt1403 -o example.pdf example.txt

There is also the choice for `FONT1403` (IBM140310Pitch-Regular-MRW.ttf). This font also comes with this program. The latter has a limited character set, but is a very good representation of the original 1403 printer chain. To use `FONT1403` you can use the option -f/--font.

    prt1403 -f FONT1403 -o example.pdf example.txt

Note that the option -p/--pitch is disregarded when using the fonts `FONTMONO` or `FONT1403`.

If you want to use fonts that are installed on your pc, that's also possible. To find the installed fonts on Linux, you can use the following commands:

    fc-list | grep -ioP '.*\.(otf|ttf)(?=:)'

To use an installed font (e.g. FreeMono.ttf) you can use the option -f/--font) and eventually -p/--pitch to scale the font.

    prt1403 -f '/usr/share/fonts/truetype/freefont/FreeMono.ttf' -p 12 -o example.pdf example.txt

### License

Copyright (c) 2025 by Filip Pynckels

This file is part of the prt1403 project that can be found at
https://github.com/Pynckels/prt1403

prt1403 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

prt1403 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with prt1403. If not, see <https://www.gnu.org/licenses/>.

### Acknowledgements

***virtual1403*** : This project is inspired by, and uses logic from the virutal1403 project of Matthew R. Wilson that can be found at https://github.com/racingmars/virtual1403

***IBM font*** : This project uses the IBMPlexMono-Regular font. It is licensed under IBMPlexMono-Regular.license

***1403 font*** : This project uses the IBM140310Pitch-Regular-MRW font. It can be found at https://ibm-1401.info/1403Fonts.html#Fonts
