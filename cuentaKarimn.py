# Autor: Karimn Daniel Hernández Castorena
# Descripcion: Programa que calcula el costo total, la propina y el iva de una cuenta de comida.

# Escribe tu programa después de esta línea.
print()
c = int (input("¿Cuál fue el costo de su comida? "))
print()
p = c * .13
i = c * .16
t = c + p + i
print("El subtotal es de: $%.2f " % (c))
print("La propina es de: $%.2f " % (p))
print("El IVA es de: $%.2f " % (i))
print("El total a pagar es de: $%.2f " % (t))
