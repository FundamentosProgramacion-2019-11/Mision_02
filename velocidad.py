# Autor: Diego Raul Elizalde Uriarte, a01748756
# Descripcion: Pregunte la velocidad e imprima las distancias en el tiempo requerido y calcule el tiempo en cierta distancia.

# Escribe tu programa después de esta línea.

#Lectura y calculo de resultados
v = int(input("Dame la velocidad a la que viaja un auto en km/h y en numeros enteros: "))
t = 6

d = (v*t)

T = 3.5
D = (v*T)

dist = 485
tiem = (485/v)

#Imprimir resultados
print("La distancia en km. que recorre en 6 hrs. es de: %.1f" %(d),"km")
print("La distancia en km. que recorre en 3.5 hrs. es de: %.1f" %(D),"km")
print("El tiempo en horas y minutos que requiere para recorrer 485 km. es de: %.1f" % (tiem),"hrs.")


