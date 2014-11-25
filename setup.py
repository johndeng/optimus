#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='Optimus',
    author='John Deng',
    version='0.0.1',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'Click',
        'jinja2'
    ],
    entry_points='''
        [console_scripts]
        optimus=optimus.optimus:main
    '''
)
