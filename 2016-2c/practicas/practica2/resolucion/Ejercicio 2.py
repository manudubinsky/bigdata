#!/usr/bin/python
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import re
from operator import itemgetter

archivo = open("quijote.txt", "r")

archivoprocesado = ""

wordcount=0
cantlineas=0
listaPalabras = {}

for linea in archivo:
    linea = linea.lower()
    linea = re.sub(r'[,;.:"!?Â¡Â¿()-]', r'', linea)
    archivoprocesado = archivoprocesado + linea
    palabrasLinea = linea.split()
    wordcount=wordcount+len(palabrasLinea)
    for palabra in palabrasLinea:
        if palabra not in listaPalabras:
            listaPalabras[palabra] = 1
        else:
            listaPalabras[palabra] += 1

                
print "(a) El texto posee ", str(wordcount), " palabras"
diccionario = sorted(listaPalabras.items(), key=itemgetter(1))

print "(b) Palabras mas usadas: "

count = 0
for k,v in diccionario:
    count = count + 1
    if (count >= len(diccionario)-4):
        print "Palabra: ", k, " | Ocurrencia: ", v

archivo.close()

archivoprohibido = open ("punto c.txt", "r")

listaPalabrasProhibidas = list()

print "c) Filtrado de articulos y preprosiciones"

for lineas in archivoprohibido:
    palabrasProhibidas = lineas.split()
    for palabra2 in palabrasProhibidas:
        if palabra2 not in listaPalabrasProhibidas:
            listaPalabrasProhibidas.append(palabra2)

for i in listaPalabrasProhibidas:
    listaPalabras[i] = 0


diccionario2= sorted(listaPalabras.items(), key=itemgetter(1))
listaGraficoPalabras = list()
listaGraficoRepeticiones = list()

print "(d) Palabras mas usadas luego del filtrado: "

contador3 = 0
for z,x in diccionario2:
    contador3 = contador3 + 1
    if (contador3 >= len(diccionario2)-4):
        listaGraficoPalabras.append(z)
        listaGraficoRepeticiones.append(x)
        print "Palabra: ", z, " | Ocurrencia: ", x

print "(e) Histograma: "

xs = [i + 0.1 for i, _ in enumerate(listaGraficoPalabras)]
plt.bar(xs, listaGraficoRepeticiones)
plt.ylabel("Repeticiones")
plt.title("Palabras")
plt.xticks([i + 0.5 for i, _ in enumerate(listaGraficoPalabras)], listaGraficoPalabras)
plt.show()
