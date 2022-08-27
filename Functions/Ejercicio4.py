#Define una función que convierta grados Farenheit en grados centígrados. (Para
#calcular los grados centígrados has de restar 32 a los grados Farenheit y multiplicar
#el resultado por cinco novenos).

def Convertidor_a_farenheit(num):
    centigrados = (num-32)*5/9
    return centigrados
temp = int(input("Ingrese cuantos grados Farenheit desea convertir: "))
print(Convertidor_a_farenheit(num=temp))
