# Autor: Luis Alberto Zepeda Hernandez, A01328616
# Descripcion: convertir temeperatura de grados fahrenheit a la escala Celsius.

# Escribe tu programa después de esta línea.

fahrenheit = int(input("Ingresa tmeperatura en grados fahrenheit: "))

conversion = (fahrenheit - 32) / 1.8

print("Temepratura en Celsius: ", "{0:.2f}".format(conversion),"°C")

