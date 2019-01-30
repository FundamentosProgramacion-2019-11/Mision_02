# Jose Luis Mata Lomelí
# A01377205
# Programa que calcule una velocidad con datos dados por el usuario con otros valores ya dados

# Entrada = Velocidad del usuario
velocidad = int(input("Escriba la velocidad del vehiculo: "))

# E/S = Calcular distancia y tiempo
distancia_formula_a= velocidad * 6
distancia_formula_b= velocidad * 3.5
tiempo_formula= 485 / velocidad

# Salida = Imprimir los resultados
print("Velocidad del vehiculo: ", velocidad)
print("Distancia recorrida en 6 horas es: %.1f" % distancia_formula_a, "km")
print("Distancia recorrida en 3.5 horas es: %.1f" % distancia_formula_b, "km")
print("Tiempo para recorrer 485 km seria: %.1f" % tiempo_formula, "hrs")

