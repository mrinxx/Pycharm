#Introducir	por	teclado	un	numero	y	mostrar	en	pantalla	la	serie:	1,	-2,	3,	-4,.........,	n o	–n

n=int(input("Escribe el número límite:"))
lista=[]

for i in range (1,n+1):
    if i%2 == 0:
        i=-i
    lista.append(i)
   
print(lista)