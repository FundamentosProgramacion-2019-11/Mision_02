# Autor: Bernardo Mondragon Ramirez, A01022325
# Descripcion: distancia en 6,3.5 horas y tiempo en 485 km.

# Escribe tu programa después de esta línea.

v= int(input("Ingresa la velocidad en Km/h : "))

d1= 6*v
d2 = 3.5*v
t= (485)/v

print("Distancia recorrerá en 6 horas = %.1f"% (d1), "km")

print("Distancia recorrerá en 3.5 horas = %.1f" %(d2),"km")

print("Para recorrer 485 km tardaría = %.1f " %(t),"horas")