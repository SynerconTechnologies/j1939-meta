from setuptools import setup

from j1939 import VERSION


setup(
    name="j1939-meta",
    version=VERSION,
    author="Patrick Forringer",
    author_email="patrick@forringer.com",
    url="https://github.com/SynerconTechnologies/j1939-meta",
    description="",
    packages=['j1939','j1587'],
    use_2to3=True)
