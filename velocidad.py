# Autor: Mario Hernández Cárdenas, A01375869
# Descripcion: Calcular los kilometros que se recorrerán despues de 6 y 3.5 horas, y el tiempo para recorrer 485 km

# Escribe tu programa después de esta línea.

velocidad = int(input("Introduce la velocidad del auto en km/h enteros: "))

seis = velocidad*6
tresy = velocidad*3.5
distancia = 485/velocidad

print("Después de 6 horas recorrerás %.1f"%seis, "kilometros.")
print("Después de 3.5 horas recorrerás %.1f"%tresy, "kilometros.")
print("Tardarás %.1f"%distancia, "horas en recorrer 485 kilometros.")

