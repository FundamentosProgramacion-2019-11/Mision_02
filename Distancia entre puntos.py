# Autor: Luis Alberto Zepeda Hernandez, A01328616
# Descripcion: calcular  la distancia entre dos puntos

# Escribe tu programa después de esta línea.

x1 = int(input("Ingresa x1: "))
y1 = int(input("Ingresa y2: "))
x2 = int(input("Ingresa x2: "))
y2 = int(input("Ingresa y2: "))

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5

print("Distancia: ", "{0:.3f}".format(distancia))


