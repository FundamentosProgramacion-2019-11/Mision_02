# Autor: Sofía Daniela Méndez Sandoval, A01242259
# Descripción: Calcula la distancia entre dos puntos

print("Ingresa coordenadas del primer punto: ")
x1 = int(input("x1: "))
y1 = int(input("y1: "))

print("Ingrese las coordenadas del segundo punto: ")
x2 = int(input("x2: "))
y2 = int(input("y2: "))

d = ((x2-x1)**2 + (y2-y1)**2)**0.5

print(("La distancia entre ambas coordenadas es: "), "%.3f" % d)
