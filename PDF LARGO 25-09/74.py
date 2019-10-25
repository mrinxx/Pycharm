#Ampl´ıa el programa del ejercicio anterior para que pueda identificar las letras e˜ne min´uscula y may´uscula

letra=input("Escribe un caracter: ") #pido

if letra >= 'a' and letra <= 'z':
	print ('Es una MINÚSCULA.')
elif letra >= 'A' and letra <= 'Z':
	print ('Es una MAYÚSCULA.')
elif letra == "Ñ": #si la letra es Ñ mayuscula
	print ('Es una eñe MAYÚSCULA.') 
elif letra == "ñ": #Si la letra es ñ minuscula
	print ('Es una eñe MINÚSCULA.')
else:
	print ('No es una letra.')