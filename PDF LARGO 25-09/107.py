#Disena un programa que calcule (un sumatorio con m arriba, donde i =n es el primer valor) 
# donde n y m son numeros enteros que debera introducir el usuario por teclado
#PARTE 2:
#Modifica el programa anterior para que si n > m, el programa no efectue ningun calculo y muestre 
#Por pantalla unmensaje que diga que n debe ser menor o igual que m

m=int(input("Introduce el último valor que tomará i: "))
n=int(input("Introduce n, el primer valor que tomará i: "))
total=0
if n>m:
    print ("n debe ser menor o igual que m")
    exit
else:
    for i in range(n,m+1):
        total+=i
    print(total)


