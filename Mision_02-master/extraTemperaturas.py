#Autor: Guillermo De Anda Casas , A01375892
#Código que convierte de grados Fahrenheit a Celsius.

F = int(input("Escribe la temperatura en Fº:"))

C = (F - 32) / 1.8

print("Temperatura: ", "{:.0f}".format(C), "Cº")

