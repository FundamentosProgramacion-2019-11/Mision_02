# Autor: Rosalía Serrano Herrera, A01374781
# Descripcion: Calcula el total del precio de una comida agregando el IVA y la propina.

# Escribe tu programa después de esta línea.
cuenta = int(input("Ingresa el costo de la comida: "))
propina = cuenta*13/100
iva = cuenta*16/100
total = cuenta + propina + iva
print("Propina: $ %.2f" % (propina))
print("IVA: $ %.2f" % (iva))
print("El total a pagar es: $ %.2f" % (total))