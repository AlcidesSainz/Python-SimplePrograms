#Diseña una función que devuelva una lista con los números perfectos comprendidos
#entre 1 y n, siendo n un entero que nos proporciona el usuario.

def numero_perfecto(num):
    #Hallando los divisores del numero que se va a ingresar
    sum_div = 0
    maxDiv = num//2 
    for divisor in range(1,maxDiv+1):
        if(num % divisor) == 0 :
            sum_div+=divisor
    #Verificando numero perfecto
    return num == sum_div
n = int(input("Ingrese n: "))
_list = []
for i in range(1,n+1):
    if numero_perfecto(num=i):
        _list.append(i)
print(*_list)