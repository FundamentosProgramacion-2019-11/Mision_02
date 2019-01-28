# Autor: Juan Carlos Flores García, A01376511
# Descripcion: Programa que calcula la distancia y el tiempo que recorrió un auto.

# Escribe tu programa después de esta línea.
v = int(input("Teclea la velocidad del auto en k/m, v: "))

distancia1 = v*6

distancia2 = v*3.5

tiempo1 = 485/v

print("Velocidad del auto en k/m: %.1f" % v)
print("Distancia recorrida en 6 horas: %.1f" % distancia1)
print("Distancia recorrida en 3.5 horas: %.1f" % distancia2)
print("Tiempo para recorrer 485km: %.1f" % tiempo1)
