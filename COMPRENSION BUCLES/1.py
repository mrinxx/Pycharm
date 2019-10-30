#¿Cuántas veces se ejecuta el print del siguiente código? ¿Cuál será el resultado por pantalla?
a=9
for i in range(0,100):
    if 0==a%4 or i%8==0:
        print("a",end=" ")

#Se ejecuta 13 veces (i%8) ya que hay 13 numeros que al dividirlos entre 8 en el rango dan 0
#el resultado será 13 a
