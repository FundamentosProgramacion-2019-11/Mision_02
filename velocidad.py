# Autor: Elizabeth Citlalli Zapata Cortes, A01746002
# Descripcion: Calcular distancias y tiempo con base en la velocidad del usuraio.

# Escribe tu programa después de esta línea.

# Entradas
velocidad = int(input("Teclear la velocidad en km/hr: "))

#Calcular datos
distancia1 = velocidad * 6

distancia2 = velocidad * 3.5

tiempo = 485 / velocidad

#Imprimir
print("Distancia recorrida en 6 hrs:  %.1f" % (distancia1), "km")
print("Distancia recorrida en 3.5 hrs: %.1f" % (distancia2), "km")
print("Tiempo para recorrer 485 km: %.1f" % (tiempo), "hrs.")
