#Autor: Sara Delgado G.
#Descripción: Calcula velocidad, tiempo y distancia

v = int(input("Velocidad del carro en (km/h): "))
t1 = 6
t2 = 3.5
d = 485
d1= t1*v
d2= t2*v
t= d/v

print("Distancia recorrida en 6 hrs:  %.1f" % d1, "km")
print("Distancia recorrida en 3.5 hrs: %.1f "% d2, "km")
print("Tiempo necesario para recorrer 485 km %.1f: "% t, "hrs.")
