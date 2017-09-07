# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="SBUX-Hack-a-thon",
    author_email="craig.j.smith@dell.com",
    url="",
    keywords=["Swagger", "SBUX-Hack-a-thon"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    long_description="""\
    This is a restful API endpoint to enable easy query access to the Starbucks fleet
    """
)

