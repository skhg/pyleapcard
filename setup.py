#!/usr/bin/env python

from distutils.core import setup

setup(
    name='PyLeapCardAPI',
    version='0.0.1',
    description='Python Leap Card API',
    long_description='https://github.com/xt16johnny/pyleapcardapi for more details',
    keywords='leap card public transport smart card api travel ireland dublin home assistant hass',
    author='Johnny Moore',
    author_email='xt16.johnny+pypi@googlemail.com',
    url='https://github.com/xt16johnny/pyleapcardapi',
    packages=['pyleapcardapi'],
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
