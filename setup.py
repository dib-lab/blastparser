#!/usr/bin/env python
from distutils.core import setup

setup(name='blastparser',
      version='0.1',
      description='A parser for regular BLAST, v2.2x',
      author='Chris Lee, C. Titus Brown',
      author_email='ctb@msu.edu',
      url='http://github.com/ged-lab/blastparser/',
      py_modules=['blastparser', 'parse_blast'],
      license='GPL',
      )
