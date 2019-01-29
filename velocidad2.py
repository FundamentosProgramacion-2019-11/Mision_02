
#Autor: Daniela Estrella, A01745753
# Descripcion: El siguiente algoritmo, dada la velocidad, calculará la distancia que recorrerá un auto en
# dos lapsos de tiempo y el tiempo que tardará en recorrer cierta distancia.

# Escribe tu programa después de esta línea.
velocidad= int(input("Ingresa la velocidad en Km/h : "))

distancia01= velocidad*6
distancia02 = velocidad*3.5
horas= 485/velocidad


print("La distancia que recorrerá en 6 horas son %.1f"% (distancia01), "km")

print("La distancia que recorrerá en 3.5 horas %.1f" %(distancia02),"km")

print("Para recorrer 485 km tardaría%.1f " %(horas),"horas")