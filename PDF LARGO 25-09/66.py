#Diseña un programa que, dados dos nuumeros enteros, muestre por pantalla uno de estos mensajes: ✭✭El segundo
#es el cuadrado exacto del primero.✮✮, ✭✭El segundo es menor que el cuadrado del primero.✮✮ o ✭✭El segundo es
#mayor que el cuadrado del primero.✮✮, dependiendo de la verificaci´on de la condici´on correspondiente al significado de
#cada mensaje.

num1=int(input("Introduce un número: ")) #pido un numero
num2=int(input("Introduce otro número: "))#pido otro numero

if num1**2 == num2: #si el primero elevado a 2 es igual que el segundo
    print("El segundo es el cuadrado exacto del primero")
elif num1**2 > num2: #si el primero elevado a 2 es mayor que el segundo
    print("El segundo es menor que el cuadrado del primero")
elif num1**2 < num2: #si el primero elevado a 2 es menor que el segundo
    print("El segundo es mayor que el cuadrado del primero")
else:
    pass
