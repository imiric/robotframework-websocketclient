#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
setup(
  name = 'robotframework-websocketclient',
  packages = ['robotframework-websocketclient'],
  version = '0.1',
  description = '	Robot Framework keywords for websocket-client',
  author = 'Damien Le Bourdonnec',
  author_email = 'damien.lebourdonnec@gmail.com',
  url = 'https://github.com/greums/robotframework-websocketclient',
  download_url = 'https://github.com/greums/robotframework-websocketclient/tarball/0.1',
  keywords = ['robotframework', 'websocket'],
  install_requires=['websocket-client'],
  classifiers = [],
)
