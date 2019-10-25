#Mejore el programa anterior haciendo que el programa avise cuando se escriben valores negativos o nulos.
num1=int(input("Escribe un numero: "))
num2=int(input("Escribe un numero: "))

if num1 == 0 or num2 == 0: #SE COMPARAN SI LOS DOS NUMEROS SON IUALES A 0
    print("Lo siento, este programa no admite valores nulos.")
elif num1 < 0 or num2 < 0: #SE COMPARAN LOS NUMEROS SI SON MENORES A 0 EN CASO DE QUE NO SEAN 0
    print("Lo siento, este programa no admite valores negativos.")
elif num1 >= num2 and num1 % num2 != 0: #SI NUMERO 1 ES MAYOR O IGUAL A NUM2 Y EL RESTO NO ES 0
    print(num1," no es múltiplo de ", num2)
elif num1 >= num2 and num1 % num2 == 0: #SI NUMERO 1 ES MAYOR O IGUAL A NUM2 Y EL RESTO SI ES 0
    print(num1," es múltiplo de ", num2)
elif num1 < num2 and num2 % num1 != 0: #SI NUMERO 1 MENOR A NUM2 Y EL RESTO NO ES 0
    print(num2," no es múltiplo de ", num1)
else:
    print(num2,"  es múltiplo de ", num1)
pass