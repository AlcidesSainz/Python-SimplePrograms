#Define una función llamada raíz_cúbica que devuelva el valor de 3√x. (Nota: recuerda
#que la notación 3√x no es más que una forma de expresar x1/3).

def raiz_cubica(num):
    raiz = num**(1/3)
    return raiz

print(raiz_cubica(num=27))

