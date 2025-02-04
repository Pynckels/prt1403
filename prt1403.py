#! /usr/bin/env python3

# Copyright 2025 Filip Pynckels
# See README.md at https://github.com/Pynckels/prt1403

from datetime import datetime
from fpdf     import FPDF

import argparse
import os
import re

#------------------------------------------------------------------------------------------

BLUE_DARK    = {'R': 65, 'G':182, 'B':255}                          # Blue banded paper
BLUE_LIGHT   = {'R':214, 'G':239, 'B':255}
BLUE         = (BLUE_DARK, BLUE_LIGHT)

GRAY_DARK    = {'R':200, 'G':200, 'B':200}                          # Gray banded paper and tractor feed holes
GRAY_LIGHT   = {'R':230, 'G':230, 'B':230}
GRAY         = (GRAY_DARK, GRAY_LIGHT)

GREEN_DARK   = {'R': 99, 'G':182, 'B': 99}                          # Green banded paper
GREEN_LIGHT  = {'R':219, 'G':250, 'B':219}
GREEN        = (GREEN_DARK, GREEN_LIGHT)

ORANGE_DARK  = {'R':219, 'G':182, 'B': 99}                          # Orange banded paper
ORANGE_LIGHT = {'R':255, 'G':221, 'B':146}
ORANGE       = (ORANGE_DARK, ORANGE_LIGHT)

WHITE_DARK   = {'R':255, 'G':255, 'B':255}                          # Plain old white paper
WHITE_LIGHT  = {'R':255, 'G':255, 'B':255}
WHITE        = (WHITE_DARK, WHITE_LIGHT)

PAGE_SMALL   = [ 684, 792,  82, 66]                                 #  9.5 inch x 11 inch,  80 chars/line, 66 lines
PAGE_MEDIUM  = [ 864, 792, 107, 66]                                 # 12.0 inch x 11 inch, 100 chars/line, 66 lines
PAGE_WIDE    = [1044, 792, 132, 66]                                 # 14.5 inch x 11 inch, 132 chars/line, 66 lines

FONT1403     = ['IBM140310Pitch-Regular-MRW.ttf', 10, '#$%*+,-./0123456789@ABCDEFGHIJKLMNOPQRSTUVWXYZ']
FONTMONO     = ['IBMPlexMono-Regular.ttf'       , 12, None]

#------------------------------------------------------------------------------------------

def change_invalid_characters(inStr, font):

    '''
    Convert all characters that the font can't cope with to space
    '''
    
    ASCII_MIN = ' '                                                 # Ascii character 32
    ASCII_MAX = '~'                                                 # Ascii character 126
    ASCII_REP = ' '                                                 # Substitution character

    if font is FONT1403:
        validCharsSet = set( font[2] )
        result = ''.join(char if char in validCharsSet else ASCII_REP for char in inStr.upper())
        return result
    elif font is FONTMONO:
        result = ''.join(char if ASCII_MIN <= char <= ASCII_MAX else ASCII_REP for char in inStr.upper())
        return result
    else:                                                           # Take the minimum allowed approach
        validCharSet = set( '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' )
        result = ''.join(char if char in validCharsSet else ASCII_REP for char in inStr.upper())
        return result

    return None                                                     # This should never be reached (security measure)

#------------------------------------------------------------------------------------------

def draw_bezier_curve(pdf, x0, y0, x1, y1, x2, y2, steps=20):

    '''
    Draw a quadratic Bézier curve (approximated by a series of lines, default 20)
    '''

    last_x, last_y = x0, y0                                         # Initialize the first point

    for t in range(1, steps + 1):
        u = t / steps                                               # Bézier curve point at parameter t (0 <= t <= 1)
        x = (1 - u)**2 * x0 + 2 * (1 - u) * u * x1 + u**2 * x2
        y = (1 - u)**2 * y0 + 2 * (1 - u) * u * y1 + u**2 * y2

        if t != 1:                                                  # Draw a line from last point to the current point
            pdf.line(last_x, last_y, x, y)

        last_x, last_y = x, y                                       # Update last point to current point

#------------------------------------------------------------------------------------------

def prt1403_draw_form(pdf, size, color):

    '''
    Draw the form background (bars, lines, characters, ...)
    '''

    FREE_HOLE_RADIUS = 5.5                                          # Experimentally found constant

    page_width  = size[0]
    page_height = size[1]

    pdf.set_draw_color(color[0]['R'], color[0]['G'], color[0]['B']) # Form settings
    pdf.set_fill_color(color[1]['R'], color[1]['G'], color[1]['B'])
    pdf.set_text_color(color[0]['R'], color[0]['G'], color[0]['B'])
    pdf.set_font("helvetica", "", 7)

    pdf.set_line_width(0.7)                                         # Alignment fiducial
    pdf.line(20, 54-FREE_HOLE_RADIUS*2, 20, 54+FREE_HOLE_RADIUS*2)
    pdf.line(20-FREE_HOLE_RADIUS*2, 54, 20+FREE_HOLE_RADIUS*2, 54)
    pdf.set_line_width(1.5)
    pdf.circle(20, 54, FREE_HOLE_RADIUS+.6, "D")
                                                                    # Draw form number (1412THE)
    x_position = page_width - 9                                     #  9 units from the right margin
    y_position = 57                                                 # 57 units from the top margin
    with pdf.rotation(-90, x_position, y_position):
        pdf.text(x_position, y_position, '1412THE')
                                                                    # Area alignment arrows
    pdf.polygon( [(40+2, 72-11), (40+2+5, 72), (40+2+5*2, 72-11)], style='F')
    pdf.polygon( [(page_width-40-2, 72-11), (page_width-40-2-5, 72), (page_width-40-2-5*2, 72-11)], style='F')

    bX = page_width - 20                                            # Outline "1"
    bY = page_height - 29
    bU = 0.6
    pdf.set_line_width(1)
    pdf.line(bX+bU*5, bY-bU*17, bX+bU*5, bY-bU*3.5)
    pdf.line(bX+bU*5, bY-bU*3.5, bX, bY-bU*3.5)
    pdf.line(bX, bY-bU*3.5, bX, bY)
    pdf.line(bX, bY, bX+bU*14, bY)
    pdf.line(bX+bU*14, bY, bX+bU*14, bY-bU*3.5)
    pdf.line(bX+bU*14, bY-bU*3.5, bX+bU*9, bY-bU*3.5)
    pdf.line(bX+bU*9, bY-bU*3.5, bX+bU*9, bY-bU*24)
    pdf.line(bX+bU*9, bY-bU*24, bX+bU*8, bY-bU*24)
    draw_bezier_curve(pdf, bX+bU*8, bY-bU*24, bX+bU*6, bY-bU*20.5, bX, bY-bU*19)
    pdf.line(bX, bY-bU*19, bX, bY-bU*15)
    draw_bezier_curve(pdf, bX, bY-bU*15, bX+bU*3.5, bY-bU*15.5, bX+bU*5, bY-bU*17)

    for i in range(0,10):                                           # Bars - fill
        pdf.rect(40, 72+i*72-0.5, page_width-80, 36, 'F')

    pdf.set_line_width(0.7)                                         # Bars - horizontal lines
    pdf.line(30-0.25, 72-0.5, page_width-30+0.25, 72-0.5)
    pdf.line(30-0.25, page_height-1-0.5, page_width-30+0.25, page_height-1-0.5)
    for i in range(0,20):
        pdf.line(40, 72+36*i-0.5, page_width-40, 72+36*i-0.5)

    pdf.set_line_width(0.5)                                         # Vertical lines
    pdf.line(30-0.5, 72-0.5, 30-0.5, page_height-1-0.5)
    pdf.line(40, 72-0.5, 40, page_height-1-0.5)
    pdf.line(page_width-30+0.5, 72-0.5, page_width-30+0.5, page_height-1-0.5)
    pdf.line(page_width-40, 72-0.5, page_width-40, page_height-1-0.5)

    for i in range(0,60):                                           # Left margin numbers
        pdf.set_xy(30, 72+i*12)
        w = 9.7
        if i < 9 : w = 10
        pdf.cell(w, 12, text=str(i+1), align='C')

    for i in range(0,80):
        pdf.set_xy(page_width-40, 72+i*9)
        w = 9.7
        if i < 9 : w = 10
        pdf.cell(w, 9, str(i+1), align='C')

#------------------------------------------------------------------------------------------

def prt1403_draw_holes(pdf, size, color):

    '''
    Draw the perforated holes
    Must be called after prt1403_draw_form in order to 'perforate' the alignment fiducial
    '''

    FREE_HOLE_RADIUS = 5.5                                          # Experimentally found constant

    page_width  = size[0]
    page_height = size[1]

    pdf.set_draw_color(color[0]['R'], color[0]['G'], color[0]['B']) # Hole settings
    pdf.set_fill_color(color[1]['R'], color[1]['G'], color[1]['B'])
    pdf.set_line_width(0.75)

    y = 18.0 + 18.0 * 2 * 0                                         # Top holes are larger than other holes
    pdf.circle(20, y, FREE_HOLE_RADIUS+1, "FD")
    pdf.circle(page_width - 20, y, FREE_HOLE_RADIUS+1, 'FD')

    y = 18.0 + 18.0 * 2 * 21                                        # Bottom holes are larger than other holes
    pdf.circle(20, y, FREE_HOLE_RADIUS+1, "FD")
    pdf.circle(page_width - 20, y, FREE_HOLE_RADIUS+1, 'FD')

    for i in range(1,21):                                           # All other holes
        y = 18.0 + 18.0 * 2 * i
        pdf.circle(20, y, FREE_HOLE_RADIUS, "FD")
        pdf.circle(page_width - 20, y, FREE_HOLE_RADIUS, 'FD')

#------------------------------------------------------------------------------------------

def prt1403_draw_page(pdf, text, size, font, color_form, color_holes):

    '''
    Draw a single page of text.
    text contains all the text that should be places on this page (incl. headers, footers, ...)
    '''

    pdf.add_page()                                                  # Create new page
    pdf.set_margins(0, 0, 0)
    pdf.set_auto_page_break(True, margin = 0.0)
    prt1403_draw_form(pdf, size, color_form)                        # Draw page background
    prt1403_draw_holes(pdf, size, color_holes)                      # Draw page holes (after drawing background)

    pdf.set_font('prt1403Font')                                     # Activate prt1403 font
    pdf.set_font_size(font[1])
    pdf.set_text_color(0, 0, 0)

    lines = [ line[:size[2]+1].rstrip() for line in text[:size[3]] ] # Clip to maximal number chars and lines

    lineNr = 1                                                      # Print all lines on the page
    for line in lines:
        line = change_invalid_characters(line, font)                # Check if the font can cope with the text chars
        pdf.text(43, lineNr*12-3, line);
        lineNr += 1

    return

#------------------------------------------------------------------------------------------

def prt1403_print(
    inFile                  ,
    outFile                 ,
    size        = PAGE_WIDE ,
    font        = FONTMONO  ,
    color_form  = GREEN     ,
    color_holes = GRAY      ,
    userId      = 'USERID'  ,
    jobId       = 'JOBID'
    ):

    '''
    Print the text in inFile. This file does not contain an ASA (page formatting) column
    '''

    date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    path = os.path.dirname(os.path.realpath(__file__)) + '/' + font[0]
    head = 'DATE: '                + \
          date                     + \
          '     USER: '            + \
          userId[:8].ljust(8, ' ') + \
          '     JOB: '             + \
          jobId[:8].ljust(8, ' ')  + \
          ' ' * ( size[2] -71 )    + \
          'PAGE: '
    page = 1

    with open(inFile, 'r') as inf:
        lines = inf.readlines()

    if font is FONT1403:                                            # Reduce used characters for FONT1403
        lines = [line.upper() for line in lines]

    pdf = FPDF(orientation='P', unit='pt', format=size)             # Create fpdf environment
    pdf.add_font('prt1403Font', '', path)                           # Setup prt1403 font

    while len(lines):
        text = [' ', ' ', ' ']
        text = text + [head + f'{page:04}']
        text = text + [' ', ' ']
        text = text + lines[:60]

        prt1403_draw_page(pdf, text, size, font, color_form, color_holes)

        page += 1
        lines = lines[60:]

    pdf.output(outFile)

#------------------------------------------------------------------------------------------

def main():

    '''
    Check arguments and print file with the given options
    '''

    def id_validator(value):
        ''' Check if the value is between 1 and 8 characters long and is alphanumeric. '''
        if not re.match(r'^[a-zA-Z0-9]{1,8}$', value):
            raise argparse.ArgumentTypeError('Job ID must be between 1 and 8 alphanumeric characters.')
        return value

    def infile_validator(file_path):
        ''' Check if the file is UTF-8 encoded. '''
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file.read()
            return file_path                                        # Return the file path if it's a valid UTF-8 file
        except UnicodeDecodeError:
            raise argparse.ArgumentTypeError(f'The file {file_path} is not a valid UTF-8 text file.')
        except FileNotFoundError:
            raise argparse.ArgumentTypeError(f'The file {file_path} does not exist.')

    def outfile_validator(file_path):
        ''' Check if the output file path is valid and does not exist. '''
        directory = os.path.dirname(file_path)                      # Check if the directory exists
        if not os.path.isdir(directory) and directory != '':
            raise argparse.ArgumentTypeError(f'The directory {directory} does not exist.')
        if os.path.exists(file_path):                               # Check if the file already exists
            raise argparse.ArgumentTypeError(f'The file {file_path} already exists.')        
        return file_path                                            # Return the output file path if it's valid

    parser = argparse.ArgumentParser(description='Print a text file to PDF in IBM 1403 retro style')

    parser.add_argument('infile',          metavar='<Input file>',  type=infile_validator,                                               help='File to process.')
    parser.add_argument('-c', '--color',                            choices=['BLUE', 'GRAY', 'GREEN', 'WHITE'],   default='GREEN',       help='Color of form preprint. Text color is black.')
    parser.add_argument('-f', '--font',                             choices=['FONT1403', 'FONTMONO'],             default='FONTMONO',    help='Choose between FONT1403 and FONTMONO.')
    parser.add_argument('-j', '--jobid',   metavar='jobID',         type=id_validator,                            default='NONE',        help='Job identifier (1 to 8 alphanumeric characters).')
    parser.add_argument('-o', '--outfile', metavar='<Output file>', type=outfile_validator,                       default='prt1403.pdf', help='Output file name.')
    parser.add_argument('-s', '--size',                             choices=['SMALL', 'MEDIUM', 'WIDE'],          default='WIDE',        help='Paper width 9.5", 12" or 14.5". Paper height is 11"')
    parser.add_argument('-u', '--userid',  metavar='userID',        type=id_validator,                            default='NONE',        help='User identifier (1 to 8 alphanumeric characters).')

    args = parser.parse_args()
                                                                    # Hit the road...
    prt1403_print(
        args.infile                                  ,
        args.outfile                                 ,
        size        = globals()['PAGE_' + args.size] ,
        font        = globals()[args.font]           ,
        color_form  = globals()[args.color]          ,
        color_holes = GRAY                           ,
        userId      = args.userid                    ,
        jobId       = args.jobid
    )

#------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()                                                          # Do not run if script is imported as a module
