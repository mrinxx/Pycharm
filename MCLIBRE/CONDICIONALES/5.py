#Mejore el programa anterior haciendo que cuando la diferencia sea exactamente un año, escriba la frase en singular:
actual=int(input("Introduce el año actual: "))
cualquiera=int(input("Introduce un año cualquiera: "))

if cualquiera-actual == 1:
    print("Falta un año para el ", cualquiera)
elif actual-cualquiera == 1:
    print("Ha pasado un año desde el ", cualquiera)
elif actual<cualquiera:
    print("Faltan ",cualquiera-actual,"años para el año ",cualquiera)
else:
    print("Han pasado ",actual-cualquiera," años desde el ",cualquiera)
pass