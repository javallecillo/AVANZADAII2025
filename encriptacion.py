import os

usuario = "admin"
contrasenia = "admin123"
contraseniaInversa = contrasenia[::-1]
acceso = False

usu = input("Ingrese el usuario: ")

if usu == usuario:
    intento = input("Ingresa tu contraseña: ")
    intentoInverso = intento[::-1]

    if intento == contrasenia and intentoInverso == contraseniaInversa and contraseniaInversa[2::2] == intentoInverso[2::2]:
        acceso = True

        #AQUI IRIA EL CODIGO

    else:
        print("Credenciales incorrectas")
else:
    print("Credenciales incorrectas")

# print(acceso)
