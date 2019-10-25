#Escriba un programa que pida una temperatura en grados Fahrenheit y que escriba esa temperatura en grados Celsius.
#Se recuerda que la relación entre grados Celsius (C) y grados Fahrenheit (F) es la siguiente: C = (F - 32) / 1,8

temperaturaenf= float(input("Escribe una temperatura en F: ")) #pido la temperatura en F
pasoac = (temperaturaenf - 32 )/1.8 #paso la temperatura a C

print (temperaturaenf," grados fahrenheit son", pasoac, " grados centígrados")