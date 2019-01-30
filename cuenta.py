# Autor: Yasmín Landaverde Nava, A01745725
# Descripcion: Este programa calcula el costo total de la comida incluyendo la propina e iva.

stotal = int(input("¿Cuánto fue el total de su cuenta?: "))
prop = stotal*.13
iva = stotal*.16
print("Costo de su comida: $", "%.2f" % stotal)
print("Propina: $", "%.2f" % prop)
print("IVA:", "%.2f" % iva)
ct = stotal + prop + iva
print("Costo total: $", ct)