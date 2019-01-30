# Autor: Mariana Teyssier Cervantes
# Descripcion. Calcular la distancia entre dos puntos.

x1 = int(input("Teclea la coordenada x1: "))
y1 = int(input("Teclea la coordenada y1: "))
x2 = int(input("Teclea la coordenada x2: "))
y2 = int(input("Teclea la coordenada y2: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** (0.5)

print "La distancia entre los dos puntos es: ", format(distancia, ".3f")
