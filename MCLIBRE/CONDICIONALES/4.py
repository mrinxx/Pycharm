#Escriba un programa que pida el año actual y un año cualquiera 
#y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

actual=int(input("Introduce el año actual: "))
cualquiera=int(input("Introduce un año cualquiera: "))

if actual<cualquiera:
    print("Faltan ",cualquiera-actual,"años para el año ",cualquiera)
else:
    print("Han pasado ",actual-cualquiera," años desde el ",cualquiera)
pass

#TAMBIEN SE PODRIA PONER UNA CONDICION DE SI EL AÑO ES EL MISMO PARA QUE LO INDIQUE