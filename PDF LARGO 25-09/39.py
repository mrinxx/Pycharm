#Haz un programa que pida al usuario una cantidad de euros, una tasa de inter´es y un n´umero de a˜nos. Muestra
#por pantalla en cu´anto se habr´a convertido el capital inicial transcurridos esos a˜nos si cada a˜no se aplica la tasa de inter´es
#introducida.
#Recuerda que un capital de C euros a un inter´es del x por cien durante n a˜nos se convierten en C · (1 + x/100)n euros.
#(Prueba tu programa sabiendo que una cantidad de 10 000 ¤ al 4.5% de inter´es anual se convierte en 24 117.14 ¤ al cabo
#de 20 a˜nos.)

euros=float(input("Introduce una cantidad de euros: ")) #pido cantidad
tasa=float(input("Introduce una tasa de interés: ")) #pido interes
tiempo=float(input("Introduce una cantidad de años: "))#pido años

total=euros*(1+tasa/100)**tiempo #calculo

print(euros,"euros, al",tasa,"de interés en",tiempo,"años es de:",total)#muestro