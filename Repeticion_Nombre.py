"""Haz un programa que pida el nombre de una persona y lo muestre en pantalla
repetido 1000 veces, pero dejando un espacio de separación entre aparición y
aparición del nombre. (Utiliza los operadores de concatenación y repetición)."""
import string

#Pidiendo el dato al usuario
nombre = str(input("Ingrese un nombre: "))
#Mostrando el dato repetido 1000 veces
print((nombre+" ")*1000)