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
		


lista=list()
n = int(input ("Ingrese un numero..."))
t0 = time.clock()
fibo_en_lista(n)
print ("resultado final: ",max(lista))
print ("El tiempo de ejecuion fue:",time.clock()-t0)


