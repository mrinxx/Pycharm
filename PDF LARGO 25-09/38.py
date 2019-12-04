#El area A de un triangulo se puede calcular a partir del valor de dos de sus lados, a y b, y 
# del angulo θ que estos forman entre sı con la f´ormula A =1/2ab sin(θ). 
#Dise˜na un programa que pida al usuario el valor de los dos lados (en metros), el angulo que estos 
# forman (en grados), y muestre el valor del ´area.
#Ten en cuenta que la funci´on sin de Python trabaja en radianes, ası que el angulo que leas en grados 
#deberas pasarlo a radianes sabiendo que π radianes son 180 grados. Prueba que has hecho bien el programa 
#introduciendo los siguientes datos: a = 1, b = 2, θ = 30; el resultado es 0.5

import math  #importo la biblioteca

#pido los lados y el angulo
a=int(input("Introduce un lado: "))
b=int(input("Introduce el otro lado: "))
ang=int(input("Introduce el angulo que forman los grados entre si: "))

angg=(3.14*ang)/180 #convierto el angulo a grados
area=1/2*(a*b*math.sin(angg)) #calculo el area con la formula dada
print("El area del triangulo es",area) #muestro el resultado