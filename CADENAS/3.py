#Diseñar	un	programa	que	partiendo	de	esta	lista:
#[“cerillas”, “patrulla”, “papel”, “azor”, “alerones”, “conversar”, “sollozo”, “manzana”]
#Permita	jugar	al	ahorcado	(no	es	necesario	imprimir	la	horca)	con	5	posibles	fallos. Es	necesario	imprimir	el	texto	
#que	quede	por	adivinar	usando	guiones	bajos.

import random #importo la biblioteca random para coger un elemento al azar de la lista dada

palabras=['cerillas', 'patrulla', 'papel', 'azor', 'alerones', 'conversar', 'sollozo', 'manzana'] #declaro la lista

palabravacia=[]
fallos=5 #maximo de fallos
contador=0
elegida = random.randint(0, len(palabras)-1 ) #elige una palabra al azar de la lista anterior
elegida=list(palabras[elegida]) #la palabra elegida al azar se convierte en lista
palabravacia=[]
solucion="".join(elegida)
print(elegida)
print(len(elegida))

#para la lista de la palabra elegida voy a añadir espacios a otra lista, uno por caracter que haya
for i in elegida: 
    espacio="_"
    palabravacia.append(espacio)

#Bucle para que vaya añadiendo las letras a medida que se van introduciendo y vean si esta o no
while fallos > 0: #mientras que el numero de fallos no sea 0
    print(" ".join(palabravacia),sep=" _ ") #muestro las letras que hay en la lista vacia
    letra=input("Introduce una letra: ") #voy introduciendo letras
    if letra in elegida: #si la letra que introduzco esta entre la palabra elegida
        if letra in palabravacia: #si la letra ya esta en la lista en la que vamos introduciendo las letras
            print("Letra ya introducida anteriormente") #muestra este mensaje
            fallos-=1 #lo toma como un fallo
            print("Quedan",fallos,"fallos") #muestra cuantos fallos quedan
        else: #si no esta
            print("CORRECTO") #muestra este mensaje
            for numeracion, valor in enumerate(elegida): #enumerate busca el valor (posicion) de cada elemento de la lista
                if valor == letra: #cuando el valor sea el mismo que la letra (ej: a == a)
                    palabravacia[numeracion]=letra #a la lista en la que están las letras, le añado la letra introducida donde me indique numeracion (ej: lugar 1)
    else: #si la letra no es correcta
        fallos-=1 #al total de fallos re resto uno
        print("Quedan",fallos,"fallos") #muestro cuantos quedan
    
    if fallos == 0: #si el total de fallos ha llegado a 0, es decir, ya no hay mas
        print ("HAS PERDIDO!!!! La palabra secreta era: ",solucion) #muestro el mensaje de que ha perdido
    elif "".join(palabravacia) == solucion: #si la cadena que hemos formado es igual a la palabra solucion
        print ("HAS DESCUBIERTO LA PALABRA SECRETA",solucion,"!!!") #muestro este mensaje
        break
    
