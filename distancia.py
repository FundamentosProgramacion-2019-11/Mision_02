#Sofía Trujillo Vargas A01747320
#En este problema se dará la distancia entre dos puntos con sus coordenadas.

import math
x1=float(input('Dame tu punto en x del primer punto: '))
y1=float(input('Dame tu punto en y del primer punto: '))
x2=float(input("Dame tu punto en x del segundo punto: "))
y2=float(input("Dame tu punto en y del segundo punto: "))

z=x2-x1
u=y2-y1

d= math.sqrt((z*z)+(u*u))

print("La distancia entre los dos puntos es de: ",round(d,3))