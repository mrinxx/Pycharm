#Escribir	una	función	que	acepte	una	cadena	por	teclado	y	muestre	la	cuenta	de	los	caracteres diferentes.
#Ejemplo:
#Introduce texto: Programacion
#El texto tiene: 1 P, 2 r, 2 o, 1 g, 2 a, 1 m, 1 c, 1 i, 1 n


c=input("Introduce una palabra: ") #introduzco la palabra
c2=list(c) #lo creo en lista
cuenta=0 #cuenta cuantas palabras hay
 #cuento para contar la repeticion
vueltas=0 #abro para contar las vueltas
estan=[]


for i in c2: #para todas las letras que estan en la cadena introducida
    if i not in estan: #si no esta en la lista donde estan las letras
        print(i,c.count(i),",",sep=" ",end=" ") #muestro la i, cuento cuantas veces esta la i en la cadena de texto
        estan.append(i)#lo meto en estan, porque si es asi, no volvere a añadir la letra.

    