#Disena un programa Python que lea un caracter cualquiera desde el teclado, y muestre el mensaje 
# ✭✭Es una MAY´USCULA✮✮ cuando el caracter sea una letra mayuscula y el mensaje 
# ✭✭Es una MIN´USCULA✮✮ cuando sea una minuscula. En cualquier otro caso, no mostrara mensaje alguno. 
# (Considera ´unicamente letras del alfabeto ingl´es.) Pista: aunque parezca una obviedad, recuerda que una 
# letra es min´uscula si est´a entre la ’a’ y la ’z’, y may´uscula si est´a entre la ’A’ y la ’Z’.

#EJERCICIO 73: Amplıa la solucion al ejercicio anterior para que cuando el caracter introducido no sea una letra
# muestre el mensaje ✭✭No es una letra✮✮. 

#EJERCCIO 74: Amplıa el programa del ejercicio anterior para que pueda identificar las letras eÑe minuscula y mayuscula
caracter=input("Introduce un caracter: ")

if caracter >= "a" and caracter <="z" or caracter == "ñ": 
    print("MINUSCULA")
elif caracter >= "A" and caracter <="Z" or caracter == "Ñ": 
    print("MAYUSCULA")
else:
    print("NO ES UNA LETRA")
    pass