#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2015-2016, René Tanczos <gravmatt@gmail.com> (Twitter @gravmatt)
The MIT License (MIT)

pyterm helps positioning the cursor and styling output inside the terminal.

Project on github https://github.com/gravmatt/pyterm
"""

__author__ = 'Rene Tanczos'
__version__ = '0.3'
__license__ = 'MIT'

import sys, re
from subprocess import Popen, PIPE

off='\033[0m\033[27m'
bold='\033[1m'
dim='\033[2m'
underscore='\033[4m'
blink='\033[5m'
reverse='\033[7m'
hide='\033[8m'

black='\033[30m'
red='\033[31m'
green='\033[32m'
yellow='\033[33m'
blue='\033[34m'
magenta='\033[35m'
cyan='\033[36m'
white='\033[37m'

bgblack='\033[40m'
bgred='\033[41m'
bggreen='\033[42m'
bgyellow='\033[43m'
bgblue='\033[44m'
bgmagenta='\033[45m'
bgcyan='\033[46m'
bgwhite='\033[47m'

def send(cmd):
    sys.stdout.write(cmd)
    sys.stdout.flush()

def pos(line, column):
    send('\033[%s;%sf' % (line, column))

def homePos():
    send('\033[H')

def up(value=1):
    send('\033[%sA' % value)

def down(value=1):
    send('\033[%sB' % value)

def right(value=1):
    send('\033[%sC' % value)

def left(value=1):
    send('\033[%sD' % value)

def saveCursor():
    send('\0337')
    # send('\033[s')

def restoreCursor():
    send('\0338')
    # send('\033[u')

def clear():
    send('\033[2J')

def clearLineFromPos():
    send('\033[K')

def clearLineToPos():
    send('\033[1K')

def clearLine():
    send('\033[2K')

def write(text='', *style):
    send(format(text, *style))

def writeLine(text='', *style):
    write(str(text)+'\n', *style)

def strip(text):
    return re.sub('\x1b\[[0-9]{1,2}m', '', text)

def center(text):
    return ' '*(int(getSize()[1]/2) - int(len(strip(text))/2)) + text

def right(text):
    return ' '*(getSize()[1] - len(strip(text))) + text

def getSize():
    p = Popen('stty size', shell=True, stdout=PIPE, stderr=PIPE)
    err = p.stderr.read().strip()
    if(err):
        return (0, 0)
    else:
        out = p.stdout.read().decode('ascii').strip().split(' ')
        return int(out[0]), int(out[1])

def format(text, *style):
    if(style):
        return '%s%s%s' % (''.join(style), text, off)
    else:
        return text
