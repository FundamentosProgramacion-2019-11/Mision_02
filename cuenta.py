# Autor: Katia Hernández Barrera
# Descripcion: Programa nqu calcula el total de la cuenta tomando en cuenta IVA y propina

# Escribe tu programa después de esta línea.
Sub = int (input("inserte el costo de la comida"))

print ("costo de su comida", Sub)

P = (Sub * 0.13)

print ("Propina", P)

I = (Sub * 0.16)

print ("IVA", I)

Total = Sub + P + I

print ("Total a pagar", Total)
