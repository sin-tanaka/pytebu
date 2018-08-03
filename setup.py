#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

required = [
    'requests-html',
    'prettytable'
]
setuptools.setup(
    name="pytebu",
    version="0.0.1",
    author="sin-tanaka",
    author_email="sin_tanaka@jsl.co.jp",
    description='Command Line Client for Hatena Bookmark HotEntry',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/sin-tanaka/pytebu',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        "console_scripts": [
            "pytebu=pytebu.pytebu:cli",
        ]
    },
    install_requires=required
)
