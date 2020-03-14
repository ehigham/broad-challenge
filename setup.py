# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='broad',
    version='0.1.0',
    description='Broad Institute Coding Challenge',
    long_description=readme,
    author='Edmund Higham',
    author_email='edhigham@gmai..com',
    url='https://github.com/ehigham/broad-challenge',
    license=license,
    packages=find_packages(exclude=('test', 'doc'))
)