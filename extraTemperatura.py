# Autor: Cecilia Daniela Olivares Hernández, a01745727
# Descripcion: Conversión de temperatura de escala Fahrenheit a la escala Celsius

# Escribe tu programa después de esta línea.

F = int(input("Inserta la temperatura en Fahrenheits: "))

C = (F - 32) / 1.8

print("La tenperatura Fahrenheit en Celsius es: "'%.4f' % C)
