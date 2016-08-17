#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='transformers',
      version='0.1',
      description="Experimental module for AST transformations.",
      author='Vladimir Iakovlev',
      author_email='nvbn.rm@gmail.com',
      url='https://github.com/nvbn/__transformers__',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples',
                                      'tests', 'tests.*', 'release']))
