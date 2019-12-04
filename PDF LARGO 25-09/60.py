#Disena un programa que lea la edad de dos personas y diga quien es mas joven, la primera o la segunda. 
# Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.

e1=int(input("Introduce la edad de la primera persona: "))
e2=int(input("Introduce la edad de la segunda persona: "))

if e1<e2:
    print("La primera persona es menor")
elif e2<e1:
    print("La segunda persona es menor")
else:
    print("Las dos personas tienen la misma edad")