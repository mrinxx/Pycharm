#Mejore el programa anterior haciendo que tenga en cuenta que no se puede dividir por cero
num1= int(input("Escriba un numero entero: "))
num2= int(input("Escriba un numero entero: "))

if num2==0: #pongo la condicion de que si el divisor es 0 no se puede hacer
    print("NO SE PUEDE DIVIDIR POR 0!!!!!!!!!")
elif num1%num2 == 0 : #pongo la division de la division
    print("La division es exacta")
else:
    print("La division no es exacta")
pass