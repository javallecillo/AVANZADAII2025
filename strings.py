import os
os.system('cls' if os.name == 'nt' else 'clear')

# saludo  = "Hola_mundo"

# try:
#     print(saludo.index('o', 4, 7))
# except ValueError:
#     print("No se encontro la subcadena")

# #rindex() devuelve la posicion de la ultima ocurrencia de una subcadena
# print(saludo.rindex('o'))

# print(saludo[4:8])

# cedula = "1622200500339"
# departamento = cedula[0:2]
# print(departamento)
# municipio = cedula[0:4]

# #islower() verifica si una cadena es minuscula
# print("hola".islower())

# #isupper() verifica si una cadena es mayuscula
# print("HOLA".isupper())

# print(saludo[2:6])

# print(saludo[3::3])

# print(saludo[2::2])

# print(saludo.count("o"))

# mensaje = "hola12345"
# mensaje2 = "holamundo"
# numero = "12345"
# decimales = "12345.555"

# print(mensaje.isdigit())
# print(numero.isdigit())
# print(decimales.isdigit())
# print("\n")

# print(mensaje.isnumeric())
# print(numero.isnumeric())
# print(decimales.isnumeric())
# print("\n")

# print(mensaje.isdecimal())
# print(numero.isdecimal())
# print(decimales.isdecimal())
# print("\n")

# print(mensaje.isalnum())
# print(mensaje2.isalnum())
# print("\n")

# mensaje3 = mensaje2.replace("hola", "hello ")

# print(mensaje3)

mensahe = "adios mundo cruel"
print(mensahe.split(" "))

nombre = "Jorge*Arturo*Vallecillo*Espinoza"
print(nombre.split("*"))
print(nombre.count("*"))
print(nombre.replace("*", " "))
