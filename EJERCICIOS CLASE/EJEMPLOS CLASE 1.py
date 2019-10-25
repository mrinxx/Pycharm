print ("hola mundo") # saca hola mundo
a = 5 #almacena 5 pero no sale
print ("El valor de a es: ", a) #saca el valor de a concatenado con el string, se pueden realizar operaciones ej: a+1
b = "Marina"
lista = [b, "Ocaña", [1,2],True] #b es la variable anteriormente declarada
print (lista[0]) #imprimira MARINA
print (lista[2]) #imprimira [1,2] para indicar que a su vez es un array 
print (lista[2][0]) #imprimira 1 porque coge el primer dato del array 
lista.append("Nuevo") #La función append hace que al final de la lista se añada el valor nuevo
print (lista)
tupla = (a,"Ocaña", True)
print (tupla) #Sacara por pantalla toda la tupla entera, se puede hacer con listas, arrays...
Diccionario = {"Marina" :"Ocaña", "Laura":"Ocaña"}
print(Diccionario["Marina"]) #imprime el valor del apellido para el valor Marina, busca y muestra
print(Diccionario.keys()) #Sacará todas las claves del diccionario
print(Diccionario.values()) #Sacará todos los valores del diccionario 
c= sum(range(0,6)) #añado un rango de numeros del 0 al 5 y hago su sumatorio
print (c) #saca porpantalla el sumatorio
#CONDICIONES
#Condicion 1
entrada= input("Variable de la condicion: ") #Pedirá un numero por pantalla
entrada = int(input("Variable de la condicion: ")) #Se realiza una conversion de una cadena a un numero entero ya quetodo lo que entra por el input es una cadena de texto y queremos compararlo en este caso con un numero
if entrada > 5:
    print("Se cumple")
    pass
#Condicion 2 --> Si el valor introducido por teclado es un numero entero, sacará que "Se cumple"
entrada = int(input("Variable de la condicion: "))
if type(entrada) == int:
    print("Se cumple")
    pass
#Condicion 3
entrada = int(input("Variable de la condicion: "))
if entrada > 17:
    print ("Sale del instituto")
else:
    print ("No sale del instituto")
    pass