#Escriba un programa que pida un año y que escriba si es bisiesto o no.
#Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí.

anho=int(input("Escribe un año: "))

if anho >= 100 and anho % 100 ==0: #comparo el año introducido con 100 para ver si es un multiplo
    print(anho," NO es un año bisiesto") #si lo es digo que no es bisiesto
elif anho >= 400 and anho % 400 == 0: #comparo el año con 400 para ver si es multiplo
    print (anho, "SI es un año bisiesto") #si lo es digo que si es bisiesto
elif anho >= 4 and anho % 4 == 0: #comparo el año con 4 para ver si es multiplo
    print (anho, "SI es un año bisiesto") #si lo es digo que es bisiesto
else: #todo lo demas que no sea multiplo de 4 o 400 
    print(anho," NO es un año bisiesto") #no son bisiestos
pass