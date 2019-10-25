#Solicitar un número en decimal por teclado y convertirlo a binario. Si no se conoce la forma de hacerlo, localizar
#el algoritmo en internet.

n=int(input("Introduce el número decimal: ")) #pido el numero


dividendo=n #el dividendo de nuestras divisiones será el número que se ha introducido
resto=0 #inicializamos la variable resto
restos=[] #abrimos la lista que almacenara los restos

while dividendo >=2: #mientras que el dividendo sea SIEMPRE mayor o igual a dos entrará en un bucle
    resto=dividendo%2  #se calculara el resto correspondiente entre el numero que toque con su modulo a 2
    restos.append(str(resto)) #se introducira ese resto a la lista en forma de cadena
    dividendo=dividendo//2 #el cociente se convierte en el dividendo
    if dividendo<=2: #en caso de que el dividendo llegue a ser menor o igual a 2
        resto=dividendo%2 #se calculará de nuevo el resto
        restos.append(str(resto)) #se añadirá de la misma manera que arriba
        dividendo=dividendo//2 #se calculará la division entera del dividendo que tenemos en ese momento y 2
        restos.append(str(dividendo))#se añadirá ese ultimo dividendo a la lista de los restos

restos.reverse() #como el binario se lee de abajo a arriba, damos la vuelta a la lista
restos="".join(restos) #lo convierto a cadena de texto(lo junto)
print ("La equivalencia de ",n,"en binario es",restos) #lo muestro







