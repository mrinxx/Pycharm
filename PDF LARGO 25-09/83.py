#Dise˜na un programa que, dados cinco n´umeros enteros, determine cu´al de los cuatro ultimos numeros es mas 
# cercano al primero. (Por ejemplo, si el usuario introduce los numeros 2, 6, 4, 1 y 10, el programa 
# respondera que el numero mas cercano al 2 es el 1.)

n1=int(input("Introduce un numero: "))
n2=int(input("Introduce otro numero: "))
n3=int(input("Introduce otro numero: "))
n4=int(input("Introduce otro numero: "))
n5=int(input("Introduce el ultimo numero numero: "))

p1=n2-n1
p2=n3-n1
p3=n4-n1
p4=n5-n1

if p1>p2 and p1>p3 and p1>p4:
    print (n1," es el numero más próximo")
elif p2>p1 and p2>p3 and p2>p4:
    print (n2," es el numero más próximo")
elif p3>p1 and p3>p2 and p3>p4:
    print (n3," es el numero más próximo")
elif p4>p1 and p4>p2 and p4>p3:
    print (n4," es el numero más próximo")