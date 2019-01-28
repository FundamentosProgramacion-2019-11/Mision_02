# Autor: Daniela Estrella, A017457543
# Descripción:Se calculará la distancia entre dos puntos dadas sus coordenadas en los ejes de X y Y.

# Empieza a escribir tu código a partir de esta línea.

x1= int(input("Teclea la coordenada en x del Primer Punto:"))
y1= int(input("Teclea la coordenada en y del Primer Punto:"))

x2= int(input("Teclea la coordenada en x del Segundo Punto: "))
y2= int(input("Teclea la coordenada en y del Segundo Punto:"))

distancia=((x2-x1)**2 + (y2-y1)**2)**0.5

print("La distancia entre los dos puntos es de", distancia)
