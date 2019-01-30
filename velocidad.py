# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

v = int(input ("¿A qué velocidad viaja el auto en km/h y enteros?: "))
tiempo = 6
tiempo1 = 3.5
distancia = 485
d = v * tiempo
d1 = v * tiempo1
t = distancia / v

print("Velocidad del auto en km/h")
print("Distancia recorrida en 6 hrs: ", "%.1f" % d, "km")
print("Distancia recorrida en 3.5 hrs: ", "%.1f" % d1, "km")
print("Tiempor para recorrer 485km: ", "%.1f" % t, "km")

