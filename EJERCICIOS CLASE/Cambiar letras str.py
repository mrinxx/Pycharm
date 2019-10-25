s="Marina Ocaña" #meto el nmbre
s=list(s) #hago un parsing y lo convierto a lista
s[1]="x" #cambio el elemento que quiera de la lista 
s="".join(s) #lo vuelvo a convertir a cadena de texto
print (type(s),s)