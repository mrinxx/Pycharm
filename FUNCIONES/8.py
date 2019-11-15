#Usar las funciones de los ejercicios 3.6 y 3.7 para reescribir el ejercicio 2.24 (Introducir por teclado la fecha actual 
#y la fecha de nacimiento del usuario (día, mes y año) e indicar si es mayor de 20 años.)

def comprobacion(f1,f2): #defino la funcion
    #hago un split de las fechas
    fa=str.split(f1,"-")
    fn=str.split(f2,"-")

    #determino que es lo que es cada termino
    da=int(fa[0])
    ma=int(fa[1])
    aa=int(fa[2])

    dn=int(fn[0])
    mn=int(fn[1])
    an=int(fn[2])

    m31=[1,3,5,7,8,10,12] #meses con 31 dias
    m30=[4,6,9,11] #meses con 30 dias

#compruebo si la fecha es valida
    if dn in range (1,32) and da in range (1,32): #si el dia esta entre 1 y 31
        if (mn in range (1,13)) and (ma in range(1,13)): #si el mes esta entre los que pertenecen a un año
            if (mn in m31 and dn<=31) or (ma in m31 and da<=31): #si esta entre los meses que tienen 31 dias y el dia es igual o menor que 31
                n=True
            elif (mn in m30 and dn<=30) or (ma in m30 and da<=30): #si el mes tiene 30 dias y el dia es igual o menor a 30
                n=True
            elif (mn==2 and dn<=28) or (ma==2 and da<=28): #si es el mes 2 y el dia es menor o igual a 28
                n=True
            elif ((an%400 ==0 or ( an%4==0 and  an%100!=0)) and (dn==29 and mn==2)): #si el año de nacimiento es bisiesto y hay 29 de febrero
                n=True
            elif ((aa%400 ==0 or ( aa%4==0 and  aa%100!=0)) and (da==29 and ma==2)): #si el año actual es bisiesto, febrero y el dia es el 29
                n=True
            else:
                n=False
        else:
            n=False
    else:
        n=False

    s=" " #INICIALIZO S PORQUE ME DA UN ERROR
    if n==True: #en caso de que n sea verdadero (fechas validas)
        #calculo si es mayor de 20 
        if aa-an > 20: 
            s="Mayor de 20"
        elif aa-an == 20 and ma>mn:
            s="Mayor de 20"
        elif aa-an == 20 and ma==mn and da>=dn:
            s="Mayor de 20"
    else:
        s="Menor de 20"

    return s #devolvera s

if __name__ == "__main__": #en el bloque principal
    #introduzco las fechas
    actual=input("Introduce la fecha de hoy: ")
    nacimiento=input("Introduce la fecha de nacimiento: ")
    resultado=comprobacion(actual,nacimiento) #llamo a la funcion
    print (resultado) #muestro
    pass