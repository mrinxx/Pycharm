#Disena un programa que, dado un caracter cualquiera, lo identifique como vocal minuscula, vocal 
#mayuscula, consonante minuscula, consonante mayUscula u otro tipo de caracter.

c=input("Introduce un caracter: ")

if c in "aeiou":
    print("VOCAL MINUSCULA")
elif c in "AEIOU":
    print("VOCAL MAYUSCULA")
elif c in "bcdfghjklmnñpqrstvwxyz":
    print("CONSONANTE MINUSCULA")
elif c in "BCDFGHJKLMNÑPQRSTVWXYZ":
    print("CONSONANTE MAYUSCULA")
else:
    print("OTRO CARACTER")