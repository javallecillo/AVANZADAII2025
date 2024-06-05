import os
os.system('cls' if os.name == 'nt' else 'clear')

texto = input("Ingresa un texto cualquiera: ").lower()

letra1 = input("Ingresa una primera letra a buscar y contar en el texto: ").lower()
letra2 = input("Ingresa una segunda letra a buscar y contar en el texto: ").lower()
letra3 = input("Ingresa una tercera letra a buscar y contar en el texto: ").lower()

num1 = texto.count(letra1)
num2 = texto.count(letra2)
num3 = texto.count(letra3)

print("La letra " + letra1 + " aparece " + str(num1) + " veces.")
print("La letra " + letra2 + " aparece " + str(num2) + " veces.")
print("La letra " + letra3 + " aparece " + str(num3) + " veces.")