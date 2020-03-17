# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt', encoding='utf8') as f:
    requirements = f.read().splitlines()

with open('README.rst', encoding="utf8") as f:
    readme = f.read()

with open('LICENSE', encoding="utf8") as f:
    license = f.read()

setup(
    name='broad',
    version='0.1',
    description='Broad Institute Coding Challenge',
    long_description=readme,
    author='Edmund Higham',
    author_email='edhigham@gmai..com',
    url='https://github.com/ehigham/broad-challenge',
    license=license,
    install_requires=requirements,
    packages=find_packages(exclude=('test', 'doc')),
    scripts=['challenge.py']
)