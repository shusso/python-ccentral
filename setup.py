#!/usr/bin/env python
# coding=utf8

from setuptools import setup

setup(
    name='CCentral',
    version="0.3.4",
    description='CCentral client library',
    author='Santtu Järvi',
    author_email='santtu.jarvi@finfur.net',
    url='https://github.com/slvwolf/python-ccentral',
    packages=['ccentral'],
    requires=["etcd", 'pyformance'],
    install_requires=["python-etcd>=0.4.3"],
    classifiers=["Programming Language :: Python :: 2.7",
                 "Programming Language :: Python :: 3.5"]
)
