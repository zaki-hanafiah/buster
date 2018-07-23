#!/usr/bin/env python

from setuptools import setup

from buster import version

setup(name="buster",
      version=version,
      description="Static site generator for Ghost and Github",
      long_description=open("README.rst").read(),
      author="Akshit Khurana",
      author_email="axitkhurana@gmail.com",
      url="https://github.com/boggin/buster",
      license="MIT",
      packages=["buster"],
      entry_points={"console_scripts": ["buster = buster.buster:main"]},
      install_requires=['GitPython==2.1.7', 'future',
                        'pyquery==1.2.8', 'python-dateutil']
      )
