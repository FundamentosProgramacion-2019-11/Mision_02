#Autor: Sara Delgado G.
#Descripcion: Calcula distancia entre dos puntos

x1= int(input("Valor de x1: "))
x2= int(input("Valor de x2: "))
y1= int(input("Valor de y1: "))
y2= int(input("Valor de y2: "))

d1= (x2-x1)**2
d2= (y2-y1)**2
d= d1+d2
dt=d**0.5

print("La distancia es: %.3f" % dt)
