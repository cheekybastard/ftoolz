#!/usr/bin/env python

from os.path import exists

from setuptools import find_packages, setup
from setuptools.dist import Distribution

import pytoolz


class BinaryDistribution(Distribution):
    """Distribution which always forces a binary package with platform name"""

    def has_ext_modules(self) -> bool:
        return True


test_requirements = [
    'coverage==4.5.1',
    'flake8==3.7.7',
    'mypy==0.700',
    'nose==1.3.7',
    # 'nose2==0.8.0',
    # 'nose2[coverage_plugin]>=0.6.5',
    'pylint==2.3.0',
]

setup(
    name='pytoolz',
    version=pytoolz.__version__,
    description='Collection of higher-order and utility functions',
    long_description=(open('README.md').read() if exists('README.md') else ''),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    url='https://bitbucket.org/blindspotsolutions/pytoolz/',
    maintainer='Martin Matyasek',
    maintainer_email='martin.matyasek@blindspot.ai',
    keywords='functional utility cytoolz itertools functools',
    packages=find_packages(include=['pytoolz']),
    include_package_data=True,
    distclass=BinaryDistribution,
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=['cytoolz==0.9.0.1'] + test_requirements,
    test_suite='tests',
    tests_require=test_requirements,
)
