# Autor: Maria Angelica Hernandez Parada, A01169796
# Descripcion: Calcular distancia y tiempo de acuerdo a la velocidad

# Escribe tu programa después de esta línea.

velocidad = int(input("Velocidad del auto en km/h: "))

tiempo1 = 6
tiempo2 = 3.5
distancia = 485

distancia1 = (tiempo1*velocidad)
distancia2 = (tiempo2*velocidad)
tiempo = (distancia/velocidad)

print ("Distancia recorrida en 6hrs: " , distancia1 , "km")
print ("Distancia recorrida en 3.5hrs: " , distancia2 , "km")
print ("Tiempo para recorrer 485 km: " , tiempo , "hrs.")
