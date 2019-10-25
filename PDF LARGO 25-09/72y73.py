#Dise˜na un programa Python que lea un car´acter cualquiera desde el teclado, y muestre el mensaje ✭✭Es una MAY´USCULA✮✮
#cuando el car´acter sea una letra may´uscula y el mensaje ✭✭Es una MIN´USCULA✮✮ cuando sea una min´uscula. En cualquier otro
#caso, no mostrar´a mensaje alguno. (Considera ´unicamente letras del alfabeto ingl´es.) Pista: aunque parezca una obviedad,
#recuerda que una letra es min´uscula si est´a entre la ’a’ y la ’z’, y may´uscula si est´a entre la ’A’ y la ’Z’.

letra=input("Escribe un caracter: ") #pido

if letra >= 'a' and letra <= 'z': #si esta en el abecedario minusculo
	print ('Es una MINÚSCULA.')
elif letra >= 'A' and letra <= 'Z': #si esta en el abecedario mayusculo
	print ('Es una MAYÚSCULA.')
else: #parte del 73: si no es una letra
	print ('No es una letra.')