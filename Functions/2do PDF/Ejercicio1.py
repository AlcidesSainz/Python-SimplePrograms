#Diseña una función que reciba una cadena y devuelva cierto si empieza por minúscula y falso en caso contrario.
#var primeraLetra = el primer caracter de la frase substring   string es un arreglo de caracteres  caracter[0]
#var lowerLetra = primeraLetra.lower() lo guardo en una variable
# return primeraLetra == lowerLetra 
def cadenaTF(cadena):
    primera_letra = cadena[0].lower()

    return primera_letra == cadena[0]
        
   
cadenaN = str(input("Ingrese una frase: "))
print (cadenaTF(cadena=cadenaN))
