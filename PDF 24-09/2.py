#Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total
#del servicio

horas=int(input("Introduzca las horas trabajadas: "))
precio=float(input("Introduzca el precio por horas: "))
total=horas*precio
print ("El total a ganar es de: ",total," euros")