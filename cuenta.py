# Autor: Roberto Castro Barrios, A01748559
# Descripcion: Programa que respecto a tu subtotal de cuenta, calcula IVA y propina para obtener el total.

# Escribe tu programa después de esta línea.
cuenta = float(input("Ingresa el subtotal de tu cuenta: "))

prop = cuenta*0.13
iva = cuenta*0.16
total = cuenta+prop+iva

print("El subtotal de tu cuenta es: $", cuenta)
print("La propina es de: $%.2f "%(prop))
print("El IVA es de: $%.2f"%(iva))
print("El total de tu cuenta es: $%.2f"%(total))


