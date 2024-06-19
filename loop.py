import os
os.system('cls' if os.name == 'nt' else 'clear')

#clico for
# for i in range(10):
#     print(i)

#ciclo for (inicio, fin, incremento)
# for i in range(2, 20, 2):
#     print(i)

# ciclo for con listas
# lista = ["uno", "dos", "tres", "cuatro", "cinco"]
# for item in lista:
#     print(item)

#ciclo for con tuplas
# tupla = ("uno", "dos", "tres", "cuatro", "cinco")
# for item in tupla:
#     print(item)

#ciclo for con diccionarios
diccionario = {
    "curso": "Python TOTAL",
    "clase": "Ciclos",
    "tema": "for",
    "duracion": "1 trimestre",
    "profesor": "Luis Teruel"
}
for llave in diccionario:
    print(llave, ": ", diccionario[llave])