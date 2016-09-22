#!/usr/bin/python

import re

s = "Hola ... Chau."
match = re.search(r'\.\.\.', s)
if match:
	print match.group()
