#OPERACIONES ARITMETICAS

import os
os.system('cls' if os.name == 'nt' else 'clear')

#usuario ingresa los datos de tipo float
x = float(input("Ingresa el primer numero: "))
y = float(input("Ingresa el segundo numero: "))

print("Suma: ", x+y)
print("Resta: ", x-y)
print("Multiplicacion:", x*y)

if y == 0:
    print("No se puede dividir entre cero.")
else:
    print("Division: ", x/y)