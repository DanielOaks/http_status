#!/usr/bin/env python
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <danneh@danneh.net> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return
# ----------------------------------------------------------------------------

from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='http-status',
    version='0.1.0a',
    description='HTTP Status codes, names, and descriptions.',
    long_description=long_description,
    author='Daniel Oaks',
    author_email='danneh@danneh.net',
    url='https://github.com/DanielOaks/http_status',
    packages=['http_status'],
    package_dir={'http_status': 'src/http_status'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
