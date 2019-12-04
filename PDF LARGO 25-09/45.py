#Disena un programa que solicite el radio de una circunferencia y muestre su area y perımetro con solo 2 decimales

radio=float(input("Introduce el radio de la circunferencia:"))
p=3.14
area=p*radio**2
perimetro=2*p*radio

print("El area y el perimetro de la circunferencia son",round(area,2),"y",round(perimetro,2),"respectivamente")
