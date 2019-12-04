#Crear una  función denominada  en_orden_ascendente que reciba una  lista y devuelva True si se encuentra   
#ordenada en    orden ascendente o False si no  es  así.
#Crear otra función denominada  esta_ordenada que reciba también una lista y devuelva True si se encuentra  
#ordenada (ascendente o descendente) y False si no es así. Intenta hacerlo sin tener que recorrer la lista   
#dos veces.

def en_orden_ascendente (lista): #creo la primera funcion para el primer objetivo del programa
    ordenada=[] #inicializo una lista para almacenar los valores y a la vez ordenarla
    for n in lista: #para cada valor que reciba la funcion en la lista
        ordenada.append(n) #lo añade a la lista creada en la misma

    ordenada.sort() #ordena la lista nueva

    if lista == ordenada: #si la lista recibida es igual a la ordenada
        r="True"
    else: #si no
        r="False"

    return r #la funcion devolvera r

def ordenada_1(lista2): #definimos la funcion para el segundo objetivo
    ordenadaasc=[] #lista para ordenar ascendente
    ordenadade=[] #lista para ordenar descentdente
    for n2 in lista2: #para todos los valores de la lista recibida
        ordenadaasc.append(n2) #lo añado a una lista
        ordenadade.append(n2) #y a la otra
        
    ordenadaasc.sort() #ordeno la lista ascendente de forma ascendente
    ordenadade.sort(reverse=True) #ordeno la lista descendente de forma descendente
    
    if lista2==ordenadaasc or lista2==ordenadade: #si la lista recibida es igual a una de las 2
        m="True"
    else: # si no
        m="False"
        
    return m    #la funcion devolvera m

if __name__ == "__main__": # en el bloque principal
    comprobacion=ordenada_1([3,1,2])#llamo a la funcion con una lista
    print(comprobacion) #muestro el resultado
    pass