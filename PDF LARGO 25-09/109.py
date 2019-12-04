#Queremos hacer un programa que calcule el factorial de un numero entero positivo. 
# El factorial de n se denota con n!, pero no existe ningun operador Python que permita efectuar 
# este calculo directamente. Sabiendo que n! = 1 · 2 · 3 · . . . · (n − 1) · n
#y que 0! = 1, haz un programa que pida el valor de n y muestre por pantalla el resultado de calcular n!

n=int(input("Introduce n: "))
fac=1
for i in range (1,n+1):
    fac=fac*i

print(fac)