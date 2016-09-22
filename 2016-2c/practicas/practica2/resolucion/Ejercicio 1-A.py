import re

str = input("Ingrese un numero romano")
match = re.search(r'^[\sXxVvIiCcDdMmLl]+$', str)
if match:                      
	print ("Es un numero romano papa"), match.group() ## 'found word:cat'
else:
	print ("Nada que ver")
