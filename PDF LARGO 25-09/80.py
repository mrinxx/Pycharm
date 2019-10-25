#Dise˜na un programa que calcule el m´aximo de 5 n´umeros enteros.  

#pido los 5 numeros
n1=int(input("INTRUDUCE EL PRIMER NUMERO: "))
n2=int(input("INTRUDUCE EL SEGUNDO NUMERO: "))
n3=int(input("INTRUDUCE EL TERCER NUMERO: "))
n4=int(input("INTRUDUCE EL CUARTO NUMERO: "))
n5=int(input("INTRUDUCE EL QUINTO NUMERO: "))

#creo una lista con los 5 numeros
lista=(n1,n2,n3,n4,n5)

max=0 #añado la variable maximo que comienza con 0

for i in lista: #para cada numero en la lista
    if i > max: #miro si ese numero es mayor que el almacenado en ese momento en max
        max=i #si es asi, max almacenara el valor de i correspondiente en ese momento
    else: #si no 
        pass #salgo de la condicion y vuelvo a irar otro numero

print("El mayor número es:",max)