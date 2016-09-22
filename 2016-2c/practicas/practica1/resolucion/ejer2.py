def productointerno (a,b):
    z = len(a)
    sum = 0
    
    if (len(a) != len(b)):
        print ("Error")
    else:    
        for i in range (0, z):
            prod = int(a[i]) * int(b[i])
            sum = sum + prod
            
        print(sum)

a = list(raw_input("Ingrese vector 1 "))
b = list(raw_input("Ingrese vector 2 "))

productointerno(a,b)
