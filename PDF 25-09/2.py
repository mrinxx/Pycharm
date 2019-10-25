#Reescribe el programa del ejercicio 2.1 usando try y except, de modo que el programa sea capaz de gestionar
#entradas no numéricas mostrando un mensaje y saliendo del programa. A continuación se muestran dos
#ejecuciones del programa:
#Horas de trabajo: 20
#Coste por hora: nueve
#Error, por favor introduzca un número
#Horas de trabajo: cuarenta
#Error, por favor introduzca un número

try: #lo que hace es si hay un error en estas lineas
    horas=float(input("Escribe el numero de horas: "))
    precio=float(input("Escribe el precio por horas: "))
except :#salte este error
    print("ha ocurrido un error, introduzca un numero!!!")
    pass

recargo=0 #abro recargo para dentro de la condicion meter un valor
if horas > 40:
    exceso=horas - 40 #calculo cuantas horas exceden de 40
    recargo=(1.5*exceso)*precio #calculo el recargo que es 1.5 mas que el precio, multiplicado por el exceso
    total1=(40*precio)+recargo #calculo el precio normal de 40 horas fijas+ el recargo que tengo
    print("El precio total del servicio es de:",total1,"euros")
elif horas <= 40: #si las horas no pasan de 40
    total2=horas*precio+recargo #calculo el precio normal, se introduce recargo, que en este caso al no pasar de 40h es 0
    print("El precio total del servicio es de:",total2,"euros")
