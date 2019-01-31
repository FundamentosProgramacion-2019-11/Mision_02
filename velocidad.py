# Autor: tKarla Ximena Rueda Ruiz, A01745943
# Descripcion: Cálculo de distancias y tiempo recorrido de un automóvil. 

# Escribe tu programa después de esta línea.

#vu=velocidad usuario (la que el indica)
#d1= distancia 1
#d2=distancia 2
#tr= tiempo requerido en 485 km

vu = int(input("velocidad del auto en km/h: "))


d1 = (6*vu)

print("Distancia recorrida en 6 hrs:", d1)

d2 = (3.5*vu)

print("Distancia recorrida en 3.5 hrs:", d2)

tr = (485/vu)
print("Tiempo para recorrer 485 km:", tr)
