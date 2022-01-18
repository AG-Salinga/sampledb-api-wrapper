import os
from codecs import open  # To use a consistent encoding

from setuptools import find_packages, setup  # Prefer setuptools over distutils

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with open(os.path.join(here, "doc/description.rst"), encoding="utf-8") as f:
    long_description = f.read()

# with open("requirements.txt") as f:
#     requirements = f.read().splitlines()


out = setup(
    name="sampledbapi",

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version="0.3.1",

    description="API wrapper for SampleDB",
    long_description=long_description,

    # The project's main homepage.
    url="https://zivgitlab.uni-muenster.de/ag-salinga/sampledb-api-wrapper",

    # Author details
    author="AG Salinga, WWU Münster",
    author_email="itsaling@uni-muenster.de",

    # Choose your license
    license="MIT",

    # See https://PyPI.python.org/PyPI?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",

        # Indicate who your project is intended for
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",

        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: MIT License",

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],

    # What does your project relate to?
    keywords="api sampledb",

    packages=["sampledbapi"],

    package_dir={"sampledbapi": "./sampledbapi"},

    package_data={"": []},

    data_files=[],

    # Requirements
    # install_requires=requirements,

    # Entry point (none so far)
    # entry_points={
    #     "console_scripts": [
    #         "puzzlestream = puzzlestream.launch:launchPuzzlestream",
    #     ]
    # },
)
