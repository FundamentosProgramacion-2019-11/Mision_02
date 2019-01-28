# Autor: DanielaEstrella, a01745753
# Descripcion: Dado el costo de la comida se calculará el iva, la propina y el costo total a pagar.

# Escribe tu programa después de esta línea.

costo= int(input("Ingresa el costo de la comida: $"))

propina= costo*0.13
iva= costo*0.16
total= costo+ propina+iva

print("Subtotal: $", costo)
print("Propina: $", propina)
print("IVA: $", iva)
print("Total a pagar: $", total)
