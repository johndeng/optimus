#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='py-optimus',
    author='John Deng',
    author_email='denghuanzhong@gmail.com',
    version='0.0.1',
    description='Optimus is a Python web framework project constructor.',
    url='http://github.com/johndeng/optimus',
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
