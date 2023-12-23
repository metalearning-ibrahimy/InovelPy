from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()

setup(
    name='InovelPy',
    version='1.0.1',
    license='GNU',
    author='Taufiqurrahman',
    author_email='metalearning@pps-ibrahimy.ac.id',
    url='https://github.com/metalearning-ibrahimy/InovelPy',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
      'joblib',
      'scikit-learn',
      'glob2',
      'tqdm',
      "networkx",
      'python-louvain',
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
    description='The goal of this package is to help scientometrician work with novelty indicators.',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
