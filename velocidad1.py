#Francsico Javier González Molina A01748636
#Calcular la datos de un auto con"X" velocidad

velocidad= int (input("Velocidad del automovil en Km/h: "))

distancia1=6*velocidad
distancia2=3.5*velocidad
tiempo=485/velocidad

print ("""Velocidad del auto: %d Km/h
Distancia recorrida en 6 hrs: %.1f Km
Distancia recorrida en 3.5 hrs: %.1f Km
Tiempo para recorrer 485 km: %.1f hrs."""%(velocidad,distancia1,distancia2,tiempo))