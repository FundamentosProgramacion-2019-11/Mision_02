# Autor: Ivana Olvera Mérida, A01746744
# Descripcion: Misión 2-Ejercicio 3: Cuenta

# Escribe tu programa después de esta línea.
subtotal = int (input("Subtotal: "))

propina = (subtotal*.13)
iva= (subtotal*.16)
total= (subtotal+propina+iva)

print ("Propina: %.2f" % (propina))
print ("IVA: %.2f" %(iva))
print ("Total a pagar: %.2f" % (total))
