#Disena un programa que pida el valor de los dos lados de un rect´angulo y muestre el valor de su perımetro 
# y el de su area
#EJERCICIO CON DECIMALES

l1=float(input("Introduce un lado: "))
l2=float(input("Introduce otro lado: "))

perimetro=(2*l1)+(2*l2)
area=l1*l2

print("El area del rectangulo es:",area,"metros cuadrado y el perimetro",perimetro,"metros")
