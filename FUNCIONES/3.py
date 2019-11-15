#Crear una función que calcule el área de un triángulo.

def longitud(radio): #defino la funcion
    pi=3.1416 #declaro la variable para el numero pi con su valor
    l=2*pi*radio #l es la formula de la longitud de la circunferencia
    return l #voy a devolver la formula fuera

if __name__ == "__main__": #en el bloque principal
    r=float(input("Introduce el radio de la circunferencia: ")) #pido el radio
    longitud=longitud(r) #llamo a la funcion usando r
    print("La longitud de la circunferencia con el radio introducido es:",longitud) #muestro el resultado