#!/usr/bin/env python

import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info < (2, 6):
    raise NotImplementedError("Sorry, you need at least Python 2.6 or Python 3.2+ to use py-term.")

import term

with open('README.rst', 'r') as f:
    longDesc = f.read()

setup(name='py-term',
      version=term.__version__,
      description='Python module to style terminal output, moving and positioning the cursor.',
      long_description=longDesc,
      author='Rene Tanczos',
      author_email='gravmatt@gmail.com',
      url='https://github.com/gravmatt/py-term',
      py_modules=['term'],
      scripts=['term.py'],
      license='MIT',
      platforms=['MacOSX', 'UNIX/Linux'],
      classifiers=['Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2.5',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Intended Audience :: Developers',
                   'Programming Language :: Python',
                   'Development Status :: 5 - Production/Stable',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: POSIX',
                   'Topic :: Terminals',
                   'Environment :: Console'
                   ],
      )
