def raices(a,b,c): #abro la funcion
    discriminante=(b**2)-(4*a*c) #creo el discriminante para ver si es positivo o no (no puede ser menor que 0 una raiz)
    if discriminante >= 0: #si el discriminante es mayor o igual a 0
        r1=(-b + (discriminante ** 0.5)) / (2 * a) #raices positivas
        r2=(-b - (discriminante ** 0.5)) / (2 * a) #raices negativas
        return r1,r2 #lo que va a salir fuera de la funcion

if __name__ == "__main__": #bloque principal del programa
    #pido los 3 coeficientes de la ecuacion
    a=float(input("Introduce el coeficiente a: "))
    b=float(input("Introduce el coeficiente b: "))
    c=float(input("Introduce el coeficiente c: "))
    if (b**2)-(4*a*c) < 0: #si el discriminante es menor a 0
        print("No es posible calcular las raices") #error
    else: #si no
        raices=raices(a,b,c) #llamo a la funcion
        print("Las raices de la ecuación son:",raices) #la muestro
    pass