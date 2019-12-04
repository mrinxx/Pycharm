def numero_aleatorio():
    import random
    aleatorio=[]
    d=0
    while d < 5:
        num=random.randrange(start=0,stop=9)
        num=str(num)
        if num in aleatorio:
            continue
        else:
            aleatorio.append(num)
        d+=1
    aleatorio="".join(aleatorio)
    return aleatorio

def numero_comprobacion(n1,n2):
    while True:
        muertos=0
        heridos=0
        estan=[]
        n2=input("Introduce un numero de 5 cifras: ")
        try:
            n2=int(n2)
            n2=str(n2)
            if len(n2)!=5:
                s="ESTE NUMERO NO TIENE 5 CIFRAS"
                continue
            else:
                for i in n2:
                    if i not in estan:
                        estan.append(i)
                    else:
                        s="NO PUEDE CONTENER VALORES REPETIDOS"
                        continue
            if n1 == n2: 
                s="CORRECTO, HAS ACERTADO!!!. ME PARECE QUE HAS HECHO TRAMPA"
                break
            else:
                for d in n2:
                    if (d in n1) and (n2.index(d) == n1.index(d)):
                        muertos+=1
                    elif (d in n1) and (n2.index(d) != n1.index(d)):
                        heridos+=1
                s=(muertos,"muertos y",heridos,"heridos")
            continue
        except ValueError:
            s="INTRODUCE SOLO NUMEROS"
            continue
        return s
          
if __name__ == "__main__":
    d1=numero_aleatorio()
    resultado=numero_comprobacion(d1)
    pass