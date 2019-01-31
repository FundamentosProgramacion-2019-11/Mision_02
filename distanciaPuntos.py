#Víctor Iván Morales Ramos a01377601
#analisis: Crear un algoritmo que calcule la distancia de dos puntos (x1, y1 y x2, y2).

import math

x1 = float(input("Dame la coordenada x1: "))
y1 = float(input("Dame la coordenada y1: "))
x2 = float(input("Dame la coordenada x2: "))
y2 = float(input("Dame la coordenada y2: "))

d = math.sqrt(((x2 - x1)**2)+((y2 - y1)**2))

print("La distancia entre ambos puntos es: %.3f"%(d))
