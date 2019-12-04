#Crear una función denominada elimina_duplicados	que	reciba una lista y la ordene eliminando	los	duplicados.
#Debe devolver una nueva	lista con los elementos	que	se	han	eliminado.

def elimina_duplicados(lista2): #define la funcion
    lista2.sort() #primero la ordena
    lista3=[] #lista para mostrar
    listae=[] #lista con los eliminados
    for i in lista2: #para cada elemento que este en la lista
        if i not in lista3: #si no esta en la lista que se va a mostrar
            lista3.append(i) #lo añade
        else: #si si que esta en la lista
            listae.append(i) #lo añade a la lista de los eliminados

    return lista3,listae #la funcion devolvera la lista y la de los eliminados

if __name__ == '__main__': #en el bloque principal
    lista=[1,2,9,3,4,5,6,6,8,5,5] #lista a ejecutar
    comprobacion=elimina_duplicados(lista) #llamo a la funcion
    print(comprobacion) #muestro el resultado