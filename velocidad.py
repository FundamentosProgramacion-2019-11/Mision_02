# Autor: MarianaTeyssierCervantes
# Descripcion: Distancia y tiempo recorrido con cierta velocidad.

# Escribe tu programa despues de esta linea.

velocidad = int(input("Teclea la velocidad de tu viaje en km/h: "))

distancia1 = velocidad*6
distancia2 = velocidad*3.5
tiempo = 485/velocidad

print "Distancia en 6 horas recorridas es:",format(distancia1, ".1f")
print "Distancia recorrida en 3.5 horas es:",format(distancia2, ".1f")
print "El tiempo recorrido en 485 km es:",format(tiempo, ".1f")

