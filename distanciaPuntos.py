# Autor: Alan Giovanni Rodriguez Camacho A01748185
# Descripcion: Programa para calcular la distancia entyrre dos puntos.

# Escribe tu programa después de esta línea.

x1=int(input("Dame el valor de x1: "))
x2=int(input("Dame el valor de x2: "))
y1=int(input("Dame el valor de y1: "))
y2=int(input("Dame el valor de y2: "))

d=(((x2-x1)**2)+((y2-y1)**2))**.5

print("x1: {0}".format(x1))
print("x2: {0}".format(x2))
print("y1: {0}".format(y1))
print("y2: {0}".format(y2))
print("Distancia: %.03f"%(d))
