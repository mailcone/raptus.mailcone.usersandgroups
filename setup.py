from setuptools import setup, find_packages
import os

version = '1.0a1'

setup(name='raptus.mailcone.usersandgroups',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Samuel Riolo',
      author_email='sriolo@raptus.com',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['raptus','raptus.mailcone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'setuptools',

      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
