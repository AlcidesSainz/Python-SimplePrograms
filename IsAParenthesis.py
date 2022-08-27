from ast import Str


a = ")"
b = "("

caracter = str(input("Type a character: "))

if caracter == a or caracter == b:
    print("Is parenthesis")
else:
    print("Not is a parenthesis")