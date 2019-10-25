#Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.

num1=int(input("Escribe un numero: "))
num2=int(input("Escribe un numero: "))

#PRIMERO VOY A COMPARAR Y GUARDAR EN UNA VARIABLE QUE NUMERO ES MAYOR Y QUE NUMERO ES MENOR
if num1>num2:
    mayor=num1
    menor=num2
else:
    mayor=num2
    menor=num1
pass

#UNA VEZ OBTENGA LAS VARIABLES CON SUS RESPECTIVOS VALORES MIRARE LOS RESTOS PARA SABER SI SON O NO MUTIPLOS

if mayor%menor == 0:
    print (mayor," es múltiplo de ", menor)
else:
    print (mayor," no es múltiplo de ", menor)
pass