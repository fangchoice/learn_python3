#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dirname() 函数返回拆分路径的第一部分

import os.path

PATHS = [
	'/one/two/three/',
	'/one/two/three',
	'/',
	'.',
	'',
]

for path in PATHS:
	print('{!r:>17} : {!r}'.format(path, os.path.dirname(path)))
