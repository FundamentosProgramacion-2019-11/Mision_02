# Autor: Mariana Coria Rodríguez, A01374765
# Descripcion: Total a pagar

# Escribe tu programa después de esta línea.
costo = int(input("Costo de su comida: " ))
propina = costo*.13
print("Propina: $ %.2f" % (propina))
iva = costo*.16
print("IVA: $ %.2f" % (iva))
total = costo + propina + iva
print("Total a pagar: $ %.2f" % (total))
