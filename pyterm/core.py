#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pyterm

 - File: pyterm/core.py
 - Author: Havocesp <https://github.com/havocesp/pyterm>
 - Created: 2023-03-22
 -
"""

import shutil
import sys
from typing import NoReturn, Text, Tuple

import regex as re

from pyterm.model import Color


class Term(Color):
    """Term class for controlling the termina feature like output color, cursor position, etc."""

    @classmethod
    def _send(cls, cmd) -> NoReturn:
        sys.stdout.write(cmd)
        sys.stdout.flush()

    @classmethod
    def pos(cls, line: int, column: int) -> NoReturn:
        """ Set the cursor position to the given line and column.

        :param line: terminal line position. 1 is the first line.
        :param column: terminal column position. 1 is the first column.
        """
        cls._send(f'\033[{line};{column}f')

    @classmethod
    def home_pos(cls) -> NoReturn:
        """ Set the cursor position to the home position (1,1). """
        cls._send('\033[H')

    @classmethod
    def up(cls, value: int = 1) -> NoReturn:
        """ Move the cursor up the given number of lines.

        :param value: number of lines to move the cursor up. 1 is the default value.
        """
        cls._send(f'\033[{value}A')

    @classmethod
    def down(cls, value=1) -> NoReturn:
        """ Move the cursor down the given number of lines.

        :param value: number of lines to move the cursor down. 1 is the default value.
        """
        cls._send(f'\033[{value}B')

    @classmethod
    def right(cls, value=1) -> NoReturn:
        """ Move the cursor right the given number of columns.

        :param value: number of columns to move the cursor right. 1 is the default value.
        """
        cls._send(f'\033[{value}C')

    @classmethod
    def left(cls, value=1) -> NoReturn:
        cls._send(f'\033[{value}D')

    @classmethod
    def save_cursor(cls) -> NoReturn:
        """ Save the current cursor position. """
        cls._send('\0337')
        # _send('\033[s')

    @classmethod
    def restore_cursor(cls) -> NoReturn:
        cls._send('\0338')
        # _send('\033[u')

    @classmethod
    def clear(cls) -> NoReturn:
        cls._send('\033[2J')

    @classmethod
    def clear_line_from_pos(cls) -> NoReturn:
        cls._send('\033[K')

    @classmethod
    def clear_line_to_pos(cls) -> NoReturn:
        cls._send('\033[1K')

    @classmethod
    def clear_line(cls) -> NoReturn:
        """ Clear the current line."""
        cls._send('\033[2K')

    @classmethod
    def write(cls, text: Text, *style) -> NoReturn:
        """ Write text to the terminal.

        :param text: text to write to the terminal.
        :param Iterable[Color] style: style to apply to the text.
        """
        cls._send(cls.style(text, *style))

    @classmethod
    def write_line(cls, text: Text, *style) -> NoReturn:
        """ Write a line of text to the terminal.

        :param text: text to write to the terminal.
        :param Iterable[Color] style: style to apply to the text.
        """
        cls.write(f'{text}\n', *style)

    @classmethod
    def set_title(cls, name: Text) -> NoReturn:
        """ Set the terminal title.

        :param name: title to set.
        """
        cls._send(f'\033]2;{name}\007')

    @classmethod
    def clear_title(cls) -> NoReturn:
        cls.set_title('')

    @classmethod
    def set_tab(cls, name: str) -> NoReturn:
        cls._send(f'\033]1;{name}\007')

    @classmethod
    def clear_tab(cls) -> NoReturn:
        cls.set_tab('')

    @classmethod
    def strip(cls, text) -> NoReturn:
        return re.sub(r'\x1b\[[0-9]{1,2}m', '', text)

    @classmethod
    def center(cls, text) -> NoReturn:
        '''
        DEPRICATED: Use textCenter() instead!
        Will be removed in later verions!
        '''
        return ' ' * (int(cls.get_size()[1] / 2) - int(len(cls.strip(text)) / 2)) + text

    @classmethod
    def text_right(cls, text: Text) -> Text:
        """Align text to the right of the terminal.

        :param text: text to align
        :return: aligned text
        """
        _diff = cls.term_cols() - len(cls.strip(text))
        return str(' ' * _diff) + text

    # @classmethod
    # def get_size(cls):
    #
    #     os_sys = platform.system()
    #     if os_sys in ['Linux', 'Darwin'] or os_sys.startswith('CYGWIN'):
    #         try:
    #             def _get_unix_terminal_size(fd):
    #                 import fcntl, termios, struct
    #                 return struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, 'rene'))
    #
    #             cr = _get_unix_terminal_size(0) or _get_unix_terminal_size(1) or _get_unix_terminal_size(2)
    #             if not cr:
    #                 fd = os.open(os.ctermid(), os.O_RDONLY)
    #                 cr = _get_unix_terminal_size(fd)
    #                 os.close(fd)
    #             return cr
    #         except:
    #             pass
    #     else:
    #         raise Exception('operating system not supported')

    @classmethod
    def term_cols(cls) -> int:
        return shutil.get_terminal_size().columns

    @classmethod
    def term_rows(cls) -> int:
        return shutil.get_terminal_size().lines

    @classmethod
    def get_size(cls) -> Tuple:
        return cls.term_rows(), cls.term_cols()

    @classmethod
    def style(cls, text: Text, *style) -> Text:
        return f'{"".join(style)}{text}{cls.OFF}' if style else text

    @classmethod
    def highligth(cls, pattern, text, *style) -> Text:
        """Apply a style to all matches of a regular expression pattern in a text.

        :param pattern: regular expression pattern to style to.
        :param text: text to apply the style to words matching the pattern.
        :param style: style to apply to the words that match the pattern.
        :return: text with text words matching the pattern styled.
        """
        positions = []
        for m in re.finditer(pattern, text, flags=re.MULTILINE):
            match = m
            if m:
                positions = [match.span()]

        if positions:
            for pos in positions:
                styled_text_range = cls.style(text[pos[0]:pos[1]], *style)
                text = text[:pos[0]] + styled_text_range + text[pos[1]:]

        return text

    @classmethod
    def color(cls, text: Text, *color: Color) -> Text:
        return cls.style(text, *color)

    # @classmethod
    # def colorize(cls, text: Text, color: str, *style) -> Text:
    #     return(cls.style(text, color, *style))
    #

    @classmethod
    def red(cls, text: Text) -> Text:
        """Format with color to a given text.

        :param text: text to apply the color to.
        :return: colored text.
        """
        return cls.color(text, cls.RED)

    @classmethod
    def cyan(cls, text: Text) -> Text:
        """Format with color to a given text.

        :param text: text to apply the color to.
        :return: colored text.
        """
        return cls.color(text, cls.CYAN)

    @classmethod
    def yellow(cls, text: Text) -> Text:
        """Format with color to a given text.

        :param text: text to apply the color to.
        :return: colored text.
        """
        return cls.color(text, cls.YELLOW)

    @classmethod
    def magenta(cls, text: Text) -> Text:
        """Format with color to a given text.

        :param text: text to apply the color to.
        :return: colored text.
        """
        return cls.color(text, cls.MAGENTA)

    @classmethod
    def white(cls, text: Text) -> Text:
        """Format with color to a given text.

        :param text: text to apply the color to.
        :return: colored text.
        """
        return cls.color(text, cls.WHITE)

    @classmethod
    def black(cls, text: Text) -> Text:
        """Format with color to a given text.

        :param text: text to apply the color to.
        :return: colored text.
        """
        return cls.color(text, cls.BLACK)

    @classmethod
    def blue(cls, text: Text) -> Text:
        """Format with color to a given text.

        :param text: text to apply the color to.
        :return: colored text.
        """
        return cls.color(text, cls.BLUE)

    @classmethod
    def green(cls, text: Text) -> Text:
        """Format with color to a given text.

        :param text: text to apply the color to.
        :return: colored text.
        """
        return cls.color(text, cls.GREEN)

    @classmethod
    def dim(cls, text: Text) -> Text:
        """Format with color to a given text.

        :param text: text to apply the color to.
        :return: colored text.
        """
        return cls.color(text, cls.DIM)

    @classmethod
    def bold(cls, text: Text) -> Text:
        """Format with color to a given text.

        :param text: text to apply the color to.
        :return: colored text.
        """
        return cls.color(text, cls.BOLD)

    def clear_lines(self, num: int = 1) -> NoReturn:
        """Clear the current line."""
        for n in range(num):
            self._send('\033[2K')
            self.up()

    def save_pos(self) -> NoReturn:
        """Save the current cursor position."""
        self._send('\033[s')

    def restore_pos(self) -> NoReturn:
        """Restore the last saved cursor position."""
        self._send('\033[u')

    def home(self) -> NoReturn:
        """Move the cursor to the home position."""
        self._send('\033[H')

    def hide_cursor(self) -> NoReturn:
        """Hide the cursor."""
        self._send('\033[?25l')

    def show_cursor(self) -> NoReturn:
        """Show the cursor."""
        self._send('\033[?25h')

    def underline(self, text: Text) -> Text:
        """Underline the given text.

        :param text: text to underline.
        :return: underlined text.
        """
        return self.style(text, self.UNDERLINE)

    def blink(self, text: Text) -> Text:
        """Blink the given text.

        :param text: text to blink.
        :return: blinked text.
        """
        return self.style(text, self.BLINK)

    def reverse(self, text: Text) -> Text:
        """Reverse the given text.

        :param text: text to reverse.
        :return: reversed text.
        """
        return self.style(text, self.REVERSE)

    def set_icon(self, icon: Text) -> NoReturn:
        """Set the terminal icon.

        :param icon: icon to set.
        """
        self._send(f'\033]1;{icon}\007')

    def clear_icon(self) -> NoReturn:
        """Clear the terminal icon."""
        self._send('\033]1;\007')

    def clear_to_end(self) -> NoReturn:
        """Clear the screen from the current position to the end."""
        self._send('\033[0J')

    def clear_from_start(self) -> NoReturn:
        """Clear the screen from the current position to the start."""
        self._send('\033[1J')

    def clear_line_to_end(self) -> NoReturn:
        """Clear the current line from the current position to the end."""
        self._send('\033[0K')

    def clear_line_from_start(self) -> NoReturn:
        """Clear the current line from the current position to the start."""
        self._send('\033[1K')
