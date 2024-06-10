import os
os.system('cls' if os.name == 'nt' else 'clear')

#booleanos

#mibool = True

#comparaciones
#a = 6 > 5
#b = 30 == 15*3

#print(not(mibool == a and mibool == b))

edad = int(input("Ingresa tu edad: "))

if edad >= 21:
    print("Eres mayor de edad")
elif edad >= 18:
    print("Eres ciudadano")
else:
   print("Eres menor de edad")