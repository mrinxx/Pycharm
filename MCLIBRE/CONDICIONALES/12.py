#Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo.
#Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir
#entonces la base y la altura y escribir el área. 
#Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces
#el radio y escribir el área.
#Se recuerda que el área de un triángulo es base por altura dividido por 2 
# y que el área de un círculo es Pi (aproximadamente 3,141592) por el radio al cuadrado.

accion=input("¿Desea calcular el area de un triángulo o un circulo? Introduzca C/c o T/t: ")

if accion == "T" or accion == "t": #si lo que se escribe es t o T
    baset=float(input("Escriba la base del triángulo: "))  #Pide la base
    alturat=float(input("Escriba la altura del triángulo: "))  #pide la altura
    areat=(baset*alturat)/2 #calcula el area
    print("El área del triángulo es de: ",areat)
elif accion == "C" or accion == "c": #si se escribe C o c
    radioc=float(input("Escriba el radio del círculo: ")) #Pide el radio 
    pi=3.141592 #almaceno la cte pi
    areac=pi*(radioc**2) #calculo area
    print("El área del círculo es de: ",areac)
else: #todo lo demas que se escriba no es valido, por lo que salgo
    print("OPCION NO VÁLIDA")
pass