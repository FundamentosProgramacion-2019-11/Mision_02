#Víctor Iván Morales Ramos A01377601

#Análisis: Se requiere un algoritmo que haga las operaciones necesarias para obtener los datos de desplazamiento de un auto recibiendo solo datos base.

v = float(input("dame la velocidad a la que viaja el auto en km/h: "))

t1 = 6
t2 = 3.5
d = 485

dp1 = t1 * v
dp2 = t2 * v
tp1 = d / v

print("La distancia recorrida en km que recorre el auto en 6 horas es: " , dp1)
print("La distancia recorrida en km que recorre el auto en 3.5 horas es: " , dp2)
print("El tiempo en horas y minutos que requiere para recorrer 485 km es: " , tp1)
