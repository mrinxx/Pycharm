#Disena un programa que, dados cinco puntos en el plano, determine cual de los cuatro ultimos puntos es mas 
# cercano al primero. Un punto se representara con dos variables: una para la abcisa y otra para la ordenada. 
# La distancia entre dos puntos (x1, y1) y (x2, y2) es ((x1 − x2)2 + (y1 − y2)2)**2

import math

x1=int(input("Introduce la x del primer punto: "))
y1=int(input("Introduce la y del primer punto: "))
x2=int(input("Introduce la x del segundo punto: "))
y2=int(input("Introduce la y del segundo punto: "))
x3=int(input("Introduce la x del tercer punto: "))
y3=int(input("Introduce la y del tercer punto: "))
x4=int(input("Introduce la x del cuarto punto: "))
y4=int(input("Introduce la y del cuarto punto: "))
x5=int(input("Introduce la x del quinto punto: "))
y5=int(input("Introduce la y del quinto punto: "))

d1=math.sqrt((x1-x2)**2+(y1-y2)**2)
d2=math.sqrt((x1-x3)**2+(y1-y3)**2)
d3=math.sqrt((x1-x4)**2+(y1-y4)**2)
d4=math.sqrt((x1-x5)**2+(y1-y5)**2)


if d1<d2 and d1<d3 and d1<d4:
    print("El segundo punto es el más cercano")
elif d2<d1 and d2<d3 and d2<d4:
    print("El tercer punto es el más cercano")
elif d3<d1 and d1<d2 and d1<d4:
    print("El cuarto punto es el más cercano")
if d4<d1 and d1<d2 and d1<d3:
    print("El quinto punto es el más cercano")
