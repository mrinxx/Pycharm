#Haz un programa que pida al usuario una cantidad de euros, una tasa de interes y un numero de anos. 
# Muestra por pantalla en cu´anto se habra convertido el capital inicial transcurridos esos anos 
# si cada a˜no se aplica la tasa de interes introducida.
#Recuerda que un capital de C euros a un inter´es del x por cien durante n a˜nos se convierten en 
# C · (1 + x/100)n euros.
#(Prueba tu programa sabiendo que una cantidad de 10 000 ¤ al 4.5% de inter´es anual se convierte en 24 117.14 ¤ al cabo
#de 20 anos.)

euros=float(input("Introduce una cantidad de euros: "))
tasa=float(input("Introduce la tasa de interes: "))
anhos=float(input("Introduce los años: "))

conversion= euros * (1 + (tasa / 100)) ** anhos

print("El total se convierte en: ",conversion)