# Autor: Roberto Emmanuel González Muñoz A01376803
# Elabora un algoritmo y escribe un programa que calcula la distancia entre dos puntos.


def main():
    coordenadaX1 = int(input("Introduce la coordenada X1: "))
    coordenadaY1 = int(input("Introduce la coordenada Y1: "))
    coordenadaX2 = int(input("Introduce la coordenada X2: "))
    coordenadaY2 = int(input("Introduce la coordenada Y2: "))

    distanciaEntrePuntos = ((coordenadaX2 - coordenadaX1)**2+(coordenadaY2 - coordenadaY1)**2)**.5
    print("Distancia: %.3f" % distanciaEntrePuntos)
    print("____________________________________")

main()