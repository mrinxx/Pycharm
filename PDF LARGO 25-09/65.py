#Disena un programa que, dado un numero entero, determine si este es el doble de un numero impar. 
# (Ejemplo: 14 esel doble de 7, que es impar.)

n=int(input("Introduce un numero: "))

mitad=n//2

if mitad%2 != 0:
    print(n,"Es el doble de un numero impar")

