# Autor: Victor Manuel Cerón Navarrete, A01374446
# Descripcion: Calcula el monto total a pagar en un restaurante

# Escribe tu programa después de esta línea.

cuenta = int(input( "Teclea el monto total de tu comida"))
propina = cuenta*.13
print("Propina: %.2f MXN" % (propina))
iva = cuenta*.16
print("El iva es %.2f MXN" % (iva))

total = cuenta + propina + iva 
print("Tu monto total a pagar es de %.2f MXN " % (total))