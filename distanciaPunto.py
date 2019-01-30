#Autor: Aline Paulette Villegas Berdejo, A01375818
#Descripción: Calcular la distancia entre dos puntos


x1=float(input("x1: "))
y1=float(input("y1: "))
x2=float(input("x2: "))
y2=float(input("y2: "))

d=((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))**0.5
print("Distancia: %.3f " % d)
