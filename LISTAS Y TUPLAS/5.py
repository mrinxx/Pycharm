#crear unanción denominada palindromos que reciba una lista de palabras y devuelva una nueva	lista con los
# elementos palíndromos (palabras capicúa, por ejemplo:rallar,eje,reconocer,rajar,salas).

def palindromos (lista): #defino la funcion
    palindromos = [] #guardará los palindromos
    for p in palabras: #para cada elemento en la lista
        p = list(p) #lo convierto a lista
        nueva = []#lista para dar la vuelta
        for l in :
            nueva.append(l) #para cada letra en la palabra la añado a la lista
        nueva.reverse() #le doy la vuelta
        if p == nueva: #si la palabra coincide con la palabra dada la vuelta
            p = "".join(p) #la convierto de nuevo a cadena
            palindromos.append(p) #la añado a la lista que guarde los palindromos

    return palindromos #devolvere los palindromos

if __name__ == '__main__': #en el bloque principal
    palabras = ["adios","mesa","rallar", "eje", "reconocer", "rajar", "salas", "hola"] #doy la lista de palabras
    comprobacion=palindromos(palabras) #llamo a la funcion
    print(comprobacion) #muestro el resultado






