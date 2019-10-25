#Introducido	por	teclado	un	número	entero	mayor	que	2,	visualizarlo	de	todas	las	formas	posibles	como	producto	
#de	dos	factores	(no	es	válido	el	número	1	como	factor).
#Por	ejemplo:	Dado	el	número	36,	habría	que	visualizar:	18	*	2,	12	*	3,	9	*	4,	6	*	6,	3 *	12,	4	*	9,	2	*	18

numero = int(input("Ingresa un numero: ")) #ingresa un numero
lista1=[]
lista2=[]

for i in range(2, numero//2+1): #para todos los numeros que esten entre 2 , ya que el uno no va a contar y la mitad del numero introducido
            if numero % i == 0:
                por=numero//i
                str(i)
                str(por)
                lista1.append(i)
                lista2.append(por)
                print(por,"*",i,",",end="")


                







