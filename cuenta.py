# Autor: Elizabeth Citlalli Zapata Cortes, A01746002
# Descripcion: Calcula el costo total de una comida en un restaurante, inluyendo propina e IVA.

# Escribe tu programa después de esta línea.

#Entradas
costo = int(input("Costo de su comida: "))

#Calcular
propina = costo * 0.13
iva = costo * 0.16
total = costo + propina + iva

#Imprimir
print("Costo de su comida: $ %.2f" % (costo))
print("Propina: $ %.2f" % (propina))
print("IVA: $ $ %.2f" % (iva))
print("Total a pagar: $ $ %.2f" % (total))
