#pido las fechas
fn=input("Introduce dia, mes y año de nacimiento: ")
fa=input("Introduce dia, mes y año actual: ") 

#convierto a cadena y paso el separador que quiero
fa=str.split(fa,"-")
fn=str.split(fn,"-")

#cada elemento de las listas se correspondera con dia, mes y año tanto actual como de nacimiento. Además, los convierto
#a tipo entero para poder operar con ellos
dian=int(fn[0])
mesn=int(fn[1])
anhon=int(fn[2])

diaa=int(fa[0])
mesa=int(fa[1])
anhoa=int(fa[2])


if anhoa-anhon > 20: #si la restas de los dos años de por si es mayor que 20
    print ("Es mayor de 20")
elif anhoa-anhon == 20 and mesa>mesn: #si laresta de los dos años es igual a 20 "pero ya ha pasado el mes de nacimiento del usuario"
    print ("Es mayor de 20")
elif anhoa-anhon == 20 and mesa==mesn and diaa>=dian: #si es la resta de los años da justamente 20, mismo mes pero el dia es el mismo o va despues que el de nacimiento
    print ("Es mayor de 20")
else:
        print("Es menor de 20")




