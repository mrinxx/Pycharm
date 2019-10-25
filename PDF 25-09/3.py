#Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la puntuación está fuera de ese rango,
#muestra un mensaje de error. Si la puntuación está entre 0.0 y 1.0, muestra la calificación usando la tabla
#siguiente (el programa debe mostrar la tabla usando tabuladores):
#Puntuación Calificación
#>= 0.9 Sobresaliente
#>= 0.8 Notable
#>= 0.7 Bien
#>= 0.6 Suficiente
#< 0.6 Insuficiente
#Introduzca puntuación: 0.95
#Sobresaliente

print("Puntuación\tCalificación") #abro la tabla con tabuladores
print(">=0.9\t\tSobresaliente")
print(">=0.8\t\tNotable")
print(">=0.7\t\tBien")
print(">=0.6\t\tSuficiente")
print("<0.6\t\tInsuficiente")

nota=float(input("Introduzca una nota del 0.0 al 1.0: ")) #cojo la nota
#aqui voy a comprobar que la nota este en el rango indicado, si no que salga del programa
if nota < 0.0 or nota > 1.0:
    print("Calificación no válida")
else:
    if nota < 0.6: #SI LA NOTA ES ESTRICTAMENTE MENOR A 0.6
        print("INSUFICIENTE")
    elif nota >= 0.6 and nota <= 0.7: #SI LA NOTA ESTA ENTRE 0.6 Y 0.7
        print ("SUFICIENTE")
    elif nota >= 0.7 and nota <= 0.8: #SI ESTA ENTRE 0.7 Y 0.8
        print("BIEN")
    elif nota >= 0.8 and nota <= 0.9: #SI ESTA ENTRE 0.8 Y 0,9
        print("NOTABLE")
    elif nota >= 0.9: #SI ES 0.9 O MAYOR
        print("SOBRESALIENTE")
pass
