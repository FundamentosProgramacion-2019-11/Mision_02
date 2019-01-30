#Autor: Sara Delgado G.
#Descripción: Calcula el costo total de una comida


subtotal = int(input("Costo de la comida: "))
propina = subtotal*0.13
iva = subtotal*0.16
total= subtotal + iva + propina


print("Propina: %.2f" % propina)
print ("IVA: %.2f" % iva)
print("Total: %.2f" % total)