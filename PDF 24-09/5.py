#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por
#pantalla el precio final del artículo.

siniva=float(input("Introduzca el precio base del artículo: "))
iva=int(input("Escribe el iva a aplicar: "))

if iva == 4: #si el iva introducido es 4
    iva4=siniva+(siniva*0.04) 
    print ("El precio final es de:",iva4,"euros")
elif iva == 10: #si el iva introducido es 10
    iva10=siniva+(siniva*0.1)
    print ("El precio final es de: ",iva10,"euros")
elif iva == 21: #si el iva introducido es 21
    iva21=siniva+(siniva*0.21)
    print("El precio final es de: ",iva21,"euros")
else: #si no es ninguna de las opciones anteriores
    print("EL IVA INTRODUCIDO NO ES VALIDO")
pass
