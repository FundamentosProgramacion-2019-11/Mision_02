# Jose Luis Mata Lomelí
# A01377205
# Programa para convertir la temperatura de °F a °C


#Datos de Entrada = Grados Farhenheit
fahrenheit = int(input("Teclea la temperatura en °F (sin °) : "))

#E/S = Conversion
celsius = (fahrenheit - 32)*(5/9)

#Salida = Imprimir resultado
print("La temperatura en °C sería de: %.2f" % celsius, "°C")

