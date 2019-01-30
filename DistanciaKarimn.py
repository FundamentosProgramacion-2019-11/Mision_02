# Autor: Karimn Daniel Hernández Castorena
# Descripcion: Programa que calcula la distancia entre dos puntos.

# Escribe tu programa después de esta línea.
print()
x1 = int(input("Escribe la coordenada x1: "))
y1 = int(input("Escribe la coordenada y1: "))
x2 = int(input("Escribe la coordenada x2: "))
y2 = int(input("Escribe la coordenada y2: "))
d = ((((x2-x1) **2) + ((y2-y1) **2)) **.5)
print()
print("La distancia es: %.3f" % (d))