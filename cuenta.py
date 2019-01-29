# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.
---------------------------------------------------------------------------------------
# Autor: Santiago España Vázquez, A01748311
# Descripcion: Datos de pago de una cuenta de restaurante

#Entradas
totalPrice=float(input("Por favor introduzca el precio por la comida: "))

#
print("El subtotal es: ", totalPrice)
print("La propina es: ", totalPrice *.13)
print("El IVA es: ", totalPrice *.16)
print("El total a pagar es de: ", totalPrice + (totalPrice *.13) + (totalPrice *.16))
