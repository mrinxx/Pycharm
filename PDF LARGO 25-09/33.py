#Disena un programa que, a partir del valor de los dos lados de un rectangulo (4 y 6 metros, 
# respectivamente), muestre el valor de su per´ımetro (en metros) y el de su ´area (en metros cuadrados).
#(El per´ımetro debe darte 20 metros y el ´area 24 metros cuadrados.)
#EJERCICIO CON ENTEROS

l1=float(input("Introduce un lado: "))
l2=float(input("Introduce otro lado: "))

perimetro=(2*l1)+(2*l2)
area=l1*l2

print("El area del rectangulo es:",area,"metros cuadrado y el perimetro",perimetro,"metros")
