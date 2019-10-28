#Usando un bucle	while,	mostrar	en	pantalla	la	serie:	1,	50,	3,	48,	5,	46,	7,	44....................,	0.

listapar=list(range(0,51,2)) #cojo una lista con los valores pares
listaimpar=list(range(1,50,2)) #cojo una lista con el rango de valores impares
listapar.reverse() #doy la vuelta a la lista

i=0 #inicializo una variable con 0 para que entre en el bucle

while i in range (0,25): #mientras que el rango este entre 0 y la mitad de cada lista
    print (listaimpar[i],",",listapar[i],end=",",sep="" ) #imprimo el valor de la i de cada lista con separadores
    i+=1 #sumo uno a i para que vaya subiendo en el rango




   
    