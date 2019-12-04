#Disena un programa que lea un caracter de teclado y muestre por pantalla el mensaje 
# ✭✭Es parentesis✮✮ solo si el caracter leıdo es un parentesis abierto o cerrado.

caracter=input("Introduce un caracter: ")

if caracter =="(" or caracter==")":
    print("ES UN PARENTESIS ")
else:
    print("No es un paréntesis")