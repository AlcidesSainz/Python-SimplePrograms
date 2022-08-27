#Define una función que convierta grados en radianes

from cmath import pi



def convertidor_grados_a_radianes(num):
    radianes = num * pi/180
    return radianes

temp = int(input("Ingrese cuantos grados se quieren convertir: "))
print(convertidor_grados_a_radianes(num=temp))
