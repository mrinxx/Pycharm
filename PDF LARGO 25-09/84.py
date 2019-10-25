#Dise˜na un programa que, dados cinco puntos en el plano, determine cu´al de los cuatro ´ultimos puntos es m´as cercano
#al primero. Un punto se representar´a con dos variables: una para la abcisa y otra para la ordenada. La distancia entre dos
#puntos (x1, y1) y (x2, y2) 

x1=int(input("INTRODUCE LA PRIMERA ABCISA: "))
y1=int(input("INTRODUCE LA PRIMERA ORDENADA: "))
x2=int(input("INTRODUCE LA SEGUNDA ABCISA: "))
y2=int(input("INTRODUCE LA SEGUNDA ORDENADA: "))
x3=int(input("INTRODUCE LA TERCERA ABCISA: "))
y3=int(input("INTRODUCE LA TERCERA ORDENADA: "))
x4=int(input("INTRODUCE LA CUARTA ABCISA: "))
y4=int(input("INTRODUCE LA CUARTA ORDENADA: "))
x5=int(input("INTRODUCE LA QUINTA ABCISA: "))
y5=int(input("INTRODUCE LA QUINTA ORDENADA: "))

d11=((x1-x2)**2+(y1-y2)**2)**0.5
d12=((x1-x2)**2+(y1-y2)**2)**0.5#calculo la distancia del primero con el segundo
d13=((x1-x3)**2+(y1-y3)**2)**0.5 #del primero con el tercero 
d14=((x1-x4)**2+(y1-y4)**2)**0.5 #del primero con el cuarto 
d15=((x1-x5)**2+(y1-y5)**2)**0.5 #del primero con el quinto

listadistancias=(d11,d12,d13,d14,d15) #creo una lista con las distancias que han salido

menor=0
menordist=0
for i in listadistancias:
    if i>menor:
        diferencia=i-d11
        menor=diferencia
        if diferencia
