# Autor: Marianela Contreeras Domínguez, A01374769
# Descripcion: Programa para calcular la distancia y tiempo que recorre un auto. 

# Escribe tu programa después de esta línea.

velocidad = float (input("velocidad (en km/h):"))

distancia1= velocidad*6

distancia2 = velocidad*3.5

tiempo = 485/velocidad

print ("Distancia recorrida en 6 hrs es:%.1f" %(distancia1), "km")
print ("Distancia recorrida en 3.5 hrs es:%.1f" %(distancia2), "km")
print ("Tiempo para recorrer 485 km es:%.1f" %(tiempo), "hrs.")


