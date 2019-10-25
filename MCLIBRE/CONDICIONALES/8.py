#Escriba un programa que pida tres números y que escriba si son los tres iguales, si hay dos iguales 
#o si son los tres distintos.

num1=int(input("Escribe un numero: "))
num2=int(input("Escribe un numero: "))
num3=int(input("Escribe un numero: "))

if num1==num2 and num1==num3:
    print("Los tres son iguales")
elif num1==num2 or num2==num3 or num1==num3:
    print("solo hay dos iguales")
else:
    print("los tres son distintos")
pass