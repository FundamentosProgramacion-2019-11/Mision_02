# Autor: Luis Alberto Zepeda Hernandez, A01328616
# Descripcion: calcular el costo total de una comida en un restaurante, incluyendo el 13% de propina y el 16% de iva

# Escribe tu programa después de esta línea.

comida = int(input("Ingresa costo total de la comida: "))
iva = comida * .16
propina = comida * .13
total = iva + propina + comida

print("Costo total de la comida: ", "$", comida)
print("Propina: ", "$", "{0:.2f}".format(propina))
print("IVA: ", "$", "{0:.2f}".format(iva))
print("Total a pagar: ", "$","{0:.2f}".format(total))

