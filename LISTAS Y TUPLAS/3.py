#Crear una función denominada hay_duplicados que reciba	 una lista y devuelva True si contiene duplicados  o
#False	si	no	es	así.
#Usar la función para generar una lista de 20 números aleatorios del 1 al 100 que no contenga duplicados.

def hay_duplicados(lista): #funcion para decir simplemente si tiene duplicados o no
    for n in lista: #para cada valor en lo que reciba
        cuenta=lista.count(n) #contare cuantas veces aparece
        if cuenta>1: #si aparece mas de una vez
            r="True"
        else: #si no
            r="False"
    return r #esta funcion devuelve esto

def hay_duplicados_lista(lista2): #funcion que genere aleatorios unicos
    import random #importo la biblioteca necesaria
    total=0 #inicializo una variable para acumular vueltas más adelante
    lista2=[] #inicializo una lista para comparar los valores que se vayan generando
    while total <=20: #mientras que el total de vueltas que da es menor o ifual a 20
        n=random.randint(1,100) #creo numeros aleatorios entre 1 y 100
        if n not in lista2: #si el numero no esta en la lista que compara los valores
            lista2.append(n) #lo añado
        else: #si no
            continue #no lo añado, si no que continuo
        total+=1 #aumento 1 vuelta

    return lista2 #la funcion devolvera esto

if __name__ == '__main__': #en el bloque principal
    lista=[] #creo una lista que vaya a contener los valores generados
    generar_lista=hay_duplicados_lista(lista) #llamo a la funcion
    print(generar_lista) #muestro el resultado

