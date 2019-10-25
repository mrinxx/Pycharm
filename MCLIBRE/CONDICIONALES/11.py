#Escriba un programa que pida los coeficientes de una ecuación de segundo grado (a x² + b x + c = 0) 
# y escriba la solución.
#Se recuerda que una ecuación de segundo grado puede no tener solución, tener una solución única, 
#tener dos soluciones o que todos los números sean solución. 
#Se recuerda que la fórmula de las soluciones cuando hay dos soluciones es x = (-b ± √(b2-4ac) ) / (2a)

#AQUI VOY A PEDIR LAS VARIABLES
a=float(input("Escribe el coeficiente A de la ecuación: "))
b=float(input("Escribe el coeficiente B de la ecuación: "))
c=float(input("Escribe el coeficiente C de la ecuación: ")) 

d=b**2-4*a*c #esto es el interior de la raiz cuadrada √(b2-4ac), la cual se utilizará mas adelante
if a == b == c == 0: #Si las tres variables introducidas son 0, la ecuacion tendra como solucion todos los numeros
    print("Todos los numeros son solución")
elif a == b == 0: #Si solo A y B son 0 la ecuacion no tiene solucion, ya que c es un numero y un numero que no es 0 igual a 0 no tiene sentido
    print ("La ecuación NO tiene solución")
elif a == 0: #si solo A es 0, se procede a hacer la ecuacion de primer grado que rsulta al despejar
    x0 = -c/b #esta es la ecuacion de primer grado que quedaria, como es de primer grado solo tiene una solucion
    print("La ecuación tiene una solución: ",x0)
elif d < 0: #En este caso se coge la variable que hemos definido en d. para que la ec. se pueda resolver la raiz no puede ser menor de 0
    print("La ecuación no tiene solucion REAL")
elif d == 0: #Si d es igual a 0 solo se va a tener una solucion
    x1=-b/(2*a)
    print("La ecuación tiene una solucion", x1)
else: #Tras recorrer todos los casos quedan las dos soluciones
    x2=(-b + d**0.5)/(2*a)
    x3=(-b - d**0.5)/(2*a)
    print("La ecuación tiene DOS soluciones: ",x2," y ",x3)
pass 