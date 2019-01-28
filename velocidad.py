# Autor: Luis Alberto Zepeda Hernandez, A01328616
# Descripcion: calcular distancia recorrida y tiempo, con ciertos datos.

# Escribe tu programa después de esta línea.

velocidad = int(input("Introduce velocidad en km/hr y en numeros enteros: "))

primerDistancia = velocidad * 6
segundaDistancia = velocidad * 3.5
tiempo1 = 485 / velocidad

print("Distancia recorrida en 6 hrs: ", "{0:.1f}".format(primerDistancia), "km.")
print("Distancia recorrida en 3.5 hrs: ", "{0:.1f}".format(segundaDistancia), "km.")
print("Tiempo para recorrer 485 km: ", "{0:.1f}".format(tiempo1), "hrs.")
