# Autor: Rosalía Serrano Herrera, A01374781
# Descripcion: Calcula la distancia entre dos puntos

x1 = int(input("Ingresa la coordenada x1: "))
y1 = int(input("Ingresa la coordenada y1: "))
x2 = int(input("Ingresa la coordenada x2: "))
y2 = int(input("Ingresa la coordenada y2: "))
d =((x2-x1)**2+(y2-y1)**2)**.5
print("La distancia entre los puntos es: %.3f" % (d))