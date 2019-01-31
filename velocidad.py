# Autor: Roberto Castro Barrios, A01748559
# Descripcion: Programa que mide el tiempo de un viaje dependiendo de la velocidad y calcula cierto tiempo a recorrer.

# Escribe tu programa después de esta línea.
v= int(input("Ingresa la velocidad en Km/h: "))

d1= v*6
d2= v*3.5
trecorrer= 485/v

print("La velocidad es: ", v, " Km/h")
print("La distancia recorrida en 6 horas es de: ", d1, " Km/h")
print("La distancia recorrida en 3.5 horas es de: %.1f Km/h"%(d2))
print("El tiempo para recorrer 485 km es de: %.1f hrs"%(trecorrer))

