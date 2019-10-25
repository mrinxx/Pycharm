while True:
    try:
        edad=int(input("Introduce la edad:"))
        print("La edad es:",edad)
        break
    except:
        print("Ha introducido algo que no es un numero")


a=2 #SI NO SE DECLARA LA VARIABLE DA ERROR, SIEMPRE TIENE QUE ESTAR DEFINIDA Y SI TIENE UN VALOR QUE NO SE CORRESPONDE CON LA CONDICION DEL WHILE, DIRECTAMENTE NO ENTRARÁ 
while a<0 or a>1:
    a=float(input("Introduce un valor entre 0-1: "))
    print("El valor de a es",a)

#en este bucle si se introduce 0 o 1 el bucle para