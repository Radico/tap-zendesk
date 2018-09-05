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
        "singer-python==5.2.0",
        'requests==2.18.4',
        "pendulum==1.2.0",
    ],
    entry_points="""
    [console_scripts]
    tap-zendesk=tap_zendesk:main
    tap-zendesk-kit=tap_zendesk.kit:main
    """,
    packages=["tap_zendesk"],
    package_data={
        "schemas": ["tap_zendesk/schemas/*.json"]
    },
    include_package_data=True,
)
