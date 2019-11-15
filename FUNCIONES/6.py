#Crear una función que devuelva	si un año es bisiesto.

def bisiesto(x): #defino la funcion
    if x%400 ==0 or ( x%4==0 and  x%100!=0): #comprobamos si el año es bisiesto
        s="si es un año bisiesto" #s sera afirmativo si lo es
    else: #si no
        s="no es un año bisiesto" #sera negativo
    return s #devolvera s

if __name__ == "__main__": #en el bloque principal del programa
     #se comprobara si a es un entero
    try: #en caso de que lo sea
        a=int(input("Introduce un año para comprobar si es bisiesto: ")) #introduzco el numero
        solucion=bisiesto(a) #llamo a la funcion
        print(a,solucion) #muestro la solucion
        pass
    except: #si no lo es 
        print("No has introducido un número!!!") #muestro que no lo es

