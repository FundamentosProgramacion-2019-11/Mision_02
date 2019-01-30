# Autor: Mariana Coria Rodríguez, A01374765
# Descripcion: Distancia entre puntos

# Escribe tu programa después de esta línea.
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**.5
print("Distancia: %.3f" % (distancia))
