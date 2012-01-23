import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
        name="dinero",
        version="0.0.1",
        packages=["dinero", "dinero.gateways"],
        author="Fusionbox Programmers",
        author_email="programmers@fusionbox.com",
        keywords="dinero authorize.net payments",
        description="Gateway-agnostic payment processing.",
        long_description=read("README.md"),
        url="https://github.com/fusionbox/dinero",
        platforms="any",
        license="BSD",
        install_requires=['lxml', 'requests'],
        )
