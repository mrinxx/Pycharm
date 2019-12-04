#Crear una	función	denominada	eliminar_extremos que reciba una lista	y elimine el primer	y el último	elemento
#de	la	misma.
#Usar la función para crear	un programa	que	calcule	la puntuación media	de la valoración de	8 jueces 
# eliminando los valores máximo	y mínimo.

def eliminar_extremos(n): #funcion para eliminar los extremos
    del n [0] #elimino el primer elemento
    del n [len(n)-1] #elimino el ultimo elemento
    return n #devuelvo la lista

def media(p): #funcion para calcular la media
    menor=p[0]
    mayor=0
    total=0 #inicializo la variable para almacenar la suma de todos los numeros
    numeros=0 #inicializo la variabl para contar el total de numeros
    for num in p:
        if num<menor:
            menor=num
        elif num>mayor:
            mayor=num 
    mac=p.count(mayor)
    mec=p.count(menor)
    while mac !=0:
        del p [p.index(mayor)]
        mac-=1
    while mec !=0:
        del p [p.index(menor)]
        mec-=1
    for m in p: #para todos los valores que estan en la lista
        total+=m #acumulo el total 
        numeros+=1 #acumulo el total de numeros
    media=total/numeros #calculo la media

    return media
    
if __name__ == "__main__":
    puntuaciones=[] #especifico la lista
    #añadire los elementos a la lista mientras que los voy pidiendo por pantalla
    p1=puntuaciones.append(int(input("Primera puntuacion: ")))
    p2=puntuaciones.append(int(input("Segunda puntuacion: ")))
    p3=puntuaciones.append(int(input("Tercera puntuacion: ")))
    p4=puntuaciones.append(int(input("Cuarta puntuacion: ")))
    p5=puntuaciones.append(int(input("Quinta puntuacion: ")))
    p6=puntuaciones.append(int(input("Sexta puntuacion: ")))
    p7=puntuaciones.append(int(input("Septima puntuacion: ")))
    p8=puntuaciones.append(int(input("Octava puntuacion: ")))
    media=media(puntuaciones) #llamo a la funcion con la lista creada
    print("La media de las puntuaciones es de: ",media) #muestro el resultado
    pass
