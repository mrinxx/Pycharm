#Crear una función que calcule el área de un triángulo.

def area(): #defino la funcion para calcular el area
    a=(b*h)/2 #formula para calcular el area
    return a #voy a devolver la variable a

if __name__ == "__main__": #en el bloque principal del programa
    #pido dimensiones
    b=float(input("Introduce la base del triangulo: "))
    h=float(input("Introduce la altura del triáingulo: "))
    area=area() #llamo a la funcion
    print("El area del triángulo con las dimensiones introducidas es:",area)#muestro el resultado
