#Dados	dos	números	enteros	 (un	dividendo	y	un	divisor	distinto	de	0)	obtener	su	cociente	y	el	 resto	mediante	
#restas	sucesivas


dividendo=int(input("Introduce el primer numero: ")) #pido dividendo
divisor=int(input("Introduce el segundo numero: ")) #pido divisor

cociente=0 #el cociente realmente es un contador de las vueltas que da y lo inicio a 0 aqui

for i in range (0,divisor+1): #para todos los valores de i que se encuentren entre 0 y el divisor
    if dividendo>=divisor: #si el dividendo es mayor o igual que el divisor
        cociente+=1 #doy una vuelta más y lo pongo como el cociente
        dividendo-=divisor #se vuelve a calcular el dividendo para ver si queda algo y volver a entrar en el bucle o no
    else: #si no lo es, salgo
        break
         
    
print ("El cociente es: ",cociente,"y el resto", dividendo)
       
        