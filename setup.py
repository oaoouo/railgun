# encoding: utf-8
"""
    railgun~setup
    `````````````

    > static site generator

    :License: MIT
    :Copyright: @oaoouo
"""

import re
import ast
import cli
from setuptools import setup, find_packages

# version
_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('cli/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')
    ).group(1)))

# entry_points
entry_points = {
    'console_scripts':[
        'railgun=cli.railgun:cli'
    ]
}

# setup
setup(
    name='railgun_cli',
    version=version,
    packages=find_packages(),
    url='https://github.com/oaoouo/railgun',
    license='MIT',
    author='oaoouo',
    author_email='oaoouo@yeah.net',
    description='static site generator',
    long_description=__doc__,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'click',
        'Flask',
        'Flask-Flatpages',
        'Flask-Script',
    ],
    entry_points=entry_points,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
