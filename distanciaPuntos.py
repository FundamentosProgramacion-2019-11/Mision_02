# Autor: Roberto Castro Barrios, A01748559
# Descripción: Programa que pregunta al usuario por 4 coordenadas y obtiene la distancia entre esos puntos.

import math as m
x1 = int(input("Ingresa el valor de x1= "))
x2 = int(input("Ingresa el valor de x2= "))
y1 = int(input("Ingresa el valor de y1= "))
y2 = int(input("Ingresa el valor de y2= "))

d= m.sqrt((x2-x1)**2+(y2-y1)**2)

print("La distancia entre los dos puntos es de: %.3f"%(d))
