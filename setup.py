#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='adebi',
    version="0.1.1",
    description='Automatic debian package dependency installer',
    author='Roman Mohr',
    author_email='roman@fenkhuber.at',
    install_requires=['argparse'],
    scripts=["adebi"],
)
