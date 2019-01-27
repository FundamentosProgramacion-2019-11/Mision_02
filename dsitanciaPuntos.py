# Autor: Bruno Omar Jiménez Mancilla A01748931
# Descripcion: Un programa que calcula la distancia entre dos puntos

# Escribe tu programa después de esta línea.
import math
x1=float(input("Ingrese x1: "))
y1=float(input("Ingrese y1: "))
x2=float(input("Ingrese x2: "))
y2=float(input("Ingrese y2: "))

d=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print("distancia: ",round(d,3),)