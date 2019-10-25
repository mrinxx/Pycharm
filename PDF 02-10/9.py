#Determinar	si	dos	números	enteros	positivos	son	amigos,	es	decir,	si	la	suma	de	los	divisores	del	1º	excepto	el	
#mismo	es igual	al	2º,	y	viceversa.

n1=int(input("Escribe un numero: ")) #pido un numero
n2=int(input("Escribe otro numero: ")) #pido otro numero

suman1=0 #suma de todos los divisores de n1
suman2=0 #suma de todos los divisores de n2

for i in range(1,n1): #para todos los numeros en el rango desde 1 al n1
    if n1%i==0: #si divido n1 entre el numero que toque en ese momento y da 0 el resto
        suman1+=i #a suman1 le añado el valor de i para que este incremente (deberia llegar a n2)

for m in range(1,n2): #para todos los numeros en el rango desde 1 al n2
    if n2%m==0: #si divido n2 entre el numero que toque en ese momento y da 0 el resto
        suman2+=m #a suman2 le añado el valor de i para que este incremente (deberia llegar a n1)

if suman1==n2 and suman2==n1: #si suman1 es igual a n2 y si suman2 es igual a n1
    print ('SON AMIGOS')
else: #si no
    print ('NO SON AMIGOS')
