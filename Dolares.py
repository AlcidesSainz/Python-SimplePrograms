"""Haz un programa que pida al usuario una cantidad de dólares, una tasa de
interés y un número de años. Muestra por pantalla en cuánto se habrá
convertido el capital inicial transcurridos esos años si cada año se aplica la
tasa de interés introducida.
Recuerda que un capital de C dólares a un interés del x por cien durante n años
se convierten en C · (1 + x/100)n dólares. (Prueba tu programa sabiendo que 
una cantidad de $10,000 al 4.5 % de interés anual se convierte en $24,117.14
al cabo de 20 años)."""

#Pidiendo los datos
dolares = float(input("Ingrese la cantidad de dolares: "))
tasa_interes = float(input("Ingrese la tasa de interes: "))
años = int(input("Ingrese el numero de años: "))

#Formula de la tasa de interes
dolares*=(1+tasa_interes/100)**años

#Mostrando el resultado
print("La cantidad de dolares total es: $ {0:.2f}".format(dolares),)


