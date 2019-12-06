
puntuaciones={'PJ':0,'PG':0,'PP':0,'PAF':0,'PEC':0,'MAR':0}
clasificacion={'CHB':puntuaciones, 'CAW':puntuaciones, 'CSU':puntuaciones, 'COS':puntuaciones, 'VIB':puntuaciones,'CHE':puntuaciones}
#equipos={'CHB':,'CAW':[] 'CSU' 'COS':['Conil','suns','COS','Conil Suns'], 'VIB' 'CHE'}
while True:
    resultado=input("Introduce el equipo y sus puntos: ")
    lista=str.split(resultado," ")
    if lista[0] in clasificacion:
        lista2=lista[1::]
        l=dict(zip(puntuaciones,lista2))
        clasificacion[lista[0]]=l
        print(clasificacion[lista[0]])
    #clavesclasif=clasificacion.keys()
    #clavespunt=puntuaciones.keys()
    #valores=puntuaciones.values()
    #for p in clavespunt:
     #   print("\t",p,sep=" ",end=" ")
    #for i in clavesclasif:
     #   print("\n",i,"\n",valores)
    if resultado.lower() == "fin":
        print("SALIENDO DEL PROGRAMA")
        break
