# Autor: Ronaldo Estefano Lira Buendia
# Programa donde calcule la distancia de dos puntos en un plano carteciano

x1=int(input("Dame la coordenada x1: "))
y1=int(input("Dame la coordenada y1: "))
x2=int(input("Dame la coordenada x2: "))
y2=int(input("Dame la coordenada y2: "))

d=(((x2-x1)**2)+((y2-y1)**2))**(1/2)

print("x1: ", x1)
print("x2: ", x2)
print("y1: ", y1)
print("y2: ", y2)
print("Distancia: {0:.3f}".format(d))
