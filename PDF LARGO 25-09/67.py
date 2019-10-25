#Un capital de C euros a un inter´es del x por cien anual durante n a˜nos se convierte en C ·(1 + x/100)n euros. 
# Dise˜na un programa Python que solicite la cantidad C y el inter´es x y calcule el capital final s´olo si x es una cantidad positiva.

euros=float(input("Introduce una cantidad de euros: ")) #pido cantidad
tasa=float(input("Introduce una tasa de interés: ")) #pido interes
tiempo=float(input("Introduce una cantidad de años: "))#pido años

if tasa >= 0: #si la tasa de interes es POSITIVA
    total=euros*(1+tasa/100)**tiempo #calculo el total
    print(euros,"euros, al",tasa,"de interés en",tiempo,"años es de:",total)#muestro
else: #si la tasa de interes MO es POSITIVA
    print("LA TASA DE INTERES ES NEGATIVA, INTRODUZCA OTRO VALOR")
    pass