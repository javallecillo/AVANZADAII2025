#tuplas

import os
os.system('cls' if os.name == 'nt' else 'clear')

mi_tupla = (1, "dos", [3.33, "cuatro", "equis"], (5.0, 6))

print(mi_tupla)
print(mi_tupla[0])
print(mi_tupla[3][1])
print(mi_tupla[2][2])

lista1 = list(mi_tupla)
print(lista1)

#umpacking de tuplas (desempaquetar tuplas)
a, b, c, d = mi_tupla
print(a)
print(b)
print(c)
print(d)

#tupla de pi e gravedad
tuplaConstante = (3.1416, 9.8, 2.7182)
pi, gravedad, e = tuplaConstante
print(f"pi = {pi}, gravedad = (gravedad), e = (e)")