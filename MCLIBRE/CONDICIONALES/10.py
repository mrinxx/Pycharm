#Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
#Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos 
# los números sean solución. Se recuerda que la fórmula de las soluciones es x = -b / a

a=float(input("Indroduce el coeficiente a de la ecuación: "))
b=float(input("Indroduce el coeficiente b de la ecuación: "))

if a == b == 0:
    print("Todos los numeros son la solución de la ecuación")
elif a == 0:
    print ("La ecuación NO tiene solución")
else:
    x=-b/a
    print ("La ecuación tiene una sola solución, la cual es: ",x)
pass