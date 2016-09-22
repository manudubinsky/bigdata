#!/usr/bin/python

import re


str2 = 'hola, aca; estoy :"" (salame) ---'


print (re.sub(r'[,;.:"!?¡¿()-]', r'', str2))
