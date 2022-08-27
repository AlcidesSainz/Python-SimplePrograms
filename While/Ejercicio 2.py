#Implementa un programa que muestre todos los múltiplos de n entre n y m · n, ambos
#inclusive, donde n y m son números introducidos por el usuario.

n = int(input("Ingrese el valor de n: "))
m = int(input("Ingrese el valor de m: "))
limite = n*m
i = 1
multiplo = 0

while multiplo<limite:
    multiplo = n*i
    print(multiplo)
    i+=1