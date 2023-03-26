#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pyterm

 - File: pyterm/utils.py
 - Author: Havocesp <https://github.com/havocesp/pyterm>
 - Created: 2023-03-26
 -
"""


def get_caller_name() -> str:
    """Get the caller name."""
    import inspect
    return inspect.stack()[2][3]
