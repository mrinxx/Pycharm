#Dado	un	número	entero	positivo	hallar	los	números	perfectos	menores	que	él.	Un	número	es	perfecto	si	la	suma	
#de	sus	divisores,	excepto	él	mismo,	es	igual	al	propio	número.

n=int(input("Introduce un numero: "))#pido un numero

for i in range(0,n): #de todos los numeros positivos desde el 0 hasta el numero
    c=0 #para sumar los multiplos
    for m in range(1, (i//2)+1): #aqui se buscan los divisores, desde el 1 hasta su mitad
        if i%m==0:
            c+=m #suma el multiplo actual mas los anteriores

    if c==i: #si la suma de los numeros es igual al numero
        print( i,"es perfecto" )
    else: #si la suma no es igual
        print( i,"no es perfecto" )

        
