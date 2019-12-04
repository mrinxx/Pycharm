#Disena un programa que, a partir del valor del lado de un cuadrado (3 metros), muestre el valor de su 
# perımetro (enmetros) y el de su ´area (en metros cuadrados).
#(El perımetro debe darte 12 metros y el ´area 9 metros cuadrados.) 
#EJERCICIO CON NUMEROS ENTEROS

lado=int(input("Introduce el lado del cuadrado: ")) #pido el lado
perimetro=lado*4 #calculo el perimetro
area=lado**2 #calculo el area
print("El area del cuadrado es",area,"metros cuadrados y el perimetro es",perimetro,"metros") #muestro el resultado
