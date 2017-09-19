#!/usr/bin/env python

from distutils.core import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pyleapcard',
      version='0.1.1',
      description='Python Leap Card API',
      long_description=readme(),
      keywords='leap card public transport smart card api travel ireland',
      author='Jack Higgins',
      author_email='pypi@jackhiggins.ie',
      url='https://github.com/skhg/pyleapcard',
      packages=['pyleapcard'],
      install_requires=[
          'requests',
          'bs4'
      ],
      tests_require = [
	  	'mock',
	    'nose',
	  ],
      license='MIT'
      )