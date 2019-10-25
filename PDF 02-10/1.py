#Escribe un programa que lea repetidamente números hasta que el usuario introduzca “fin”. Una vez lo haya
#hecho, muestra por pantalla la suma total, la cantidad y la media de esos números. Si el usuario introduce otra
#cosa que sea un número ni “fin”, debe mostrar un error y pasar al número siguiente.

suma=0 #contador para la suma
cantidad=0 #contador para la cantidad de numeros que introduzco

while True: #con while true va a entrar en el bucle si o si
    n=input("Introduce un numero:") #pido lo que sea por pantalla
    if n=="fin": #abro la condicion primero para verificar si lo que he introducido es la cadena que para el bucle
        print("ERROR")#si es fin muestra el error
        break#luego sale del programa
    n=int(n)#si no es fin lo que hago es pasar la variable n a un entero
    suma+=n #suma los valores
    cantidad+=1 #incrementa la cantidad en 1
    media=suma/cantidad #calculo la media
    print("La suma es: ",suma,", se han introducido",cantidad,"números y la media es",media)#muestro

print("La suma final es: ",suma,", se han introducido ",cantidad,"números y la media es ",media)

