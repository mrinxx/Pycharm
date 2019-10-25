#Mejore el programa anterior haciendo que no se escriban las unidades innecesarias (cuando el valor es cero).

cantidad=int(input("Introduzca la cantidad de centímetros: "))

kilometros= cantidad//100000 #Se hace la division entera de la cantidad para pasarla a km
metros= cantidad%100000 //100 #Se hace el resto de lo que queda hipoteticamente en km y se divide /100 para tener los metros
centimetros= cantidad%100 #se coge la cantidad y se hace el resto para ver cuanto queda

if kilometros == 0 and metros != 0: #Si los kilometros son 0 pero el numero de metros no es nulo
    print(cantidad," cm son: ",metros," metros y ",centimetros," centímetros")
elif kilometros==0 and metros == 0: #tanto si km como metros son nulos
    print(cantidad," cm son: ",centimetros," centímetros")
else: #si ninguno es nulo
    print(cantidad," cm son: ",kilometros," kilómetros, ",metros," metros y ",centimetros,"centímetros")
pass