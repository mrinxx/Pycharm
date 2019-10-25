n=input("Introduce un número en el sistema HEXADECIMAL: ")
n=list(n) #convierto lo anterior a una lista 
listavalores=[] #abro una nueva lista para almacenar futuros valores
valor=0 #inicializo variable para almacenar el valor total del numero


for i in n: #para todos los valores que haya en n
    if (i>='a' and i<='f') or (i>='0' and i<='9' ): #si los valores estan en los digitos utilizados en el sistema hexadecimal
        if i =='a': #se va poniendo la equivalencia de la letra en numero
            i=10
        elif i=='b':
            i=11
        elif i =='c':
            i=12
        elif i =='d':
            i=13
        elif i =='e':
            i=14
        elif i =='f':
            i=15
        i=int(i) #convierto el valor que sea a un entero para realizar posteriormente operaciones
        listavalores.append(i) #añado el valor a la lista quealmacena los valores numericos
    else: #si no está entre los caracteres utilizados
        print("El número hexadecimal no es válido")
        exit

listavalores.reverse() #le doy la vuelta a la lista
print(listavalores)

for m in range(len(listavalores)): #para todos los valores que esten en el rango del len de listavalores
    posicion=m #la posicion será m, que será 0,1,2....
    valor+=listavalores[m]*16**m  #multiplico el numero por 16 elevado a su posicion

n="".join(n) #convierto a cadena de caracteres
print("El valor del número hexadecimal",n,"es",valor)#muestro