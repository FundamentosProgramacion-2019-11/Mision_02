# Autor: Rosalía Serrano Herrera, A01374781
# Descripción: Calcula la distancia y tiempo de un recorrido.

# Escribe tu programa después de esta línea.
v = int(input("Teclea la velocidad en km: "))
d = v*6
d2 = v*3.5
t = 485/v
print("La distancia recorrida en 6 horas es: %.1f" % (d), "km ")
print("La distancia recorrida en 3.5 horas es: %.1f" % (d2), "km ")
print("El tiempo que se requiere para recorrer 485km es: %.1f" % (t), "hrs")