from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()

setup(
    name='InovelPy',
    version='0.0.1',
    license='GNU',
    author='Taufiqurrahman',
    author_email='taufiqurrahman.info@gmail.com',
    url='https://github.com/metalearning-ibrahimy/InovelPy',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
      'pymongo',
      'joblib',
      'sklearn',
      'glob2',
      'tqdm',
      "networkx",
      'python-louvai',
      'numpy',
      'pickle-mixin',
      'scipy',
      'pandas',
      'multiprocess',
      'pyyaml',
      'spacy',
      'scispacy',
      'cycler',
      'thinc',
      'wosfile',
      'seaborn'
    ],
    zip_safe=True,
    description='he goal of this package is to help scientometrician work with novelty indicators.',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
