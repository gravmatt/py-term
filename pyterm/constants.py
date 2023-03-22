#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pyterm

 - File: pyterm/constants.py
 - Author: Havocesp <https://github.com/havocesp/pyterm>
 - Created: 2023-03-22
 -
"""
BLINK = '\033[5m'
BOLD = '\033[1m'
DIM = '\033[2m'
HIDE = '\033[8m'
OFF = '\033[0m\033[27m'
REVERSE = ' \033[7m'
UNDERSCORE = '\033[4m'
UNDERLINE = UNDERSCORE

BLACK = '\033[30m'
BLUE = '\033[34m'
CYAN = '\033[36m'
GREEN = '\033[32m'
MAGENTA = '\033[35m'
RED = '\033[31m'
WHITE = '\033[37m'
YELLOW = '\033[33m'

BGBLACK = '\033[40m'
BGBLUE = '\033[44m'
BGCYAN = '\033[46m'
BGGREEN = '\033[42m'
BGMAGENTA = '\033[45m'
BGRED = '\033[41m'
BGWHITE = '\033[47m'
BGYELLOW = '\033[43m'

# aliases
BK = BLACK
BL = BLUE
CY = CYAN
GN = GREEN
MG = MAGENTA
RD = RED
WH = WHITE
YL = YELLOW

BGK = BGBLACK
BGL = BGBLUE
BGC = BGCYAN
BGG = BGGREEN
BGM = BGMAGENTA
BGR = BGRED
BGW = BGWHITE
BGY = BGYELLOW

BLK = BLINK
BD = BOLD
DN = DIM
HD = HIDE
OF = OFF
RV = REVERSE
US = UNDERSCORE
UL = UNDERLINE

__all_constants__ = []

__all__ = [
    'BD',
    'BGBLACK',
    'BGBLUE',
    'BGC',
    'BGCYAN',
    'BGG',
    'BGGREEN',
    'BGK',
    'BGL',
    'BGM',
    'BGMAGENTA',
    'BGR',
    'BGRED',
    'BGW',
    'BGWHITE',
    'BGY',
    'BGYELLOW',
    'BK',
    'BL',
    'BLACK',
    'BLINK',
    'BLK',
    'BLUE',
    'BOLD',
    'CY',
    'CYAN',
    'DIM',
    'DN',
    'GN',
    'GREEN',
    'HD',
    'HIDE',
    'MAGENTA',
    'MG',
    'OF',
    'OFF',
    'RD',
    'RED',
    'REVERSE',
    'RV',
    'UNDERLINE',
    'UNDERSCORE',
    'US',
    'WH',
    'WHITE',
    'YELLOW',
    'YL',
    'UL',
    '__all_constants__'
]

__all_constants__.extend(__all__)
