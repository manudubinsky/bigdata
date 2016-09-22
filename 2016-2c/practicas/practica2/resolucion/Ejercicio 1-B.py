#!/usr/bin/python

import re


str = input ("ingrese un nombre,apellido,dni")

tupla = re.findall(r'[A-Z][a-z]+', str)

print (tupla)
i = 0
while (i < len(tupla)-1):
	print ("Nombre: " + tupla[i] + " Apellido:" + tupla[i+1])
	i = i + 2

