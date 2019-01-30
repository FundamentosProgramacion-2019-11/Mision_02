# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.
---------------------------------------------------------------------------------------
# Autor: Santiago España Vázquez, A01748311
# Descripcion: Datos de pago de una cuenta de restaurante

#Entradas
totalPrice=float(input("Por favor introduzca el precio por la comida: "))

#Calculos
prop=(totalPrice*.13)
iva=(totalPrice*.16)
full=totalPrice+prop+iva

#Salidas
print("El subtotal es: %.2f" %totalPrice)
print("La propina es: %.2f" %prop)
print("El IVA es: %.2f" %iva)
print("El total a pagar es de: %.2f" %full)
