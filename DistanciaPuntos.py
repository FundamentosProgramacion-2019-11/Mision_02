#Autor: Martha Margarita Dorantes Cordero 
#distancia entre los puntos



import math

x1 = int(input("Ingrese x1: "))
y1 = int(input("Ingrese y1: "))
x2 = int(input("Ingrese x2: "))
y2 = int(input("Ingrese y2: "))
res = math.sqrt((x2-x1)**2+(y2-y1)**2)
print('La distancia entre los puntos (%d,%d) y (%d,%d) es: %.3f'%(x1,y1,x2,y2,res))
