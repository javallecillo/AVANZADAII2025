
print("EMPRESA DE COMPUTADORAS")

precio = 100
cantidad = int(input("Ingrese la cantidad de computadoras a comprar: "))
subtotal = precio * cantidad

if cantidad >= 10 and cantidad <= 999:
    print("Aplica para descuento del 20%")
    descuento = subtotal * 0.20
    total = subtotal - descuento
    print("El total de la compra es: ", total)
elif cantidad >= 1000:
    print("Aplica para descuento del 50%")
    descuento = subtotal * 0.50
    total = subtotal - descuento
    print("El total de la compra es: ", total)
else:
    print("El total de la compra es: ", subtotal)
    