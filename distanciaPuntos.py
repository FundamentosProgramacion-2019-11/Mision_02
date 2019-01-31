# Autor: Karla Ximena Rueda Ruiz, A01745943
# Descripcion: Cálculo de distancia entre dos puntos.

# Escribe tu programa después de esta línea.

x2=int(input("Teclea el valor de x2: "))
x1=int(input("Teclea el valor de x1: "))
y2=int(input("Teclea el valor de y2: "))
y1=int(input("Teclea el valor de y1: "))


d =((x2-x1)**2 + (y2-y1)**2) **0.5

print("Distancia: ",d)
