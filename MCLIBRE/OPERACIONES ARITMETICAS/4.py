#Escriba un programa que pida una temperatura en grados Celsius y que escriba esa temperatura en grados Fahrenheit.
#Se recuerda que la relación entre grados Celsius (C) y grados Fahrenheit (F) es la siguiente: F = 1,8 * C + 32

temperaturaenc= float(input("Escribe una temperatura en C: ")) #Pido la temp en grados C
pasoaf= 1.8*temperaturaenc+32 #paso la temperatura anterior a F

print(temperaturaenc," grados centígrados son ",pasoaf," grados fahrenheit") 