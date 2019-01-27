# Autor: Guillermo De Anda Casas, A01375892
# Descripcion: Calcular velocidades y distancia de un auto

# Escribe tu programa después de esta línea.

d = int(input("Inserte la distancia recorrida en km: "))
t = int(input("Inserte el tiempo en horas: "))

v = d/t

d1 = v*6
d2 = v*3.5

t1 = 485/v
t2 = t1*60

print("Velocidad del auto en km/h:","{:.1f}".format(v))
print("Distancia recorrida en 6 hrs: ","{:.1f}".format(d1))
print("Distancia recorrida en 3.5 hrs:","{:.1f}".format(d2))
print("Tiempo para recorrer 485 km:","{:.1f}".format(t1),"horas ,","{:.1f}".format(t2),"minutos")
