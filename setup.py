from setuptools import setup, find_packages
import sys
import os

setup(name='Cog_BCI',
      version='0.0.0',
      description='A lib for controlling OpenBCI Devices',
      author='GRIK Research Group',
      author_email='notAtThisMoment@gmail.com',
      license='TBD',
      packages=find_packages(),
      install_requires=['numpy', 'openbci-python'],
      url='https://github.com/grik/Cog_BCI',  # use the URL to the github repo
      download_url='https://github.com/grik/Cog_BCI.git',
      keywords=['device', 'control', 'eeg', 'openbci', 'ganglion', 'cyton', 'bci'],
      zip_safe=False)
