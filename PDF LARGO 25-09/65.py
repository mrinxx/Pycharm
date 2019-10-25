#Dise˜na un programa que, dado un n´umero entero, determine si ´este es el doble de un n´umero impar. (Ejemplo: 14 es
#el doble de 7, que es impar.)

numero=int(input("Introduce un numero: ")) #pido un numero entero

mitad=numero/2 #en una variable almaceno su mitad

if mitad%2 != 0: #si la mitad es impar
    print(numero,"es el doble de",mitad,"que es impar")
else: #si no lo es
    print("Su mitad NO es impar")
    pass
