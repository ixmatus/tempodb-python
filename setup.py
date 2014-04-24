#!/usr/bin/env python
# encoding: utf-8
"""
tempodb/setup.py

Copyright (c) 2012 TempoDB Inc. All rights reserved.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


install_requires = [
    'python-dateutil >= 2.0',
    'requests >= 2.0',
    'simplejson',
    'six'
]

tests_require = [
    'mock',
    'unittest2',
]

setup(
    name="tempodb",
    version="0.5.0",
    author="TempoDB Inc",
    author_email="dev@tempo-db.com",
    url="http://github.com/getsentry/tempodb-python/",
    description="A client for the TempoDB API",
    packages=["tempodb"],
    long_description="A client for the TempoDB API.",
    dependency_links=[
    ],
    setup_requires=['nose>=1.0'],
    install_requires=install_requires,
    tests_require=tests_require,
)
