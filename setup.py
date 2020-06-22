#!/usr/bin/env python

from distutils.core import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyleapcard',
    version='0.0.0',
    description="Python Leap Card API (Unofficial). Access your card balance and journey history for Ireland's public "
                "transport smart card.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='leap card public transport smart card api travel ireland',
    author='Jack Higgins',
    author_email='pypi@jackhiggins.ie',
    url='https://github.com/skhg/pyleapcard',
    packages=['pyleapcard'],
    install_requires=[
        'requests',
        'bs4'
    ],
    tests_require=[
        'mock',
        'nose',
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'])
