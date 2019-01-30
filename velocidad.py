# Autor: Aline Paulette Villegas Berdejo, A01375818
# Descripcion: Calcular la distancia y el tiempo que recorre un auto de acuerdo a su velocidad

# Escribe tu programa después de esta línea.
v=int(input("Velocidad del auto en km/h: "))
d=v*6
d2=v*3.5
t=485/v

print("Distancia recorrida en 6 horas: %.1f " % d, "km")
print("Distancia recorrida en 3.5 horas: %.1f " % d2, "km")
print("Tiempo para recorrer 485 km: %.1f " % t, "hrs.")
