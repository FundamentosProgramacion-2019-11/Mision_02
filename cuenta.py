# Autor: Cesar Guzman Guadarrama, A01748918
# Descripcion: Este programa calcula el porcentaje de la propina, el IVA y el costo total de la comida.


com = float(input("Cual es el costo total de la comida?"))
prop = round(com * .13,2)
print("Propina: $", prop,)
iva = round(com * .16,2)
print("IVA: $",iva)
total = com + prop + iva
print("Total a pagar: $",total)