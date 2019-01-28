#Autor: Eric Andrés Jardón Chao, A01376748
#Descripción: Programa que calcula la distancia recorrida en 6 y 3.5 horas respectivamente, así como el tiempo necesario para recorrer 485 km, dada la velocidad en km/h.

vel=int(input("Teclea aquí la velocidad del auto en km/h enteros: "))

dist1= vel*6
dist2= vel*3.5
tiempo=485/vel
tiempoH=485//vel
tiempomin=int((tiempo-tiempoH)*60)

print("La velocidad del auto es:",vel,"km/h")
print("La distancia recorrida en 6 horas es de:",dist1,"km.")
print("La distancia recorrida en 3.5 horas es de:",dist2,"km.")
print("El tiempo necesario para que el auto recorra 485 km es de:",tiempoH,"horas con %.1f"% (tiempomin),"minutos.")

#Fin del programa