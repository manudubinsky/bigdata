import re

palabras = {}
palabrasp = {}
palabras2 = {}
lista1=[]
lista=[]
lista2=[]
listap=[]
contador =0

#Cargo Archivo a lista y cuento palabras
f = open('quijote.txt', 'r')
for line in f:
	lista = line.lower().split(" ") #paso a minusculas
	for p in lista:
		contador=contador+1
		p=re.sub(r'\n',r'',p) #elimino \n 
		if p in palabras.keys():
			palabras[p]+=1
		else:
			palabras[p]=1
	print contador
f.close()

print ("1) Cantidad de palabras: " + str(contador))
#Ordeno lista
ordenada = sorted(palabras.items(), key=lambda x:x[1], reverse=True)

print ("2) 5 Palabras mas usadas" + str(ordenada[0:5]))

#Cargo palabras prohibidas a lista
p = open('prohibidas.txt', 'r')
for l in p:
	l=re.sub(r'\n',r'',l)#elimino \n
	listap.append(l)
p.close()
print ("3) Lista de palabras prohibidas" )
print(listap)

#Filtro palabras prohibidas
contador=0
#Cargo Archivo a lista y cuento palabras
f = open('quijote.txt', 'r')
for line in f:
	lista1 = line.lower().split(" ") #paso a minusculas
	for p in lista1:
		if p not in listap:
			contador=contador+1
			p=re.sub(r'\n',r'',p) #elimino \n 
			if p in palabrasp.keys():
				palabrasp[p]+=1
			else:
				palabrasp[p]=1
f.close()


#Ordeno lista
sortedp = sorted(palabrasp.items(), key=lambda x:x[1], reverse=True) 


print ("4) Cantidad de palabras: " + str(contador))
print ("5 Palabras mas usadas" + str(sortedp[0:5]))


#Cargo Archivo a lista y cuento palabras
f = open('rey_lear.txt', 'r')
contador=0
for line in f:
	lista2 = line.lower().split(" ") #paso a minusculas
	for p in lista2:
		contador=contador+1
		p=re.sub(r'\n',r'',p) #elimino \n 
		if p in palabras2.keys():
			palabras2[p]+=1
		else:
			palabras2[p]=1
f.close()


print ("5) Cantidad de palabras: " + str(contador))
#Ordeno lista
ordenada2 = sorted(palabras2.items(), key=lambda x:x[1], reverse=True)

print (" 5 Palabras mas usadas" + str(ordenada[0:5]))




