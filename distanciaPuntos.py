#Autor: María Fernanda García Gastélum, A01376181
# Calcular distancia entre dos coordenadas

#
x1= int(input("Escribir valor de x1: "))
y1= int(input("Escribir valor de y1: "))
x2= int(input("Escribir valor de x2: "))
y2= int(input("Escribir valor de y2: "))

distancia= ((x2-x1)**2 + (y2-y1)**2)**0.5

print("Distancia= %.3f" % (distancia))
