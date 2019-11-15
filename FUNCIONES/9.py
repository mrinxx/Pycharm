#Crear una función que	devuelva el	número de dígitos necesarios para expresar un número en	binario.

def bits(dividendo):
    import math #importo la biblioteca math
    bits=math.log(dividendo, 2) +1 #uso la funcion de logaritmo para saber a que numero debe estar elevado 2 para representar el numero introducido, que realmente es el numero de digitos
    return int(bits) #se mostrará el numero de digitos como estero ya que si no da decimales

if __name__ == "__main__": #en el bloque ppal
    n=int(input("Introduce un número: ")) #introduzco el numero
    digitos=bits(n) #llamo a la funcion
    print("Los digitos necesarios para representar el número",n,"son",digitos) #muestro
    pass