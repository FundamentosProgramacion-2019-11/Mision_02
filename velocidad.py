# Autor: Roberto Emmanuel González Muñoz A01376803
# La velocidad de un auto puede calcularse con la fórmula v = d/t.
# Elabora un algoritmo y escribe un programa que pregunte al usuario
# la velocidad a la que viaja un auto (km/h, número entero) y calcule el tiempo.

def imprimir(d1,d2,t):
    print("___________________________________________________________________________")
    print("Distancia recorrida en 6 horas: %.1f" % d1)
    print("___________________________________________________________________________")
    print("Distancia recorrida en 3.5 horas: %.1f" % d2)
    print("___________________________________________________________________________")
    print("Tiempo para recorrer 485 km: %.1f" % t)
    print("___________________________________________________________________________")


def main():
    velocidad = float(input("Velocidad del auto en km/h: "))
    distancia1 = velocidad * 6
    distancia2 = velocidad * 3.5
    tiempo = 485 / velocidad

    imprimir(distancia1, distancia2, tiempo)



main()