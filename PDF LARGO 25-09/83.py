#Dise˜na un programa que, dados cinco n´umeros enteros, determine cu´al de los cuatro ´ultimos n´umeros es m´as cercano
#al primero. (Por ejemplo, si el usuario introduce los n´umeros 2, 6, 4, 1 y 10, el programa responder´a que el n´umero m´as
#cercano al 2 es el 1.)

#pido los 5 numeros

n1=int(input("INTRUDUCE EL PRIMER NUMERO: "))
n2=int(input("INTRUDUCE EL SEGUNDO NUMERO: "))
n3=int(input("INTRUDUCE EL TERCER NUMERO: "))
n4=int(input("INTRUDUCE EL CUARTO NUMERO: "))
n5=int(input("INTRUDUCE EL QUINTO NUMERO: "))

lista=(n2,n3,n4,n5) #creo una lista con los numeros menos el primero

cerca=lista[1] #el mas cercano podria ser el siguiente de la lista
primero=n1 #el primero es el primero que he introduciso
for i in lista: #para cada i dentro de la lista a partir del segundo elemento
    diferenciacon1=abs(i-n1) #calculo la diferencia de i con el primero en valor absoluto por si es negativo
    diferenciaconmenor=abs(cerca-i) #calculo la diferencia del que esta más cercano con el numero que toca en valor absoluto por si es negativo
    if diferenciacon1<diferenciaconmenor: #si la diferencia con el primero es menor que la diferencia con el menor
        cerca=i #el mas cercano es ese numero
    else: #si no paso
        pass
print("El numero más cercano a",n1,"es:",cerca)




