#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module contains the specification of the mmworkbench package"""
# pylint: disable=locally-disabled,invalid-name
from setuptools import setup

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click~=7.1',
    'click-log==0.1.8',
    'elasticsearch5~=5.5',
    'Flask~=1.0',
    'Flask-Cors~=3.0',
    'nltk~=3.2',
    'numpy~=1.14',
    'pandas~=0.22',
    'pip>=9.0.1',
    'py~=1.4',
    'python-dateutil~=2.6',
    'pytz>=2017.2',
    'requests~=2.20',
    'scipy>=0.9,<2.0',
    'scikit-learn>=0.18.1,<0.20',
    'tqdm~=4.15',
    'python-crfsuite~=0.9',
    'sklearn-crfsuite>=0.3.6,<1.0',
    'distro~=1.3'
]

setup_requirements = [
    'pytest-runner~=2.11',
    'setuptools>=36',
]

test_requirements = [
    'flake8==3.2.1',
    'pylint==1.6.5',
    'pytest==3.0.5',
    'pytest-cov==2.4.0',
    'pytest-asyncio==0.8.0'
]

setup(
    name='mmworkbench',
    version='4.0.0post12',
    description="A Python module for building natural language processing models.",
    long_description=history,
    author="MindMeld, Inc.",
    author_email='contact@mindmeld.com',
    url='https://github.com/mindmeld/mindmeld-workbench3',
    packages=[
        'mmworkbench',
    ],
    package_dir={'mmworkbench': 'mmworkbench'},
    entry_points={
        'console_scripts': ['mmworkbench=mmworkbench.cli:cli']
    },
    include_package_data=True,
    install_requires=requirements,
    extras_require={'tensorflow': ['tensorflow~=1.2']},
    zip_safe=False,
    keywords='mindmeld',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements
)
