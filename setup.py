#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name = 'robotframework-websocketclient',
    packages = ['robotframework-websocketclient'],
    version = '0.3',
    description = '	Robot Framework keywords for websocket-client',
    author = 'Damien Le Bourdonnec',
    author_email = 'damien.lebourdonnec@gmail.com',
    url = 'https://github.com/greums/robotframework-websocketclient',
    download_url = 'https://github.com/greums/robotframework-websocketclient/tarball/0.3',
    keywords = ['robotframework', 'websocket'],
    install_requires=[
        'websocket-client'
    ],
    classifiers = []
)
