#Adivinar el resultado del programa introduciendo: 3, 8 y 13. ¿Qué hace el programa?

try:
    a=int(input("numero: "))
    p=True
    for n in range(2,a):
        if not a%n:
            p=False
            break
    if p:
        print("si")
    else:
        print("no")
except:
    print("no es un numero: ")

#3:mostrara si
#8:mostrara no
#13:Mostrara si
#Primero comprueba si lo que se introduce es un numero o no, si no lo es, muestra el mensaje de error. Si es un numero se
#abre la variable p como verdadero, luego para todos los valores comprendidos entre 2 y el numero introducido, si el  
#numero del rango que toca en ese momento no es divisible entre el que hemos introducido, la variable p toma el valor falso.
#Si p es falso, mostrará si pero si es verdadero, se mostrará no