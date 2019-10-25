#Mostrar los 50 primeros números pares a partir del 0, separados por comas y en orden creciente. O sea:
lista=[] #creo una lista

for i in range(0,100,2): #hago un bucle que recorra el rango que hay entre el 0 y el 100 cogiendo solo los numero pares
    lista.append(i)#en cada ciclo añado el numero correspondiente

print(lista)#ya fuera del bucle muestro la lista que he creado