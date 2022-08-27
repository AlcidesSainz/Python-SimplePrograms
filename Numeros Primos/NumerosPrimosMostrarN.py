n = int(input("Ingrese la cantidad de numeros primos que desea mostrar: "))

print("Los primeros {} numeros primos son: ".format(n))
h = n*n+2
listaPrimos =[]

for i in range(2,h):
    creoQueEsPrimo = True

    for divisor in range(2,i):
        if i % divisor == 0:
            creoQueEsPrimo = False
            break
    
    if creoQueEsPrimo and len(listaPrimos)<n:
        listaPrimos.append(i)
print(listaPrimos)
