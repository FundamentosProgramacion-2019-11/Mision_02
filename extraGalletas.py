# Autor: Cecilia Daniela Olivares Hernández, a01745727
# Descripcion: Calculo de ingredientes que se requieren para elaborar el numero indicado de galletas

# Escribe tu programa después de esta línea.

g= int(input("Inserta la cantidad de galletas que deseas realizar: "))

a = (g * 1.5) / 48

m = (g * 1) / 48

h = (g * 2.75) / 48

print("Tazas de azucar: "'%.1f' % a)

print("Tazas de mantequilla: "'%.1f' % m)

print("Tazas de harina: "'%.1f' % h)



