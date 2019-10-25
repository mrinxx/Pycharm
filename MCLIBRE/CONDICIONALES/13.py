#Escriba un programa que pida una distancia en centímetros y que escriba esa distancia en 
#kilómetros, metros y centímetros (escribiendo todas las unidades).

#// ES DIVISION ENTERA

cantidad=int(input("Introduzca la cantidad de centímetros: "))

kilometros= cantidad//100000 #Se hace la division entera de la cantidad para pasarla a km
metros= cantidad%100000 //100 #Se hace el resto de lo que queda hipoteticamente en km y se divide /100 para tener los metros
centimetros= cantidad%100 #se coge la cantidad y se hace el resto para ver cuanto queda

print(cantidad," cm son: ",kilometros," kilómetros, ",metros," metros y ",centimetros," centímetros")
 
