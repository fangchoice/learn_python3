# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import os.path

for user in ['', 'dhellmann', 'nosuchuser']:
	lookup = '~' + user
	print('{!r:>15} : {!r}'.format(lookup, os.path.expanduser(lookup)))
