# Autor: Sofía Daniela Méndez Sandoval, A01242259
# Descripcion: Calcula costo total de una comida incluyendo propina e IVA.

subtotal = int(input("Teclea el costo total de tu comida: "))
propina = subtotal*.13
IVA = subtotal*.16
Total = subtotal+propina+IVA

print(("Subtotal: $"), "%.2f" % subtotal)
print(("Propina: $"), "%.2f" % propina)
print(("IVA: $"), "%.2f" % IVA)
print(("Total: $"), Total)
