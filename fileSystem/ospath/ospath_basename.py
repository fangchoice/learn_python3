#!/usr/bin/env python
#-*- coding: utf-8 -*-

# basename() 函数返回一个等于值的第二部分的split()值

import os.path
PATHS = [
	'/one/two/three',
	'/one/two/three/',
	'/',
	'.',
	'',
]

for path in PATHS:
	print('{!r:>17} : {!r}'.format(path, os.path.basename(path)))
