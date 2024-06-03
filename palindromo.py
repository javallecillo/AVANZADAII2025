import os
os.system('cls' if os.name == 'nt' else 'clear')

palabra = input("Ingrese una palabra para saber si es una palabra palindroma: ").lower()

reves = palabra[::-1]

if palabra == reves :
    print("La palabra es un palindromo.")
else:
    print("La palabra no es un palindromo")