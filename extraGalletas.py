# Autor: Mariana Teyssier Cervantes
# Descripcion. Saber la cantidad de ingredientes que se necesita para hacer galletas.

galletas = int(input("Teclea el numero de galletas qu quieres hacer: "))

azucar = (galletas * 1.5)/(48)
mantequilla = (galletas * 1.0)/(48)
harina = (galletas * 2.75)/(48)

print "Cantidad de azucar: ", azucar, "tazas"
print "Cantidad de mantequilla: ", mantequilla, "tazas"
print "Cantidad de harina: ", harina, "tazas"

