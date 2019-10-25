#Realiza un programa que calcule el desglose en billetes y monedas de una cantidad exacta de euros. Hay billetes de
#500, 200, 100, 50, 20, 10 y 5 ¤ y monedas de 2 y 1 ¤.
##Realiza un programa que calcule el desglose en billetes y monedas de una cantidad exacta de euros. Hay billetes de
#500, 200, 100, 50, 20, 10 y 5 ¤ y monedas de 2 y 1 ¤.(¿Que c´omo se efect´ua el desglose? Muy f´acil. Empieza por calcular la divisi´on entera entre la cantidad y 500 (el valor
#de la mayor moneda): 434 entre 500 da 0, as´ı que no hay billetes de 500 ¤ en el desglose; divide a continuaci´on la cantidad
#434 entre 200, cabe a 2 y sobran 34, as´ı que en el desglose hay 2 billetes de 200 ¤; dividimos a continuaci´on 34 entre 100
#y vemos que no hay ning´un billete de 100 ¤ en el desglose (cabe a 0); como el resto de la ´ultima divisi´on es 34, pasamos a
#dividir 34 entre 20 y vemos que el desglose incluye un billete de 20 ¤ y a´un nos faltan 14 ¤ por desglosar. . . )

cantidad=int(input("Introduzca la cantidad a desglosar: ")) #introduzco la cantidad

if cantidad%500 != 0 or cantidad%500 == 0:
    billetes500=cantidad//500
    resto500=cantidad%500
