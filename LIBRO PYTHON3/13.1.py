#Write an if statement to determine whether a variable holding a year is a leap year.
#(See the Numbers chapter exercises for the rules for leap years).
year=int(2019)
if year % 4 == 0:
    print (year,"es un año bisiesto")
elif year % 100 == 0:
    if year % 400 == 0:
        print(year,"es un año bisiesto")
else:
    print(year,"No es un año bisiesto")
pass

