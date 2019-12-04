#Introducir	una	cadena	por	teclado	e	imprimirla	sin	vocales, sin consonantes y con las vocales en mayúsculas
# (las consonantes	deben	quedarse	tal	como	estén).

p=input("Introduce una palabra: ") #introduzco la palabra

p=list(p) #el string lo convierto a una lista

vocales= 'aeiouAEIOU' #uso esta variable para almacenar vocales mayusculas y minusculas
sinvocales=[] #creo una lista vacia para el primer objetivo (mostrar la palabra sin vocales)
sinconsonantes=[] #creo una lista para mostrar la palabra sin consonantes
mayusculas=[] #creo una lista para mostrar las vocales en mayusculas


for i in p: #para los valores en la lista de la palabra
    if i not in vocales: #si la variable no esta en la cadena de las vocales
        sinvocales.append(i) #lo añado a la lista que he creado para almacenar SOLO las consonantes(sinvocales)

sinvocales="".join(sinvocales)    #convierto la lista a cadena

for m in p: #para los valores en la lista de la palabra
    if m in vocales: #si la variable se encuentra en la cadena de las vocales, es decir, si es vocal
        sinconsonantes.append(i) #lo añado a la lista que creo para almacenar SOLO las vocales (sinconsonantes)

sinconsonantes="".join(sinconsonantes) #convierto la lista a string

for s in p: #para los valores en la lista de la palabra
    #si se encuentran vocales, las convierte en mayusculas y las añade a la lista creada para ello, pero
    #tambien se introduciran las consonantes, aunque en minuscula
    if s == "a": 
        s = "A"
    elif s == "e":
        s="E"
    elif s == "i":
        s="I"
    elif s == "o":
        s = "O"
    elif s=="u":
        s ="U"
    mayusculas.append(s) #aqui se añade

mayusculas="".join(mayusculas) #lo convierto a string

#muestro las tres listas que he creado con los valores que se ha pedido
print(sinvocales)
print(sinconsonantes)
print(mayusculas)

        
