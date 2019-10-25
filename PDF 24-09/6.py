#Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha
#pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).

importe=float(input("Introduzca el precio final del artículo: ")) #pido el precio final del articulo

siniva=importe-(importe*0.1)

print ("El importe sin iva es de:",siniva,"euros y se ha aplicado un iva del 10%")