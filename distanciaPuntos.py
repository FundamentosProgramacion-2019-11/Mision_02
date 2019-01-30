# Autor: Elizabeth Citlalli Zapata Cortes, A01746002
# Descripcion: Calcular la distancia entre dos puntos.

#Entradas
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

#Calcular
distancia = ((x2 - x1)**2  +  (y2 - y1)**2)**0.5

#Imprimir
print("Distancia: %.3f" % (distancia))