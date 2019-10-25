#Modifica	el	programa anterior	para	que	ahora	muestre	por	pantalla	el	máximo	y	mínimo	de	los	números.

suma=0 
cantidad=0 
mayor=0 #abro la variable para almacenar el mayor
lista=[] #creo una lista para almacenar todos los numeros que vaya a introducir en el while

while True: 
    n=input("Introduce un numero:") 
    if n=="fin": 
        print("ERROR")
        break
    n=int(n)
    suma+=n 
    cantidad+=1 
    media=suma/cantidad 
    print("La suma es: ",suma,", se han introducido",cantidad,"números y la media es",media)
    lista.append(n)

menor=lista[0] #abro la variable para almacenar el menor, que en la lista en este caso es el primero que introduzco
   
for i in lista: #para todos los valores de i en la lista
    if i>mayor: #si la i es mayor que el valor de mayor, que en el primero es 0 pero luego se actualiza
        mayor=i #almaceno i como mayor
    elif i<=menor: #si la i es menor o igual que el primero en la lista en un primer momento o si es menor que el almacenado
        menor=i #almaceno esa i como el menor
   
print("La suma final es: ",suma,", se han introducido ",cantidad,"números y la media es ",media,",el mayor número es",mayor,"y el menor es",menor)

