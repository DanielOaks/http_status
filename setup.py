#!/usr/bin/env python
# written by Daniel Oaks <daniel@danieloaks.net>
# licensed under the BSD 2-clause license

from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='http-status',
    version='0.1.1b',
    description='HTTP Status codes, names, and descriptions.',
    long_description=long_description,
    author='Daniel Oaks, Chad Nelson',
    author_email='daniel@danieloaks.net',
    url='https://github.com/DanielOaks/http_status',
    packages=['http_status'],
    package_dir={'http_status': 'src/http_status'},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
