# Autor: Alan Giovanni Rodriguez Camacho A01748185
# Descripcion: Calcular la cuenta total en un restaurante.

# Escribe tu programa después de esta línea.

subtotal=int(input("¿Cual fue el costo de tu comida?: "))
propina=float(subtotal*.13)
iva=float(subtotal*.16)
total=float(subtotal+propina+iva)

print("Costo de su comida: %.02f $"%(subtotal))
print("Propina: %.02f $"%(propina))
print("Iva: %.02f $"%(iva))
print("Total a pagar: %.02f $"%(total))



