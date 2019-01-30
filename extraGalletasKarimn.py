# Autor: Karimn Daniel Hernández Castorena A01379038
# Descripcion: Programa que ayuda a saber cuantas tazas de azucar, mantequilla y harina se necesitan para hornear galletas

# Escribe tu programa después de esta línea
print()
g = int(input("¿Cuántas galletas se van a hornear? "))
print()
a = (g * 1.5)/48
m = (g * 1)/48
h = (g*2.75)/48

print("Se necesitan", (a), "tazas de azucar")
print("Se necesitan", (m), "tazas de mantequilla")
print("Se necesitan", (h), "tazas de harina")