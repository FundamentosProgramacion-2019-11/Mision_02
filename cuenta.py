# Autor: María Fernanda García Gastélum, A01376181
# Descripcion: Problema del total de la cuenta de una comida

# Escribe tu programa después de esta línea.

subtotal= float(input("Escribe total de tu cuenta: "))
propina=(subtotal*0.13)
iva= (subtotal*0.16)
totalAPagar= subtotal + propina + iva

print("Subtotal= $ %.2f" % (subtotal))
print("Propina= $ %.2f" % (propina))
print("IVA= $ %.2f" % (iva))
print("Total a pagar= $ %.2f" % (totalAPagar))

