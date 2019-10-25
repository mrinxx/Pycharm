#Introducir una serie de números enteros por teclado. La serie termina al introducir un 0. Indicar la suma total, y
#cuántos han sido positivos y cuántos negativos.

#creo variables que inicien en 0 para luego usarlas
suma=0
positivo=0
negativo=0

while True: #entro directamente en el bucle
    n=int(input("Introduce un número: ")) #pido otro numero
    if n == 0:#si el numero  es 0
       print("HA INTRODUCIDO UN 0, ADIOS") #mensaje de error
       break #salgo del bucle
    suma+=n #a suma le añado el valor del numero
    if n<0: #para ver si es positivo
        negativo+=1 #añado uno al contador de positivos
    elif n>=0: #para ver si es negativo
        positivo+=1 #añado uno al contador de negativos


print("La suma de todos los números es:",suma," hay",positivo,"números positivos","y",negativo,"números negativos")