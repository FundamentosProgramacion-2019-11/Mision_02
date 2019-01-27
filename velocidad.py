# Autor: Bruno Omar Jiménez Mancilla, A01748931
# Descripcion:Pedir la velocidad en km/hr y de ahí multiplicarla por el número de horas para saber cuánto recorre el auto en las horas dadas

# Escribe tu programa después de esta línea.
v=float(input("Ingresa la velocidad en enteros y km/hr: "))

v1=v*6.0
v2=v*3.5
t=485.0/v

print("Velocidad del auto en km/hr: ",v,
      "Distancia recorrida en 6 hr: ",v1,
      "Distancia recorrida en 3.5hrs: ",v2,
      "Tiempo para recorrer 485 km: ",t,)

