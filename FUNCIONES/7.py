#Crear una función que devuelva si una fecha es válida reutilizando la función del ejercicio 3.6.

def fechacorrecta(f): #defino la funcion
    f=str.split(f,"-") #hago un split del string introducido
    d=int(f[0]) #defino el dia
    m=int(f[1]) #el mes
    a=int(f[2]) #el año

    if d>=1 and d<=31: #si el dia esta entre 1 y 31
        if m>=1 and m<=12: #si el mes esta entre los que pertenecen a un año
            if (m == 1 or m==3 or m == 5 or m == 7 or m == 8 or m == 10) and d<=31: #si esta entre los meses que tienen 31 dias y el dia es igual o menor que 31
                s=("es una fecha correcta") #la fecha es correcta
            elif  (m == 4 or m==6 or m == 9 or m == 11) and d<=30: #si el mes tiene 30 dias y el dia es igual o menor a 30
                s=("es una fecha correcta") #la fecha es correcta
            elif m==2 and d<=28: #si es el mes 2 y el dia es menor o igual a 28
                s=("es una fecha correcta")
            elif (a%400 ==0 or ( a%4==0 and  a%100!=0)) and d==29 and m==2: #si el año es bisiesto, febrero y el dia es el 29
                s=("es una fecha correcta")
            else:
                s=("es una fecha incorrecta")     
        else:
            s=("es una fecha incorrecta")
    else:
        s=("es una fecha incorrecta")

    return s #devolvera s


if __name__ == "__main__": #en el bloque principal
    fecha=input("Introduce una fecha: ") introduzco la fecha
    solucion=fechacorrecta(fecha) #llamo a la funcion con la fecha introducida
    print(fecha,solucion) #muestro el resultado
    pass