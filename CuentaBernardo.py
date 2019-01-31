# Autor: Bernardo Mondragon Ramirez, A01022325
# Descripcion: Clacular el costo total (con IVA y propina)
#
# Escribe tu programa después de esta línea

comida = int(input("costo de comida: "))

propina = .13*comida

iva = .16*comida

total= comida + propina + iva

print("Comida: $ %.2f" % (comida))

print("Propina: $ %.2f" % (propina))

print("Iva: $ %.2f" % (iva))

print("Total de la cuenta: $ %.2f" % (total))