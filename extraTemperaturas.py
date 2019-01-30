# Autor: Elizabeth Citlalli Zapata Cortes, A01746002
# Descripcion: Realizar conversión de temperaturas en escala Fahrenheit a escala Celsius.

#Entradas
farenheit = int(input("Temperatura en grados Farenheit: "))

#Calcular
celsius = (farenheit - 32) * (5/9)

#Imprimir
print("Temperatura en grados Celsius: %.2f" % (celsius),"°")