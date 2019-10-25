#Escribe un programa que solicite un número al usuario e indique si es par o impar.

numero=int(input("Escribe un numero: "))

if numero%2 == 0:
    print(numero,"es PAR")
else:
    print(numero,"es IMPAR")
