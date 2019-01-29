# Autor: Cesar Guzman Guadarrama, A01748918
# Descripcion: Este programa te dice la distancia entre 2 puntos

from math import sqrt

x1 = float(input("Cual es el valor de x1"))
y1 = float(input("Caul es el valor de y1"))

x2 = float(input("Cual es el valor de x2"))
y2 = float(input("Cual es el valor de y2"))

d = round(sqrt((x2-x1)**2 + (y2-y1)**2),3)
print("La distancia es de ",d,)

