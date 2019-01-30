# Autor: María Fernanda García Gastélum, A01376181
# Descripcion: Calcular v=d/t

# Escribe tu programa después de esta línea.
v= int(input("Velocidad del auto en km/hr: "))
d1= v*6
d2= v*3.5
t= 485/v

print("Velocidad del auto en km/hr: ", v)
print("Distancia recorrida en 6 hrs: %.1f " % d1, "km")
print("Distancia recorrida en 3.5 hrs: %.1f " % d2, "km")
print("Tiempo para recorrer 485 km: %.1f " % t, "hrs")
