# Autor: Luis Fernando Duran Castillo, A01745792
# Descripcion: calcular la distancia entre dos puntos a traves de coordenadas

# Escribe tu programa después de esta línea.

x1= int(input("ponga la coordenada x del primer punto: "))
y1= int(input("ponga la coordenada y del primer punto: "))
x2= int(input("ponga la coordenada x del segundo punto: "))
y2= int(input("ponga la coordenada y del segundo punto: "))

d=(((x2-x1) *(x2-x1)) +((y2-y1) *(y2-y1))) **.5

print("La distancia entre los dos puntos es de: %.3f" % (d))