#Introducir una fecha por teclado y el día de la semana del 1 de enero de ese año y calcular el día de la semana
#correspondiente a la fecha introducida.

f=input("Introduce la fecha: ") #introduzco la fecha
f2=input("Introduce el día de la semana del 1 de enero de ese año:")
f=str.split(f,"-") #la formateo
f=list(f) #la convierto a lista

dia=int(f[0]) #el dia es el primer elemento de la lista
mes=int(f[1]) #el mes el segundo

meses31=[1,3,5,7,8,10,12] #meses con 31 dias
meses30=[4,6,9,11] #meses con 30 dias
febrero=[2] #mes con 28 dias
dias=0 #variable para acumular los dias entre el dia actual y el 1 de enero 

for i in range (1,mes): #para todos los meses entre enero y el mes correspondiente
    if i in meses31: #si estra en los meses con 31 dias
        dias+=31 #sumo 31 al total
    elif i in meses30: #si entra en los meses con 30 dias
        dias+=30 #sumo 30 al total
    elif i in febrero: #si el mes esta en febrero
        dias+=28 #sumo 29
    
dias+=dia #al total de dias le sumo lo que llevo transcurrido de mes

modulo=dias%7 #hago el modulo para ver cuantos dias le tengo que sumar al dia en el que cae el 1 de enero

#aqui convierto el dia que escribo del 1 de enero a su dato numerico
if f2 == "lunes": 
    f2=1
elif f2 == "martes":
    f2=2
elif f2 == "miércoles":
    f2=3
elif f2 == "jueves":
    f2=4
elif f2 == "viernes":
    f2=5
elif f2 == "sábado":
    f2=6
elif f2 == "domingo":
    f2=7

diasemana=f2+modulo-1 #para saber el dia en el que cae sumo el dia en el que cae el 1 de enero+el modulo que he 
                        #sacado antes y le resto uno porque realmente el dia no ha pasado 

#aqui voy a convertir el resultado que me de en un dia de la semana
if diasemana == 1 :
    diasm="lunes"
elif diasemana == 2:
    diasm="martes"
elif diasemana == 3 :
    diasm="miércoles"
elif diasemana == 4 :
    diasm="jueves"
elif diasemana == 5:
    diasm="viernes"
elif diasemana == 6 :
    diasm="sábado"
elif diasemana == 7:
    diasm="domingo"

f="-".join(f) #vuelvo a convertir la fecha que he introducido anteriormente en una cadena
print("El dia",f,"cae en",diasm)
