# Autor: Mario Hernández Cárdenas, A01375869
# Descripción: Calcular la distancia entre dos puntos.

x1 = int(input("x1= "))
y1 = int(input("y1= "))
x2 = int(input("x2= "))
y2 = int(input("y2= "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print("La distancia entre los dos puntos es: %.3f"%distancia)