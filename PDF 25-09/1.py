#Reescribe el programa del cálculo del coste de un servicio, para darle 1.5 veces la tarifa horaria para todas las
#horas trabajadas que excedan de 40.
# Horas de trabajo: 45
#Coste por hora: 10
#Importe total: 475.0

horas=float(input("Escribe el numero de horas: "))
precio=float(input("Escribe el precio por horas: "))

recargo=0 #abro recargo para dentro de la condicion meter un valor
if horas > 40:
    exceso=horas - 40 #calculo cuantas horas exceden de 40
    recargo=(1.5*exceso)*precio #calculo el recargo que es 1.5 mas que el precio, multiplicado por el exceso
    total1=(40*precio)+recargo #calculo el precio normal de 40 horas fijas+ el recargo que tengo
    print("El precio total del servicio es de:",total1,"euros")
elif horas <= 40: #si las horas no pasan de 40
    total2=horas*precio+recargo #calculo el precio normal, se introduce recargo, que en este caso al no pasar de 40h es 0
    print("El precio total del servicio es de:",total2,"euros")

