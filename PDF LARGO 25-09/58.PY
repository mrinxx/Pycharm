#Diseña un programa que lea un numero flotante por teclado y muestre por pantalla el mensaje 
#                               El numero es negativo 
# solo si el numero es menor que cero.

numero=float(input("Escribe un numero: "))

if numero < 0:
    print("El numero es negativo")
else:
    print ("El numero no es menor que 0")
pass