#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import drf_nested_resource

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = drf_nested_resource.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-rest-framework-nested-resource',
    version=version,
    description="""DRF view mixin for nested resources""",
    long_description=readme + '\n\n' + history,
    author='SimpleEnergy',
    author_email='piper@simpleenergy.com',
    url='https://github.com/simpleenergy/django-rest-framework-nested-resource',
    packages=[
        'drf_nested_resource',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-rest-framework-nested-resource',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)