#FRANCISCO JAVIER GONZÁLEZ MOLINA A01748636
#Calcular la velocidad de un automovil

a= int (input("""¿Que desea calcular? 
(por favor solo escriba el numero correspondiente).
1.Distancia (Km)
2.Tiempo    (Hrs)

Su seleccion: """))

if a==1:
    velocidad = float(input("Inserte valor de Velocidad en Km/h: "))
    tiempo= float (input("Inserte valor de Tiempo en Hrs: "))
    distancia_recorrida= tiempo*velocidad
    print ("Velocidad del auto en Km/h: ",velocidad)
    print ("La distancia recorrida en ",tiempo," hras : %.1f "%(distancia_recorrida),"Km")
elif a==2:
        velocidad= float (input("Inserte valor de Velocidad en Km/h: "))
        distancia= float (input("Inserte valor de Distancia en Km: "))
        tiempo_transcurrido=distancia/velocidad
        print ("Velocidad del auto en Km/h: ", velocidad)
        print ("El tiempo para recorrer ",distancia,"Km es: %.1f "%(tiempo_transcurrido),"Hrs")

else:
    print("Favor de escribir solo el numero de la opcion que desea.")


