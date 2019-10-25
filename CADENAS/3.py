#Diseñar	un	programa	que	partiendo	de	esta	lista:
#[“cerillas”, “patrulla”, “papel”, “azor”, “alerones”, “conversar”, “sollozo”, “manzana”]
#Permita	jugar	al	ahorcado	(no	es	necesario	imprimir	la	horca)	con	5	posibles	fallos. Es	necesario	imprimir	el	texto	
#que	quede	por	adivinar	usando	guiones	bajos.

import random #importo la biblioteca random para coger un elemento al azar de la lista dada

palabras=['cerillas', 'patrulla', 'papel', 'azor', 'alerones', 'conversar', 'sollozo', 'manzana'] #declaro la lista

palabravacia=[]
fallos=5 #maximo de fallos
print(len(palabras)) 
elegida = random.randint(0, len(palabras)-1 ) #elige una palabra al azar de la lista anterior
elegida=list(palabras[elegida]) #la palabra elegida al azar se convierte en lista
print(elegida)


#para la lista de la palabra elegida voy a añadir espacios a otra lista, uno por caracter que haya
for i in elegida: 
    espacio="_"
    palabravacia.append(espacio)

#Bucle para que vaya añadiendo las letras a medida que se van introduciendo y vean si esta o no
while fallos > 0: #mientras que el numero de fallos no sea 0
    letra=input("Introduce una letra: ") #voy introduciendo letras
    if letra in elegida: #si la letra que introduzco esta entre la palabra elegida
        cuenta=elegida.count(letra) #cuento cuantas veces aparece la letra en la palabra elegida al azar
        #DESDE AQUI NO SE!!!!
        if cuenta>1: #si la cuenta da mayor a uno
            for d in elegida:
                print(elegida.index(letra),letra)
            #for s in palabravacia: #para todos los valores que esten en la lista vacia
                #palabravacia[elegida.index(letra)]=letra #le introduzco la letra en el indice de las letras repetidas de la elegida al azar
        else:
           palabravacia[elegida.index(letra)]=letra 

    else:
        fallos-=1
        print("Quedan",fallos,"fallos")
    #if:    
    print("".join(palabravacia),sep=" ",end=" ")
