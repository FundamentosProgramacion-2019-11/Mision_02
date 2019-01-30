#Yasmín Landaverde Nava, A01745725
#Descripción:Este programa calcula la distancia entre dos coordenadas

print("Ingrese los valores de la primera cordenada: ")
x = int(input("x1: "))
y = int(input("y1: "))
print("Ingrese los valores de la segunda cordenada:")
xx = int(input("x2: "))
yy = int(input("y2: "))
d = ((xx - x)**2 + (yy - y)**2)**0.5
print("la distancia es: ","%.3f" % d)