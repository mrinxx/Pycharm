#Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no.
num1= int(input("Escriba un numero entero: "))
num2= int(input("Escriba un numero entero: "))

if num1%num2 == 0 :
    print("La division es exacta")
else:
    print("La division no es exacta")
pass