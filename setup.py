#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools.command.test import test as TestCommand
from setuptools import setup, find_packages

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]
    def initialize_options(self):
        TestCommand.initialize_options(self) 
        self.pytest_args = []

    def finalize_options(self): 
        TestCommand.finalize_options(self) 
        self.test_args = [] 
        self.test_suite = True

def run_tests(self):
#import here, cause outside the eggs aren't loaded import pytest
    errno = pytest.main(self.pytest_args) 
    sys.exit(errno)

setup(
    name     = 'webdavclient',
    version  = '0.3.0',
    packages = find_packages(),
    requires = ['python (>= 2.7.6)'],
    install_requires=['pycurl', 'lxml'],
    scripts = ['wdc'],
    description  = 'Webdav API, resource API and webdav tool for WebDAV services (Яндекс.Диск, Dropbox, Google Диск, Box и 4shared)',
    long_description = open('README.rst').read(),
    author = 'Designerror',
    author_email = 'designerror@yandex.ru',
    url          = 'https://github.com/designerror/webdavclient',
    download_url = 'https://github.com/designerror/webdavclient/tarball/master',
    license      = 'MIT License',
    keywords     = 'webdav, client, python, module, library, packet, Яндекс.Диск, Dropbox, Google Диск, Box, 4shared',
    classifiers  = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    tests_require=['pytest'],
    cmdclass = {'test': PyTest},
)
