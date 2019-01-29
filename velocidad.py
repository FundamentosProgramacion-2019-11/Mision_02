# Autor: Cecilia Daniela Olivares Hernández, a01745727
# Descripcion: Calculo de la distancia en 6 y 3.5 hrs y el tiempo en 485km en base al valor de la velocidad que se inserte

# Escribe tu programa después de esta línea.

v = int(input("Inserta la velocidad a la cual viaja un auto en km/h enteros: "))

d1 = v*6

d2 = v*3.5

t= 485/v

print("La distancia en km que recorre el auto en 6 hrs es: " '%.1f' % d1,"km")

print("La distancia en km que recorre el auto en 3.5 hrs es: " '%.1f' % d2,"km")

print("El tiempo en hrs y minutos que requiere el auto para viajar 485km son: " '%.1f' % t,"hrs")
