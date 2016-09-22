

palabras = dict()
palabra = ''
listaMap = []

#Map
f = open('quijote.txt', 'r')
for line in f:
	for c in line:
		if c != " " and  c != "," and c != ";" and c!="." and c != '\n' :
			palabra = palabra + c
		else:
			listaMap.append((palabra, 1))
			palabra = ''

f.close()

#Reduce
for item in listaMap:
		if(palabras.has_key(item[0])):
			palabras[item[0]] = palabras.get(item[0]) + 1
		else:
			palabras[item[0]] = 1
			
print str(palabras)