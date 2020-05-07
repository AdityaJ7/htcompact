#!/usr/bin/env python3

# Todo: test

from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()


setup(name='HTCompact',
      version='0.0.5',
      description='HTCondor summariser script',
      long_description=long_description,
      author='Mathis Loevenich',
      author_email='m.loevenich@fz-juelich.de',
      packages=find_packages(),
      install_requires=[
            "datetime",
            "configparser",
            "pandas",
            "tabulate"
      ],
      dependency_links=[
            'https://github.com/astanin/python-tabulate.git'
      ],
      python_requires='>=3.7',
      scripts=[
            'script/htcompact'
      ],
      )
