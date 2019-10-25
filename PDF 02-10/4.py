#Realizad el mismo ejercicio anterior y además hallar la suma de todos los números visualizados.

lista=[] #creo una lista
total=0 #empiezo el conador total en 0
for i in range(0,100,2): #hago un bucle que recorra el rango que hay entre el 0 y el 100 cogiendo solo los numero pares
    lista.append(i)
    total+=i#en cada ciclo sumo el valor de i al total

print(lista)
print ("La suma de todos los numeros mostrados es:",total)