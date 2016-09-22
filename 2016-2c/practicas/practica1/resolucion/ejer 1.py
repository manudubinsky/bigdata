def capicua (s):

    a = list(s)
    b = len(a)-1
    c = list()

    for i in range (0,b):
        if (a[i] == a[b-i]):
            c.append(1)
        else:
            c.append(0)

    if 0 in c:
        print ("El string no es capicua")
    else:
        print ("El string es capicua")
        

s = raw_input ("Ingrese numero")
capicua(s)
