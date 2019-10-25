#Diseñar	un	programa	que	a	partir	de	una	fecha	introducida	por	teclado	con	el	formato	día, mes, año,
#se	obtenga	la	fecha	del	día	siguiente.

f=input("Introduce dia, mes y año: ") #cojo la fecha
f=str.split(f,"-") #la convierto a cadena y paso el separador

d=int(f[0]) #el dia
m=int(f[1]) #el mes
a=int(f[2]) #el año

if d>=1 and d<=31: #si el dia esta en el rango de dias de un mes
    if m>=1 and m<=12: #si es asi, compara si el mes esta dentro del rango de meses de un año
        if m == 1 or m==3 or m == 5 or m == 7 or m == 8 or m == 10: # si el mes esta entre los que tienen 31 dias
            if d == 31: #si el dia es el 31
                m+=1 #subo un mes
                d=1 #el dia es 1
        elif  m == 4 or m==6 or m == 9 or m == 11: # si el mes esta entre los que tienen 30 dias
            if d == 30: #y el dia es 30
                m+=1 #subo 1 mes
                d=1 #el dia es 1
        elif d == 31 and m == 12: #si el mes es diciembre y es el 31
                a+=1 #subo un año
                m=1 #el mes es 1
                d=1 #el dia es 1

        if a >= 400 and a % 400 == 0: #si el año es bisiesto 
            if m == 2 and d == 28: #si es asi, mira si el mes es febrero y si el dia es el 28
                d = 29   #si es asi dice que el dia es 29
            else: # si no 
                d=1 #el dia es 1
                m+=1 #el mes se pone en 3
        elif a >= 4 and a % 4 == 0: #hace lo mismo que arriba
            if m == 2 and d == 28:
                d = 29
            else: #si no hace lo mismo que arriba
                d=1
                m+=1
        else:
            d+=1
print(d,m,a,sep="-")


# from datetime import datetime, datedelta
# fecha= input("Ingrese fecha ==> "d/m/a": ")
# fecha = datetime.strptime(fecha, '%d/%m/%Y')
# print(fecha + timedelta(days=1))

    









