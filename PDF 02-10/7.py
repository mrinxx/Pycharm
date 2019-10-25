#Usando un bucle	while,	mostrar	en	pantalla	la	serie:	1,	50,	3,	48,	5,	46,	7,	44....................,	0.

listapar=list(range(0,51,2))
listaimpar=list(range(1,50,2))
listapar.reverse()
listafinal=[]
i=0
while i in range (0,25):
    print (listaimpar[i],",",listapar[i],end=" ",sep="" )
    i+=1




   
    