##Diseña un programa que lea un numero flotante por teclado y muestre por pantalla el mensaje 
#                               El numero es positivo
# solo si el numero es mayor o igual que cero.

numero=float(input("Escribe un numero: "))

if numero >= 0:
    print("El numero es positivo")
else:
    print ("El numero es menor que 0")
pass