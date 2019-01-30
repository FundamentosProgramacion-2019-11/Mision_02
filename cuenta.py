# Autor: Mario Hernández Cárdenas, A01375869
# Descripcion: Calcular la propina, el IVA, y el total a pagar de una cuenta de comida.

# Escribe tu programa después de esta línea.

comida = int(input("Escriba el total de la comida en pesos completos: "))
subtotal = comida
propina = comida * .13
IVA = comida * .16
Total = comida + propina + IVA

print("El subtotal de su cuenta es:$%.2f"%subtotal)
print("La propina de su cuenta es: $%.2f"%propina)
print("El IVA de su cuenta es: $%.2f"%IVA)
print("El total de su cuenta es: $%.2f"%Total)
