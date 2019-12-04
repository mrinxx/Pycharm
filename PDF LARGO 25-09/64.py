#Disena un programa que, dado un numero entero, muestre por pantalla el mensaje 
# ✭✭El n´umero es par.✮✮ cuando el numero sea par y el mensaje ✭✭El numero es impar.✮✮ cuando sea impar.

n=int(input("Introduce un numero: "))

if n%2 == 0:
    print("PAR")
else:
    print("IMPAR")