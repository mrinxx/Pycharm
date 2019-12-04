#Disena un programa que calcule el maximo de 5 numeros enteros. 
# Si sigues una estrategia similar a la de la primera 
# solucion propuesta para el problema del maximo de 3 numeros, tendras problemas. Intenta resolverlo como en 
# el ultimo programa de ejemplo, es decir con un ✭✭candidato a valor maximo✮✮ que se va actualizando 
# al compararse con cada numero.

n1=int(input("Introduce un numero: "))
n2=int(input("Introduce otro numero: "))
n3=int(input("Introduce otro numero: "))
n4=int(input("Introduce otro numero: "))
n5=int(input("Introduce el ultimo numero numero: "))

numeros=[]

numeros.append(n1)
numeros.append(n2)
numeros.append(n3)
numeros.append(n4)
numeros.append(n5)

mayor=0 

for n in numeros:
    if n > mayor:
        mayor=n

print("El numero mayor es", mayor)
