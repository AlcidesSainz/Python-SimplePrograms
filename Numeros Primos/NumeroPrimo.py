#Mostrar si el numero ingresado es primo o no

num = int(input("Ingrese un numero: "))

if num > 1:
    cont =0
    for div in range(2,num):
        rest = num%div
        if rest == 0:
            cont+=1
    if cont ==0:
        print("El numero {} es un numero primo".format(num))
    else:
        print("El numero {} no es un numero primo".format(num))
else:
    print("El numero {} no es un numero primo".format(num))