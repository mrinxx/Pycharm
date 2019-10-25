#Escribe un programa que solicite dos números al usuario y le permita decidir si sumarlos, restarlos, multiplicarlos
#o dividirlos. El programa debe controlar todos los errores posibles.

#AQUI LO QUE HAGO ES COMPROBAR ERRORES, SI NO INTRODUZCO UN NUMERO SALTARA EL MENSAJE DEL EXCEPT
try:
    n1=float(input("Escribe el primer número:"))
    n2=float(input("Escribe el segundo número:"))
except:
    print("NO ES UN NUMERO!!!")
pass

operacion=(input("Introduce la Operación a realizar: "))
if type(operacion) == str:
    if operacion == "sumar" : #lo que hago con .lower es que va a pasar todo lo que haya en operaion a minuscula, por lo que no habra problemas en si es mayuscula o minuscula
        suma=n1+n2
        print("La suma de los dos números es:",suma)
    elif operacion == "restar":
        resta=n1-n2
        print("La resta de los dos números es:",resta)
    elif operacion == "multiplicar":
        multiplicacion=n1*n2
        print("La multiplicación de los dos números es:",multiplicacion)
    elif operacion == "dividir":
        if n2 == 0:
            print("NO SE PUEDE DIVIDIR ENTRE 0")
        else:
            division=n1/n2
            print("La divisioón de los dos números es:",division)
        pass
else:
    print ("No se ha introducido una operacion válida")
pass