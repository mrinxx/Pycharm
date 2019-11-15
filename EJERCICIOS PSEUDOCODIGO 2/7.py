#Dado un  mes del año y el día de la semana en que comienza, mostrar por pantalla una representación del
#calendario similar a la muestra:

m=input("Introduce un mes del año: ") #pido el mes
m31=['enero','marzo','mayo','julio','agosto','octubre','diciembre'] #meses con 31 dias
m30=['abril','junio','septiembre','noviembre'] #meses con 30 dias
try: #comprueba que sea correcto
    if str.lower(m) in m31: #si el mes esta entre los que tienen 31 dias
        dm=31 #los dias son 31
    elif str.lower(m) in m30: #si el mes esta entre los que tienen 30 dias
        dm=30 #los dias son 30
    elif str.lower(m)=="febrero": #si el mes es febrero
        dm=28 #los dias son 28
except ValueError:
    print("ERROR, MES INCORRECTO") #si no es correcto da este error
else: #si es correcto continuo
    dia=input("Introduzca el dia de la semana en el que cae el primer dia del mes: ") #pido el dia de la semana
    print(m, "\nL\tM\tX\tJ\tV\tS\tD") #muestro la cabecera
    if str.lower(dia) == 'lunes' or str.lower(dia) == "l": #si el dia introducido es lunes
        for i in range(1,dm+1): #desde el dia 1 hasta el total de dias del mes
            if i==7 or i==14 or i==21 or i==28: #si la i va de 7 en 7 dias
                print(i,end="\n")
            else:
                print(i,end="\t")
    elif str.lower(dia) == 'martes' or str.lower(dia) == "m": #si el primer dia es martes
        print("\t",end="") #muestro un espacio
        for i in range(1,dm+1): #desde el dia 1 hasta el dia de final del mes
            if i==7-1 or i==14-1 or i==21-1 or i==28-1: #si va de 7 en 7 dias, quitando el hueco
                print(i,end="\n")
            else:
                print(i,end="\t")
    elif str.lower(dia) == 'miercoles' or str.lower(dia) == "x": #si el primer dia es miercoles
        print("\t\t",end="")# muestro dos espacios
        for i in range(1,dm+1): #desde el dia 1 hasta el ultimo
            if i==7-2 or i==14-2 or i==21-2 or i==28-2: #si va de 7 en 7 dias, quitando los dos huecos
                print(i,end="\n")
            else:
                print(i,end="\t")
    elif str.lower(dia) == 'jueves' or str.lower(dia) == "j": #si el primer dia es jueves
        print("\t\t\t",end="") #3 huecos
        for i in range(1,dm+1):
            if i==7-3 or i==14-3 or i==21-3 or i==28-3: #si los dias van de 7 en 7 quitando los 3 huecos
                print(i,end="\n")
            else:
                print(i,end="\t")
    elif str.lower(dia) == 'viernes' or str.lower(dia) == "v": #si el primer dia es viernes
        print("\t\t\t\t",end="") #muestro 4 huecos
        for i in range(1,dm+1):
            if i==7-4 or i==14-4 or i==21-4 or i==28-4: #si va de 7 en 7 quitando los 4 huecos
                print(i,end="\n")
            else:
                print(i,end="\t")
    elif str.lower(dia) == 'sabado' or str.lower(dia) == "s": #si el dia de la semana es el sabado
        print("\t\t\t\t\t",end="") #muestro 5 espacios
        for i in range(1,dm+1):
            if i==7-5 or i==14-5 or i==21-5 or i==28-5: #de 7 en 7 quitando los 5 huecos
                print(i,end="\n")
            else:
                print(i,end="\t")
    elif str.lower(dia) == 'domingo' or str.lower(dia) == "d": #si el dia de la semana es domingo
        print("\t\t\t\t\t\t",end="") #muestro 6 huecos
        for i in range(1,dm+1):
            if i==7-6 or i==14-6 or i==21-6 or i==28-6: #si va de 7 en 7 dias quitando el numero de huecos
                print(i,end="\n")
            else:
                print(i,end="\t")
    else:
        print("DIA INTRODUCIDO NO VALIDO")


