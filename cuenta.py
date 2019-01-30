# Autor: Marianela Contreras Domínguez, A01374769
# Descripcion: Problema para calcular la cuenta de restaurante de una comida, con propina e IVA.

# Escribe tu programa después de esta línea.


costo = float(input("Costo de la comida:"))

propina = costo *.13
iva = costo *.16
total = costo + iva + propina

print ("Propina: $ %.2f"% (propina))
print ("IVA: $ %.2f"% (iva))
print ("Total:$ %.2f" % (total))

       


