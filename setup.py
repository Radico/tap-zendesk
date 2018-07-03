#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-zendesk",
    version="0.1.0",
    description="Singer.io tap for extracting data from zendesk",
    author="Simon Data",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_zendesk"],
    install_requires=[
        "singer-python==5.1.5",
        "requests",
        "pendulum==1.2.0"
    ],
    entry_points="""
    [console_scripts]
    tap-zendesk=tap_zendesk:main
    """,
    packages=["tap_zendesk"],
    package_data={
        "schemas": ["tap_zendesk/schemas/*.json"]
    },
    include_package_data=True,
)
