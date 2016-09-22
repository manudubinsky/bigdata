#3.b) Escribir otro programa (fib2.py) similar al anterior que tome por línea de comando un nro. natural n y que imprima fib(n) pero que calcule cada término de la sucesión una sóla vez. Sugerencia: usar una lista que en cada posición tenga el valor de la función para cada n.

import time



def fibo_en_lista(n):

    lista.append(0)
    lista.append(1)   
    
    x=0

    y=1

    for i in range(n):

        lista.append(x+y)

        aux = x + y

        x = y

        y = aux
		
f = open("fib3.txt", "w")
lista=list()
n = int(input ("Ingrese un numero..."))

for i in range (0,int(n)+1):
    t0 = time.clock()
    for x in range (0,99):
        fibo_en_lista(i)
    t2 = (time.clock() - t0)/100
    print ("fibo ", i, " ", t2)
    
f.close()

