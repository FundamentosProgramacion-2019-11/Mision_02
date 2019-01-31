# Autor: Sofía Daniela Méndez Sandoval, A01242259
# Descripción: Calcula la velocidad

velocidad = int(input("¿A cuántos km/h viaja el auto? (en números enteros): "))

tiempo = 6
tiempo2 = 3.5
distancia = 485

d = velocidad*tiempo
d2 = velocidad*tiempo2
t = distancia/velocidad

print("Velocidad del auto: ")
print("Distancia recorrida en 6 horas: ", "%.1f" % d, "km")
print("Distancia recorrida en 3.5 hotas: ", "%.1f" % d2, "km")
print("Tiempo para recorrer 485km: ", "%.1f" % t, "hrs")
