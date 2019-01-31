# Autor: Sofía Daniela Méndez Sandoval, A01242259
# Descripción: Cantidad de Ingredientes para # de Galletas

cantidad = int(input("¿Cuántas galletas realizará?: "))

azucar = (cantidad*1.5)/48
mantequilla = cantidad/48
harina = (cantidad*2.75)/48

print("Para realizar el determinado número de galletas, necesitará: ")
print("Azúcar: ", "%.2f" % azucar, "tazas")
print("Mantequilla: ", "%.2f" % mantequilla, "tazas")
print("Harina: ", "%.2f" % harina, "tazas")
