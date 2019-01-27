#Autor: Guillermo De Anda Casas , A01375892
#Código que calcula la distancia entre dos puntos, dadas sus coordenadas.

x1 = int(input("Escribe el valor de x1: "))
y1 = int(input("Escribe el valor de y1: "))

x2 = int(input("Escribe el valor de x2: "))
y2 = int(input("Escribe el valor de y2: "))

d = (((x2-x1)**2) + ((y2-y1)**2))**0.5

print("Distancia: ","{:.3f}".format(d))