#Disena un programa que, dado un numero real que debe representar la calificacion numerica de un examen, 
#proporcionela calificacion cualitativa correspondiente al numero dado. La calificacion cualitativa sera 
#una de las siguientes: ✭✭Suspenso✮✮ (nota menor que 5), ✭✭Aprobado✮✮ (nota mayor o igual que 5, pero 
#menor que 7), ✭✭Notable✮✮ (nota mayor o igual que 7, pero menor que 8.5), ✭✭Sobresaliente✮✮ 
#(nota mayor o igual que 8.5, pero menor que 10), ✭✭Matr´ıcula de Honor✮✮ (nota 10).

nota=float(input("Introduce la nota del examen: "))
if nota < 5:
    print ("SUSPENSO")
elif nota >=5 and nota < 7:
    print("Aprobado")
elif nota >=7 and nota < 8.5:
    print("NOTABLE")
elif nota >=8.5 and nota<10:
    print("SOBRESALIENTE")
elif nota==10:
    print("MATRICULA DE HONOR")
else:
    print ("CALIFICACION NO VALIDA")