#Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de una persona y que calcule su índice de masa corporal (imc).

peso=int(input("Escriba su peso en kg: "))
altura=float(input("Escriba su altura en metros: "))

imc=peso/(altura*altura) #el elevado se expresa como ** seguido de la potencia

print ("Su imc es de: ", imc)