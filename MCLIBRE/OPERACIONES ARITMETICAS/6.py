#Escriba un programa que pida una cantidad de segundos y que escriba cuántos minutos y segundos son.

segundos=float(input("Escribe una cantidad de segundos "))

if segundos%60 != 0: #si el numero no es una cantidad exacta de minutos
    minu=int(segundos/60)  #paso la cantidad a minutos
    resto=segundos%60 #guardo en una variable el resto que queda de segundos a minutos
    seg=int(resto/60*60) #el resto lo paso a segundos   
    print(segundos," segundos son ",minu," minutos y ", seg,"segundos")
else:
    solominu=segundos/60 #si el numero si que da de resto 0 divido los segundos entre 60
    print(segundos," segundos son ",solominu," minutos ") #muestro los minutos que son 
pass
