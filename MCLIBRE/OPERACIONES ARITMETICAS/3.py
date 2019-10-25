#Escriba un programa que pida una distancia en pies y pulgadas y que escriba esa distancia en centímetros.
#Se recuerda que un pie son doce pulgadas y una pulgada son 2,54 cm.

pies = float(input("Escribe una distancia en pies: ")) #cojo los pies
pulgadas = float(input ("Escribe una distancia en pulgadas: ")) #cojo las pulgadas

piesenpulgadas=pies*12 #paso pies a pulgadas
totalpulgadas=pulgadas+piesenpulgadas #sumo todas las pulgadas
totalencm=totalpulgadas*2.54 #paso todas las pulgadas a cm

print(pies," pies y ",pulgadas," pulgadas son: ",totalencm," cm")
