#Implementa un programa que muestre todos los números potencia de 2 entre 2**0 y 2**30,ambos inclusive.

i=0
potencia=0

while i!=31:
    potencia = 2**i
    print("2 elevado a: ",i," es igual a: ",potencia)
    i+=1
