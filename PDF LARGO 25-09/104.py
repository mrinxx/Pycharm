#Implementa un programa que muestre todos los multiplos de n entre n y m·n, ambos inclusive, donde 
#n y m son numeros introducidos por el usuario

n=int(input("Introduce un numero: "))
m=int(input("Introduce el otro: "))

for i in range(n,m*n+1):
    if i%n ==0:
        print(i)