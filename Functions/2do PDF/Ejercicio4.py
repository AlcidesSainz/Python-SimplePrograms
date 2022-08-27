# #Define una función que devuelva el número de días que tiene un año determinado. Ten
# #en cuenta que un año es bisiesto si es divisible por 4 y no divisible por 100, excepto si
# #es también divisible por 400, en cuyo caso es bisiesto.

# (Ejemplos: El número de días de 2002 es 365: el número 2002 no es divisible por 4, así
# que no es bisiesto. El año 2004 es bisiesto y tiene 366 días: el número 2004 es divisible
# por 4, pero no por 100, así que es bisiesto. El año 1900 es divisible por 4, pero no es
# bisiesto porque es divisible por 100 y no por 400. El año 2000 sí es bisiesto: el número
# 2000 es divisible por 4 y, aunque es divisible por 100, también lo es por 400).
def anioBisiesto(anioN):
    p= anioN % 4 == 0
    q= anioN % 100 == 0
    r= anioN % 400 == 0

    return p and (not q or r)

anio = int(input("Ingrese un anio: "))
if anioBisiesto(anioN=anio): 
    print(anioBisiesto(anioN=anio))
    print("El anio ", anio, " es bisiesto y tiene 366 dias")
else:
     print("El anio ", anio, " NO es bisiesto y tiene 365 dias")
