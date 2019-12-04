#Un capital de C euros a un inter´es del x por cien anual durante n anos se convierte en C ·(1 + x/100)n 
# euros. Disena un programa Python que solicite la cantidad C y el interes x y calcule el capital final
# solo si x es una cantidad positiva.

capital=float(input("Introduce el capital: "))
interes=float(input("Introduce el interes: "))
anhos=float(input("Introduce el tiempo: "))

cfinal=capital*(1+interes/100)**anhos 

if interes >=0:
    print (cfinal)