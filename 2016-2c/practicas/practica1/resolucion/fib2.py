#3.b) Escribir otro programa (fib2.py) similar al anterior que tome por línea de comando un nro. natural n y que imprima fib(n) pero que calcule cada término de la sucesión una sóla vez. Sugerencia: usar una lista que en cada posición tenga el valor de la función para cada n.

import time
def fibo(x):
        return (lista[x-2] + lista[x-1])

def fibo_en_lista(n):
    for i in range (0,n+1):
            if (i > len(lista)-1):
                lista.append(fibo(i))		
		
lista=list()
lista.append(0)
lista.append(1)

n = int(input ("Ingrese un numero..."))
t0 = time.clock()
fibo_en_lista(n)

print(lista[n])
print 'El tiempo de ejecucion fue:',time.clock()-t0
