#Solicitar por teclado una cantidad de dinero con decimales hasta los céntimos y calcular el cambio en billetes y
#monedas de curso legal.

dinero=float(input("Introduce una cantidad de dinero: "))

#en una lista introducire todos los valores que pueden tomar los billetes y monedas
cantidades = [500,200,100,50,20,10,5,2,1,0.50,0.20,0.10,0.05,0.02,0.01]

print(dinero,"euros son: ") #esto es para que salga la cantidad total antes del desglose

for i in cantidades: #para todas las cantidades que estan en la lista anterior
    if dinero/i>=0: #dividiremos el total introducido entre el primer valor y si la division es mayor que 0
        total=dinero//i #el total de billetes que hay de esa cantidad se calcula
        dinero=dinero-(total*i) #el dinero restante a desglosar es el dinero que habia - el total de billetes/monedas de esa cantidad * la cantidad
        if total != 0: #si el total es un numero distinto de 0
            print(int(total),"billetes/monedas de",i) #mostraremos el resultado para ese numero
    
