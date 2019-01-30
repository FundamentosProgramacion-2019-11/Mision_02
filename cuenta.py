# Autor: YadiraFuentesCalderón, A01745235
# Descripcion: Calcular el costo total de una cuenta de comida.

# Escribe tu programa después de esta línea.

subtotal = int (input("¿Cual fue el costo de tu comida?"))

propina =  subtotal*.13
IVA = subtotal*.16

total = subtotal+propina+IVA

print ("Costo de su comida: $ %.2f"%subtotal)
print ("Propina: $ %.2f"%propina)
print ("IVA: $ %.2f"%IVA)
print ("Total a pagar: $ %.2f"%total)