# Autor: Cecilia Daniela Olivares Hernández, a01745727
# Descripcion: Calculo de la distancia de dos puntos mediante sus coordenadas.

# Escribe tu programa después de esta línea.

x1 = int(input("Escribe la cordenada en x del primer punto: "))

y1 = int(input("Escribe la cordenada en y del primer punto: "))

x2 = int(input("Escribe la cordenada en x del segundo punto: "))

y2 = int(input("Escribe la cordenada en y del segundo punto: "))

d = ((x2 - x1)**2 + (y2 - y1)**2)

sqrt = d**(1/2.0)

print("La distancia total entre los dos puntos es: " '%.3f' % sqrt)