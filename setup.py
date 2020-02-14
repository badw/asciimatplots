"""
vasp-analysis: a "teach yourself python" tools made useful
"""

from os.path import abspath, dirname
from setuptools import setup, find_packages

project_dir = abspath(dirname(__file__))

setup(
    name='asciimatplots',
    version='1.0.0',
    description='ascii plots for various aspects of materials dft',
    url="https://github.com/badw/asciimatplots",
    author="Benjamin A. D. Williamson",
    author_email="benjamin.williamson@ntnu.no",
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics'
        ],
    keywords='chemistry pymatgen physics dft vasp',
    packages=find_packages(),
    install_requires=['colorama','termplotlib', 'numpy', 'pymatgen'],
    entry_points={'console_scripts': [
                      'ascii-converge = asciimatplots.converge_status:main']},
    )
