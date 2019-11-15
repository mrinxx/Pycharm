#Crear un programa	para jugar a adivinar un número entre 0	y 100. Debe	ofrecer	cinco oportunidades e indicar	
#ante un fallo si el objetivo es menor,	mayor o	esta muy cerca (a 2 de distancia o	menos). Se debe	utilizar una	
#función para comprobar	si el número es	el	acertado o no y	hacer las indicaciones	al	jugador

def aleatorio ():
    import random #importamos libreria
    na=random.randint(0, 101) #el numero elegido estara entre 0 y 100 aleatorio

    oportunidades=5 #defino el numero de oportunidades limite
    while oportunidades !=0: #mientras que las oportunidades no se hayan acabado
        n=int(input("Introduce un numero: ")) #voy pidiendo numeros
        if n == na: #si el numero es igual al aleatorio
            s=print("CORRECTO, HAS ACERTADO!!!") #es correcto
            break #termino el programa
        else: #si no es correcto
            oportunidades-=1 #quito una oportunidad
            if n>na: #si es mayor
                s=print("EL NUMERO QUE HAS INTRODUCIDO ES MAYOR QUE LA SOLUCION,QUEDAN",oportunidades,"OPORTUNIDADES!!!")
            elif n<na:#si es menor
                s=print ("EL NUMERO QUE HAS INTRODUCIDO ES MENOR QUE LA SOLUCION",oportunidades,"OPORTUNIDADES!!!") 
            elif na-n==2 or na-n==1: #si esta a 2 o 1 numero de la solucion
                s=print("ESTAS CERCA, A 2 O MENOS NUMEROS DE LA SOLUCION!!!",oportunidades,"OPORTUNIDADES!!!")
        if oportunidades==0: #si las oportunidades llegan a 0 
            f=print("HAS PERDIDO, LA SOLUCION ERA",na) #muestro la solucion correcta
            return f #devuelvo 
    
    return s #siempre devolvere s

if __name__ == "__main__": #en el bloque principal
    aleatorio() #llamo a la funcion para que se ejecute
