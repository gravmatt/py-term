#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2015-2016, René Tanczos <gravmatt@gmail.com> (Twitter @gravmatt)
The MIT License (MIT)

pyterm helps positioning the cursor and styling output inside the terminal.

Project on github https://github.com/gravmatt/py-term
"""

__author__ = 'Rene Tanczos'
__version__ = '0.6'
__license__ = 'MIT'

import sys
import re
import os
from subprocess import Popen, PIPE


off = '\033[0m\033[27m'
bold = '\033[1m'
dim = '\033[2m'
underscore = '\033[4m'
blink = '\033[5m'
reverse = ' \033[7m'
hide = '\033[8m'

black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
magenta = '\033[35m'
cyan = '\033[36m'
white = '\033[37m'

bgblack = '\033[40m'
bgred = '\033[41m'
bggreen = '\033[42m'
bgyellow = '\033[43m'
bgblue = '\033[44m'
bgmagenta = '\033[45m'
bgcyan = '\033[46m'
bgwhite = '\033[47m'


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
    write(str(text) + '\n', *style)


def setTitle(name):
    send('\033]2;%s\007' % name)


def clearTitle():
    setTitle('')


def setTab(name):
    send('\033]1;%s\007' % name)


def clearTab():
    setTab('')


def strip(text):
    return re.sub('\x1b\[[0-9]{1,2}m', '', text)


def center(text):
    return ' ' * (int(getSize()[1] / 2) - int(len(strip(text)) / 2)) + text


def right(text):
    return ' ' * (getSize()[1] - len(strip(text))) + text


def getSize():
    import platform
    os_sys = platform.system()
    if(os_sys in ['Linux', 'Darwin'] or os_sys.startswith('CYGWIN')):
        try:
            def __get_unix_terminal_size(fd):
                import fcntl, termios, struct
                return struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, 'rene'))
            cr = __get_unix_terminal_size(0) or __get_unix_terminal_size(1) or __get_unix_terminal_size(2)
            if(not cr):
                fd = os.open(os.ctermid(), os.O_RDONLY)
                cr = __get_unix_terminal_size(fd)
                os.close(fd)
            return cr
        except:
            pass
    else:
        raise Exception('operating system not supported')


def format(text, *style):
    if(style):
        return '%s%s%s' % (''.join(style), text, off)
    else:
        return text


def highlight(pattern, text, func):
    output = ''
    idx = 0
    matches = [(m.start(), m.end()) for m in re.finditer(pattern, text)]
    for p in matches:
        output += text[idx:p[0]]
        output += func(text[p[0]:p[1]])
        idx = p[1]
    output += text[idx:]
    return (output, len(matches), matches)
