# Autor: Mariana Teyssier Cervantes
# Descripcion: Obtener el total de la cuenta, junto con la propina y el IVA.

# Escribe tu programa despues de esta linea.

subtotal = int(input("Teclea el costo total de su comida: "))

propina = subtotal*.13
IVA = subtotal*.16
total = subtotal + propina + IVA

print "Costo de su comida: ", format(subtotal, ".2f")
print "Propina: ", format(propina, ".2f")
print "IVA: ", format(IVA, ".2f")
print "Total: ", format(total, ".2f")


