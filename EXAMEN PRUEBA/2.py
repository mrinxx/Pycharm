

votaciones=dict()
votaciones={'Louganis':[],'Xiao':[],'Perez':[],'Gordon':[],'Chan':[]}
while True:
    opcion=input("¿Qué desea hacer?: ")
    #if opcion.lower()=votaciones[]
    if opcion.lower()=="saltos":
        print(votaciones)
        continue
    if opcion.lower()=="clasificacion":
        orden=sorted(votaciones.items())
        for i in orden:
            for p in range (1,6): 
                print(p,i)
    if opcion.lower()=="salir":
        print("SALIENDO DEL PROGRAMA")
        break

print(votaciones)