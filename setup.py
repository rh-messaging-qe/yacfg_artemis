#!/usr/bin/env python

# Copyright 2018-2020 Red Hat Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

setup(
    name="yacfg-artemis",
    version="0.1",
    packages=[
        'yacfg.profiles.artemis',
        'yacfg.templates.artemis'
    ],
    package_dir={'': 'src'},
    install_requires=[
        'yacfg'
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest'
    ],
    url='https://github.com/rh-messaging-qe/yacfg-artemis',
    license='Apache-2.0',
    author='Zdenek Kraus',
    author_email='zkraus@redhat.com',
    maintainer="Dominik Lenoch",
    maintainer_email="dlenoch@redhat.com",
    description="",
    long_description="",
    package_data={
        'yacfg.profiles.artemis': [
            'src/yacfg/profiles/artemis*'
        ],
        'yacfg.templates.artemis': [
            'src/yacfg/templates/artemis*'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Systems Administration',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ],
)
