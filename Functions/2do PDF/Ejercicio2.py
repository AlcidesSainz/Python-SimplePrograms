#Diseñar una función que nos diga si un número dado es o no es perfecto. Se dice que un
#número es perfecto si es igual a la suma de todos sus divisores excluído él mismo. Por
#ejemplo, 28 es un número perfecto, pues sus divisores (excepto él mismo) son 1, 2, 4, 7
#y 14, que suman 28.
def numero_perfecto(num):
    #Hallando los divisores del numero que se va a ingresar
    sum_div = 0
    maxDiv = num//2 
    for divisor in range(1,maxDiv+1):
        if(num % divisor) == 0 :
            print(divisor, " es divisor")
            sum_div+=divisor
    #Sumando los divisores
    print("La suma de los divisores es: ",sum_div)
    #Verificando numero perfecto
    if(num == sum_div):
        print("El numero: ", num, " es perfecto")
    else:
        print("El numero: ",num," NO es perfecto")
num1= int(input("Ingrese un numero: "))
numero_perfecto(num=num1)
