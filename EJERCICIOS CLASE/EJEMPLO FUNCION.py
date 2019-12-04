def sumatorio(lista): #una lista se define escribiendo def+nombre+(NOMBRE QUE VA A USAR LA VARIABLE DENTRO), 
                    #no importa el nombre, ya que cuando llegue a la funcion tomará el nombre indicado
    if lista[0] != type(1): #si el primer valor de la lista no es un entero
        return False #EL RETURN ES LO QUE QUEREMOS QUE SALGA AL EXTERIOR DESDE NUESTRA FUNCION
    for i in lista:
        resultado+=i
        return resultado
                            #MUY IMPORTANTE QUE EN LAS FUNCIONES JAMAS HAYA PRINT
if __name__=="__main__": #Si el nombre de lo que estoy ejecutando es el main --> INDICA QUE ES EL PROGRAMA EN SI, LO QUE SE EJECUTA
    print("hola")
    numeros=[1,2,3,4,5,6,7]
    sumatorio=sumatorio(numeros)#llamo a la funcion
    print (sumatorio)#muestro lo que salga de la funcion, que en este caso sera falso
