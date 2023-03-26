#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from pathlib import Path

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

if sys.version_info < (3, 6):
    raise NotImplementedError("Sorry, you need at least Python 3.6 to use py-term.")

import pyterm

readme_file = Path(__file__).parent / 'README.md'

if readme_file.is_file():
    long_desc = readme_file.read_text()
else:
    long_desc = pyterm.__doc__

setup(
    name='pyterm',
    version=pyterm.__version__,
    description='Python module to style terminal output, moving and positioning the cursor.',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    author='Havocesp',
    packages=find_packages(exclude=['tests', 'tests.*', 'examples', 'examples.*', 'docs', 'docs.*', 'venv', 'venv.*', 'build', 'build.*', 'dist', 'dist.*']),
    url='https://github.com/havocesp/pyterm',
    py_modules=['pyterm'],
    scripts=['pyterm'],
    license='MIT',
    platforms=['MacOSX', 'UNIX/Linux'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Topic :: Terminals',
        'Environment :: Console'
    ],
)
