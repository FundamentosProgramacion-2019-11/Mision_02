# Autor: Diego Raul Elizalde Uriarte, a01748756
# Descripcion: Calcula la distancia entre dos puntos.

#Lecturas
import math as m
x1 = int(input("Dame la coordenada de x1 del primer punto: "))
y1 = int(input("Dame la coordenada de y1 del primer punto: "))
x2 = int(input("Dame la coordenada de x2 del segundo punto: "))
y2 = int(input("Dame la coordenada de y2 del segundo punto: "))

#Calculo de resultados
d = m.sqrt(((x2-x1)**2)+((y2-y1)**2))

#Imprimir resultados
print("x1: ",x1)
print("y1: ",y1)
print("x2: ",x2)
print("y2: ",y2)
print("Distancia: %.3f"%(d))