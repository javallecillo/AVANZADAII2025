import os
os.system('cls' if os.name == 'nt' else 'clear')

#DICCIONARIOS

alumnos = [
    { "id" : 1, "nombre" : "Jorge Arturo Vallecillo Espinoza", "edad" : 18 },
    { "id" : 2, "nombre" : "Lucas Rodrigo Bautisma Juarez", "edad" : 18 },
    { "id" : 3, "nombre" : "Jose David Mejia Mendoza", "edad" : 31 },
    { "id" : 4, "nombre" : "Kennet Andersson Martinez Varela", "edad" : 21 },
    { "id" : 5, "nombre" : "Tomy Jose Montufar Zuniga", "edad" : 19 },
    { "id" : 6, "nombre" : "Angel Antonio Perez Rodriguez", "edad" : 18 },
    { "id" : 7, "nombre" : "Jose Eduardo Sabillon Hurtado", "edad" : 19 },
    { "id" : 8, "nombre" : "Diany Lizbeth Enamoradi Fernandez", "edad" : 19 },
    { "id" : 9, "nombre" : "Anderson Jair Garcia Menjivar", "edad" : 19 },
    { "id" : 10, "nombre" : "Iliana Liceth Zuniga Enamorado", "edad" : 18 },
    { "id" : 11, "nombre" : "Derick Dair Muñoz Iraheta", "edad" : 20 },
    { "id" : 12, "nombre" : "Norman Bu", "edad" : 25 },
    { "id" : 13, "nombre" : "Walter Eduardo Rapalo Smith", "edad" : 20 },
    { "id" : 14, "nombre" : "Edson Jhair Rios Coto", "edad" : 26 },
]

#for valores in alumnos:
#   print(valores)

for valores in alumnos:
    print(valores["id"], " - ", valores["nombre"], " - ", valores["edad"])
