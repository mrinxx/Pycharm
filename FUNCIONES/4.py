#Crear una función que calcule la distancia entre dos puntos en el plano.
def distancia(a,b,c,d): #defino la funcion
    d=(((c-a)**2)+((d-b)**2))**0.5 #abro una variable con la funcion de la distancia entre puntos
    return d #fuera saldra la variable d

if __name__ == "__main__": #en el bloque principal
    #pido las coordenadas de los dos puntos
    x1=float(input("Introduce la primera coordenada de x: "))
    y1=float(input("Introduce la segunda coordenada de x: "))
    x2=float(input("Introduce la primera coordenada de y: "))
    y2=float(input("Introduce la segunda coordenada de y: "))
    distancia=distancia(x1,x2,y1,y2) #llamo a la funcion usando las variables introducidas
    print("La distancia entre los dos puntos es de:",distancia) #muestro el resultado
