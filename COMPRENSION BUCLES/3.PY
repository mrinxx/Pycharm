#Adivinar el resultado del programa introduciendo: 2000, 2010, 2012 y 2100. ¿Qué hace el programa?
try:
    a=int(input("numero: "))
    if not a%400 or (not a%4 and a%100):
        print("si")
    else:
        print("no")
except:
    print("no es un numero")


#2000: MOSTRARÁ SÍ YA QUE ES DIVISIBLE ENTRE 400
#2010: MOSTRARÁ NO YA QUE NO CUMPLE NINGUNA DE LAS CONDICIONES (NO ES DIVISIBLE ENTRE 400, NI ENTRE 100 PERO TAMPOCO ENTRE 4)
#2012:MOSTRARA SI YA QUE ES DIVISIBLE ENTRE 400
#2100:MOSTRARA SI YA QUE ES DIVISIBLE ENTRE 400 Y ADEMAS, ES DIVISIBLE ENTRE Q00 PERO NO ENTRE 4

#El programa muestra si los numeros que se introducen son divisibles entre 400 O si son divisibles entre 100 pero no entre 4
#podría ser una comprobación de si un año itroducido es bisiesto o no