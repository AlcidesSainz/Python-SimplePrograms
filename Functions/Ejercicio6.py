#Define una función que convierta radianes en grados. (Recuerda que 360 grados son 2π radianes)

from cmath import pi


def convertidor_radianes_a_grados(num):
    grados = num * 180/pi
    return grados

rad = int(input("Ingrese la los radianes que se desean convertir: "))

print(convertidor_radianes_a_grados(num=rad))