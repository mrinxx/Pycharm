#Diseña un programa que, dado un numero entero, muestre por pantalla el mensaje ✭✭El numero es par.✮✮ cuando el
#numero sea par y el mensaje ✭✭El numero es impar.✮✮ cuando sea impar.

numero=int(input("Introduce un número: "))

if numero%2 == 0:
    print("ES PAR")
else:
    print("ES IMPAR")
pass

