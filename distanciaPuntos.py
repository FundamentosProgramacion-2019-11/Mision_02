# Jose Luis Mata Lomelí
# A01377205
# Programa que calcule la distancia que existe dentro de dos puntos (x, y)

# Entrada = Coordenas (x, y)
x1= int(input("x1 : "))
y1= int(input("y1: "))
x2= int(input("x2: "))
y2= int(input("y2: "))

# E/S = Calcular la distancia
distancia_formula = float((x2-x1)**2 + (y2-y1)**2)**.5

# Salida = Resultado del calculo
print("La distancia entre los dos puntos es: %.3f" % distancia_formula)