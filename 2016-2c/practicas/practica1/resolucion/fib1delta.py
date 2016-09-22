import time

def fibo(n):
    if (n == 1):
        return 1

    elif (n == 0):
        return 0

    else:
        return fibo(n-1) + fibo(n-2)
f = open("fib1.txt", "w")
n = input ("Ingrese un numero...")

for i in range (0,int(n)+1):
    t0 = time.clock()
    for x in range (0,99):
        fibo(i)
    t2 = (time.clock() - t0)/100
    print ("fibo ", i, " ", t2)
        
f.close()
