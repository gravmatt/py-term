#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pyterm

 - File: pyterm/__init__.py
 - Author: Havocesp <https://github.com/havocesp/pyterm>
 - Created: 2023-03-22
 -
"""
from pyterm.constants import __all_constants__
from pyterm.core import Term
from pyterm.model import Color

Tm = Term

__version__ = '0.7.2'

__all__ = [
    'Term',
    'Tm',
    'Color',
    '__version__',
    *__all_constants__
]
