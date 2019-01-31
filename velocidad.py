# Autor: Victor Manuel Cerón Navarrete A01374446
# Descripcion: Como sacar la velocidad de un viaje

# Escribe tu programa después de esta línea.

Velocidad = int(input("¿Cuál es la velocidad del auto en km/h? (Escribir en letras y sin espacios) "))
print(Velocidad)

seis = Velocidad * 6
print("Distancia recorrida en 6 horas: %.1f km/h:" % (seis))

tresymedio = Velocidad * 3.5 
print("distancia en 3.5 horas: %.1f km/h" % (tresymedio))

tiempo = 485 / Velocidad
print("Tiempo para recorrer 845 km: %.1f horas" % (tiempo))