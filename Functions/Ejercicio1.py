#Define una función la reciba como parámetro 2 números enteros y nos devuelva la    suma de estos.

def suma(num1,num2):
    sumaNum = num1+num2
    return sumaNum

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
print(suma(num1,num2))
