#Crear un programa para gestionar una agenda	de	contactos. El funcionamiento	será el	siguiente:
 #   • El	programa	pedirá introducir	algo por teclado:
  #      o Si se	introduce un número	de	teléfono comprobará si	existe, si	es	así mostrará a	
   #     quién pertenece. Si no existe pedirá el nombre	del	contacto para darlo	de	alta.
    #    o Si se introduce un contacto debe	comprobar si existe, si	es así mostrará el número de teléfono.	 
     #   Si no existe	pedirá el número de	teléfono para darlo	de	alta.
#    • Debe	reconocer números de teléfono con espacios	entre los dígitos o no y con el	símbolo	+ al principio
#   	para indicar prefijo de	país.
 #   • Los	nombres	deben comenzar	por	letras	y pueden contener números y	caracteres	especiales	imprimibles.
 #   • Comandos	especiales:
 #       o adios: Sale	del	programa
  #      o listado:	Muestra	el	listado	completo de	contactos	ordenados por	nombre
   #     o consulta	texto:	Muestra	el	listado	de	los	contactos que contengan texto o	“Ningún	contacto” 
   #        si no	hubiera	ninguno.
   
agenda_contactos=dict() #inicializo el diccionario

seleccion=input("Seleccione una opcion: ") #hago que se introduzca la seleccion
numeros=agenda_contactos.values() #cojo los valores del diccionario
if seleccion.lower()=="numero de telefono": #si la seleccion es el numero de telefono
    num=input("Introduce el numero de telefono: ") #hago que se introduzca el numero
    num=list(num) #creo una lista con el numero introducido
    if num[0]!="+": #si el primer elemento no es el + del prefijo
        print("NUMERO NO CORRECTO") #fuera
        exit #salgo del programa
    else: #si es
        t=0 #inicializo variable para llevar el control del elemento
        for d in num: #para cada elemento en la lista del numero para ver si cada 3 numeros hay un espacio
            t+=1 #añado 1 a t
            if (t == 4 or t == 8 or t==12) and d==" ": #si t coincide con los espacios del numero paso
                continue #y continuo con el bucle
        try: #si paso el byucle anterior
            del num#qelimino este elemento que es el + del prefijo
            c=0 # inicializo otro contador de digitos
            for n in num: #para cada numero en la lista
                c+=1 #añado un contador que cuente la posicion
                if (c==3 or c==7 or c==11) and n==" ": #si es un espacio y esta en la posicion correspondiente
                    continue #continua
                else: #si no 
                    n=int(n) #intenta convertirlo a entero
        except ValueError: #en caso de que de un error (que no sea espacio o )
            print("NUMERO NO CORRECTO") #muestro el mensaje
            exit #salgo
        else: #si se cumple continuo el codigo
            if num in numeros: #si el numero introducido esta en los valores del diccionario
                print("El número introducido pertenece a: ", agenda_contactos[num]) #muestro
            else: #si no
                num="".join(num) #convierto el numero a cadena
                #voy a introducir en el diccionario el nombre de la persona cpn ese numero
                agenda_contactos[input("Introduce el contacto para darlo de alta: ")]="+"+num
elif seleccion.lower() == "contacto": #si es esta seleccion
    con = input("Introduce el contacto: ") #introducimos el contacto
    if con in agenda_contactos: #si el contacto esta 
        print("El contacto indicado tiene el número de teléfono: ",agenda_contactos[con]) #muestro su numero
    else: #si no esta
        agenda_contactos[con]=input("Introduce el numero de telefono del contacto: ") #añado el contacto
elif seleccion.lower()=="adios": #si es esta seleccion
    print("SALIENDO DEL PROGRAMA")
    exit #salgo del programa
elif seleccion.lower()=="listado": #si es esta seleccion
    print("MOSTRANDO EL LISTADO DE CONTACTOS")
    lista_orden=sorted(agenda_contactos.items()) #ordeno el diccionario
    print(lista_orden) #lo muestro
elif seleccion.lower()=="consulta texto":
    c=agenda_contactos.get("Contacto","No hay contacto")
    print(c)

