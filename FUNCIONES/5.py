#Crear una función que calcule la suma de la progresión	geométrica:	1+x+x2+x3+...+xn

def progresion(x): #creo la progresion
    lista=[] #abro una lista para almacenar los valores
    for i in range(0,x+1): #para todos los valores que esten entre 0 y el numero
        elevado=x**i #elevare el numero que introduzco a dicho valor
        lista.append(str(elevado)) #añado la variable elevado a la lista ya en forma de cadena
    total="+".join(lista) #hago un parsing de la lista
    return total #devolvere el total

if __name__ == "__main__": #en el bloque rincipal del programa
    t=int(input("Introduce el término para realizar la sucesión:")) #introduzco el numero
    total=progresion(t) #llamo a la funcion
    print("El resultado de la sucesion es: ",total) #muestro el resultado