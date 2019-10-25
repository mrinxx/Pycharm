#Diseña un programa que lea la edad de dos personas y diga quien es mas joven, la primera o la segunda. Ten en
#cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.

edad1=int(input("Introduce la edad de la primera persona: "))
edad2=int(input("Introduce la edad de la segunda persona: "))

if edad1 == edad2:
    print("Tienen la misma edad")
elif edad1 > edad2:
    print("La primera persona es mayor")
else:
    print("La segunda persona es la mayor")
pass