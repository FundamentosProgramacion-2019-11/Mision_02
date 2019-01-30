# Autor: Alan Giovanni Rodriguez Camacho A01748185
# Descripcion: Programa para calcula la distancia y el tiempo de un recorrido de un auto

# Escribe tu programa después de esta línea.

vel=int(input("Indica la velocidad a la que va un auto: "))
disSeis="%.1f"%(vel*6)
disTres="%.1f"%(vel*3.5)
tiempo="%.1f"%(485/vel)

print("Velocidad del auto en km/h: {0}\nDistancia recorrida en 6 hrs: {1} km\nDistancia recorrida en 3.5 hrs: {2} km\nTiempo para recorrer 485 km: {3} hrs.".format(vel,disSeis,disTres,tiempo))

