#Realiza un programa que calcule el desglose en billetes y monedas de una cantidad exacta de euros. 
#Hay billetes de 500, 200, 100, 50, 20, 10 y 5  y monedas de 2 y 1 . 

cantidad=float(input("Introduce la cantidad a desglosar: "))

cantidades=[]
leidas=[]


while cantidad != 0:
    if cantidad%500 == 0:
        cantidad-=500
        cantidades.append(500)
    elif cantidad%200 == 0:
        cantidad-=200
        cantidades.append(200)
    elif cantidad%100 == 0:
        cantidad-=100
        cantidades.append(100)
    elif cantidad%50 == 0:
        cantidad-=50
        cantidades.append(50)
    elif cantidad%20== 0:
        cantidad-=20
        cantidades.append(20)
    elif cantidad%10 == 0:
        cantidad-=10
        cantidades.append(10)    
    elif cantidad%5 == 0:
        cantidad-=5
        cantidades.append(5)
    elif cantidad%2 == 0:
        cantidad-=2
        cantidades.append(2)
    elif cantidad%1 == 0:
        cantidad-=1
        cantidades.append(1)
        
print("\nDESGLOSE DE LA CANTIDAD:   ")
for i in cantidades:
    if i not in leidas:
        leidas.append(i)
        cuenta=cantidades.count(i)
        print(cuenta,"billetes de", i)    
        pass
    


