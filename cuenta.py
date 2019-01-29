# Autor: Maria Angelica Hernandez Parada, A01169796
# Descripcion: Cuenta total con subtotal, propina e IVA

# Escribe tu programa después de esta línea.

subtotal = int(input("Costo de su comida: "))

propina = .13
IVA = .16

propina1 = (subtotal*propina)
IVA1 = (subtotal*IVA)
total = (subtotal+propina1 + IVA1)

print ("Propina: $  %.2f" % (propina1))
print ("IVA: $ %.2f" % (IVA1))
print ("Total a pagar: $ %.2f" % (total))