import os
os.system('cls' if os.name == 'nt' else 'clear')

numero = int(input("Ingresa un numero: "))

print("Tabla del ", numero)
for i in range(1, 13):
    print(numero, " x ", i, " = ", (numero*i))