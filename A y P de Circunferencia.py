"""Diseña un programa legible que solicite el radio de una circunferencia y
muestre su área y perímetro con solo 2 decimales. """
from math import *
#Pidiendo el valor de la radio
radio = float(input("Ingrese el valor de la radio: "))
#Formula del area
area = pi*(radio**2)
#Formula del perimetro
perimetro = 2*pi*radio
#Mostrando los resultados
print("El area de la circunferencia es: {0:.2f}".format(area),"centimentros cuadrados")
print("El perimetro de la circunferencia es: {0:.2f}".format(perimetro),"cm")


