#Escribe el programa anterior usando solamente dos variables.

lista=[] #creo una lista a la que voy a añadir los numeros

lista.append(float(input("Inserte el primer numero: "))) #añado a la lista el primero
lista.append(float(input("Inserte el segundo numero: "))) #añado el segundo
lista.append(float(input("Inserte el tercer numero: "))) #añado el tercero

mayor=max(lista) #con la funcion max saco el numero mas grande que haya en la lista

print("El mayor número es:",mayor)