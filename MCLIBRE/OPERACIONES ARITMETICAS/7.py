#Escriba un programa que pida una cantidad de segundos y que escriba cuántas horas, minutos y segundos son.
#LA SOLUCION DE ESTO NO ME DA
segundos=float(input("Escribe una cantidad de segundos "))

if segundos%60*60 != 0: #si el numero no es una cantidad exacta de horas
    hora=int(segundos/3600)  #paso la cantidad a horas
    resto=segundos%3600 #guardo en una variable el resto que queda de segundos a horas
    minut=int(resto/60)#el resto lo paso a minutos
    if segundos%60 != 0: #si el numero no es una cantidad exacta de minutos
        minu=int(segundos/60)  #paso la cantidad a minutos
        resto2=segundos%60 #guardo en una variable el resto que queda de segundos a minutos
        seg=int(resto2/60*60) #el resto lo paso a segundos   
        print(segundos," segundos son ",hora," horas",minut," minutos y ", seg,"segundos")
    pass
else:
    solohora=int(segundos/60**2)
    print(segundos," segundos son ",solohora," horas ")
pass
