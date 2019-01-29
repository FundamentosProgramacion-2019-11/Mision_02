# Autor: Cecilia Daniela Olivares Hernández, a01745727
# Descripcion: Calculo de el costo total de una comida en un restaurante.

# Escribe tu programa después de esta línea.

subtotal = int(input("Inserta el costo de la comida: "))

propina = .13*subtotal

IVA = .16*subtotal

total = subtotal + propina + IVA

print("Costo de la comida: $" '%.2f' % subtotal)

print("Propina: $"'%.2f' % propina)

print("IVA: $"'%.2f' % IVA)

print("El total a pagar es: $" '%.2f' % total)



