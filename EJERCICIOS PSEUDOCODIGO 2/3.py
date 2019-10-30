#Dada la siguiente serie: a1=0, a2=1, an=3*an-1+2*an-2 (para n>=3)
#Calcular el valor y el rango (la n) del primer término mayor o igual a 1000.

a=0 #a empieza en 0
b=1 #b empieza en 1
n=0 #inicializo la variable n (rango) para ir sumando
v=0 #inicializo v (valor) para usarla luego

while True: #SIEMPRE ENTRO EN EL BUCLE
    v=a+b #c sera la suma de a y de b
    a=b #a sera sustituida por el valor de b (2 anteriores)
    b=v #b sera sustituida por el valor de c (1 anterior)
    n+=1 #i se ira incrementando en 1
    if v >= 1000: #si el valor es mayor o igual a 1000
        print("El rango es",n,"y su valor es de",v) #muestro la informacion
        break #como solo se pide que se muestre uno, salgo del bucle
    
        



