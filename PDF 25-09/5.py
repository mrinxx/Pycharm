#Escribe un programa que solicite tres números al usuario y muestre el mayor de ellos.

lista=[] #creo una lisa vacia

#voy a pedir los numeros a comparar
numero1=float(input("Inserte el primer numero: "))
numero2=float(input("Inserte el segundo numero: "))
numero3=float(input("Inserte el tercer numero: "))

#añado los tres numeros a la lista vacia
lista.append(numero1)
lista.append(numero2)
lista.append(numero3)
#abro una variable mayor que sea igual a 0 para luego comparar
mayor=0

#abro un bucle que por cada numero en la lista me lo compare unicamente con mayor y si es el mayor
#sustituyo el valor de mayor por el valor de la lista que toque
for i in lista:
    if i > mayor:
        mayor= i
    pass
#muestro el mayor0
print("El mayor número es:",mayor)