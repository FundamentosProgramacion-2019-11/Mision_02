# Autor: Karimn Daniel Hernández Castorena A01379038
# Descripcion: Programa que ayuda a conocer la distancia y el tiempo de un auto.

# Escribe tu programa después de esta línea
print()
v = int(input("¿Qué velocidad tiene el carro? "))
d1 = (v * 6)
d2 = (v * 3.5)
t1 = (485 / v)
print()
print("La distancia recorrida en 6 horas es %.1f" % (d1), "km.")
print("La distancia recorrida en 3.5 horas es %.1f" % (d2), "km.")
print("El tiempo que tarda en recorrer 485 km es %.1f" % (t1), "hrs.")
