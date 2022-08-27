#Define una función que convierta grados centígrados en grados Farenheit
 
def convertidor_a_farenheit(num):
    farenheit = (num*9/5) + 32
    return farenheit
temp = int(input("Ingrese los grados centigrados que desea convertir a Farenheit: "))
print(convertidor_a_farenheit(num=temp))
