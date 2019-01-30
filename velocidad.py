# Autor: Ronaldo Estefano Lira Buendia
# Programa donde calcule la velocidad y tiempo de un automovil

v=int(input("Ingrese la velocidad del auto en km/h: "))

d=v*6
d2=v*3.5
t=485/v

print("Velocidad del auto en km/h: ", v)
print("Distancia recorrida en 6 hrs: {0:.1f}".format(d))
print("Distancia recorrida en 3.5 hrs: {0:.1f}".format(d2))
print("Tiempo para recorrer 485 km: {0:.1f}".format(t))
