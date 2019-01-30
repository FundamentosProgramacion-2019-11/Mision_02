# Autor: YadiraFuentesCalderón, A01745235
# Descripcion: Calcular distancias y tiempos recorridos con un auto que va a velocidad constante.

# Escribe tu programa después de esta línea.

velocidad = int (input ("¿A que velocidad (en km/hr) viaja tu auto?" ))

#velocidad = distancia/tiempo
#distancia = velocidad*tiempo
#tiempo = distancia/velocidad

distancia_6_horas = velocidad*6
distancia_3_y_media_hora = velocidad*3.5
tiempo_485_km = 485/velocidad

print ("La distancia recorrida en 6 horas es de: ",distancia_6_horas,"km")
print ("La distancia recorrida en 3 horas y media es de: ",distancia_3_y_media_hora,"km")
print ("El tiempo que tardaría tu auto en recorrer 485km es de : ",tiempo_485_km,"hrs")