#Adivinar el resultado del programa introduciendo: 3, aa y 6.

try:
    n=int(input("numero"))
except:
    n=3
a=1

for i in range(n,0,-1):
    print(" "*i+"*"*a)
    a+=2
print(" "*(n-1)+"*"*3)

#Se comprobará si lo que introducimos es un numero(n), si no es asi, a la variable se le añade el valor 3 y se inicializa 
# una variable a en 2, entra en un bucle que vaya desde n hasta 0 quitando 1.
#imprimirá espacios por el valor de i y asteriscos por valor de a, sumará a la variable a 2 por cada vuelta de bucle y 
#al final imprimirá espacios por el valor de n-1 y 3 asteriscos
#3 --> Apareceran una serie de asteriscos: 1 asterisco y 3 espacios, 3 asteriscos y 2 espacios, 5 asteriscos y un espacio
# y finalmente 3 asteriscos y 2 espacios
#aa --> Como es una letra, hará lo mismo que en el caso anterior ya que n se establece como 3
#6 --> Aparecerá la sigiente serie: 1 asterisco y 6 espacios, 3 asteriscos y 5 espacios, 5 asteriscos y 4 espacios,
#7 asteriscos y 3 espacios, 9 asteriscos y 2 espacios,11 asteriscos y un espacio y finalmente 3 asteriscos y 2 espacios