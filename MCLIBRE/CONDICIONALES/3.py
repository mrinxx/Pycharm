#Escriba un programa que pida dos números y que conteste cuál es el menor y cuál el mayor o que escriba que son iguales.

#PIDO AMBOS NUMEROS
num1= int(input("Escriba un numero entero: "))
num2= int(input("Escriba un numero entero: "))

if num1<num2: #comparo si numero 1 es menor que el num2
    print(num2," es mayor que ", num1) #si es menor muestro que num2 es mayor
elif num1>num2: #si lo anterior no se cumple, comparo si el numero 2 es menor que el num1
    print(num1," es mayor que ", num2) #si es menor muestro que num1 es mayor
else: #si ninguna de las dos condiciones anteriores se cumple 
    print(num1, " y ",num2," son iguales") #muestro que ambos numeros son iguales
pass