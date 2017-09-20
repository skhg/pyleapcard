#!/usr/bin/env python

from distutils.core import setup

setup(name='pyleapcard',
      version='0.1.3',
      description='Python Leap Card API',
      long_description='See project page with usage examples at https://github.com/skhg/pyleapcard',
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
      license='MIT',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6',
      ]
      )