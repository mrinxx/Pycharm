#Dado un  mes del año y el día de la semana en que comienza, mostrar por pantalla una representación del
#calendario similar a la muestra:

import calendar

m=input("Introduce un mes del año: ") #pido el mes
dia=input("¿En que día de la semana comenzó?: ") #pido el dia



if m.lower() == "enero" :
    m=1
elif m.lower()=="febrero":
    m=2
elif m.lower()=="marzo":
    m=3
elif m.lower()=="abril":
    m=4
elif m.lower()=="mayo":
    m=5
elif m.lower()=="junio":
    m=5
elif m.lower()=="julio":
    m=7
elif m.lower()=="agosto":
    m=8
elif m.lower()=="septiembre":
    m=9
elif m.lower()=="octubre":
    m=10
elif m.lower()=="noviembre":
    m=11
elif m.lower()=="diciembre":
    m=12
else:
    print("MES INTRODUCIDO NO VÁLIDO")

m=int(m)

if dia.lower()=="lunes":
    dia=1
elif dia.lower()=="martes":
    dia=2
elif dia.lower()=="miercoles":
    dia=3
elif dia.lower()
c= calendar.TextCalendar()
c=c.formatmonth(m)

print(c)
