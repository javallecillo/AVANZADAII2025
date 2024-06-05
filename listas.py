import os
os.system('cls' if os.name == 'nt' else 'clear')

#listas

lista_1 = ["C", "C++", "Python", "Java"]
lista_2 = ["PHP", "SQL", "Visual Basic"]
lista_12 = lista_1 + lista_2

lista_3 = ["d", "a", "c", "b", "e"]
lista_4 = [5, 4, 7, 1, 9]

#concatenar listas
lista_13 = lista_1 + lista_3
lista_14 = lista_1 + lista_4

lista_5 = [True, False, False, True]
lista_145 = lista_1 + lista_4 + lista_5

print("Elemento cero de la lista_1: \n", lista_1[0])
print("\nElemento cero de la lista_2: \n", lista_2[0])

print("\nLista numero 1: \n", lista_1)
print("\nLista numero 2: \n", lista_2)
print("\nLista numero 3: \n", lista_3)
print("\nLista numero 4: \n", lista_4)
print("\nLista numero 5: \n", lista_5)

print("\nLista 12: \n", lista_12)

print("\nLista 13: \n", lista_13)

print("\nLista 14: \n", lista_14)

print("\nLista 145: \n", lista_145)

#agregar elementos a una lista
lista_5.append(True)

print("\nLista numero 5: \n", lista_5)

#remover elementos de una lista
lista_5.pop(2)
print("\nLista numero 5: \n", lista_5)

#ordenar elementos
lista_5.sort()
print("\nLista numero 5: \n", lista_5)

#invertir elementos
lista_5.reverse()
print("\nLista numero 5: \n", lista_5)