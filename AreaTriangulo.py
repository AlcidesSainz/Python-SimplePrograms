
from math import *
lado1 = float(input("Ingrese el valor del primero lado: "))
lado2 = float(input("Ingrese el valor del segundo lado: "))
angulo = int(input("Ingrese el angulo del triangulo: "))

#Convirtiendo el angulo a radianes
angulo *= pi/180
angulo = sin(angulo)
print("La conversion del angulo es: ","{0:.3}".format(angulo))

#Aritmetica del triangulo
area = 1/2*lado1*lado2*angulo
print("El area del triangulo es: {0:.3}".format(area))



