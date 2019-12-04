#Dise˜na un programa que pida el valor de los tres lados de un tri´angulo y calcule el valor de su ´area y per´ımetro.
#Recuerda que el ´area A de un tri´angulo puede calcularse a partir de sus tres lados, a, b y c, ası:
#  A = (s(s − a)(s − b)(s − c))**1/2 donde s = (a + b + c)/2.

l1=float(input("Introduce un lado del triangulo: "))
l2=float(input("Introduce otro lado del triangulo: "))
l3=float(input("Introduce el ultimo lado del triangulo: "))

s=(l1+l2+l3)/2

a=(s*(s-l1)*(s-l2)*(s-l3))**0.5
p=l1+l2+l3
print("El area del triangulo es",a,"y el perimetro",p)