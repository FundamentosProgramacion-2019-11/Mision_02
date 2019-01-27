# Autor: David Yair Fernández Salas, Matricula A01747088
# Descripcion: Este programa te dice el tiempo y la velocidad final de un carro

# Escribe tu programa después de esta línea.

velocidadinicial=float(input("Velocidad del auto en Km/h: "))
t1= 6
t2= 3.5
d3= 485
d1= velocidadinicial*t1
d2= velocidadinicial*t2
t3= d3/velocidadinicial
print("Distancia recorrida en 6 hrs: ", d1,"km")
print("Distancia recorrida en 3.5 hrs", d2,"km")
print("Tiempo para recorrer 485km:", t3,"hrs.")