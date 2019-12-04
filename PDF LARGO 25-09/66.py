#Disena un programa que, dados dos numeros enteros, muestre por pantalla uno de estos mensajes: ✭✭El segundo
#es el cuadrado exacto del primero.✮✮, ✭✭El segundo es menor que el cuadrado del primero.✮✮ o ✭✭El segundo es
#mayor que el cuadrado del primero.✮✮, dependiendo de la verificacion de la condicion correspondiente 
#al significado decada mensaje.

n1=int(input("Introduce un numero: "))
n2=int(input("Introduce un numero: "))

if n1**2 == n2:
    print("El segundo es el cuadrado exacto del primero ")
elif n1**2 > n2:
    print("El segundo es menor que el cuadrado del primero")
elif n1**2<n2:
    print("El segundo es mayor que el cuadrado del primero")