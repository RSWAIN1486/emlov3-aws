#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="src",
    version="1.0.0",
    description="Demo for GPT Script model for Harry Potter",
    author="",
    author_email="",
    url="https://github.com/RSWAIN1486/emlov3-aws",
    install_requires=["lightning", "hydra-core"],
    packages=find_packages(),
    # use this to customize global commands available in the terminal after installing the package
    entry_points={
        "console_scripts": [
            "demo_jit_script_gpt = demo_jit_script_gpt:main",
        ]
    },
)