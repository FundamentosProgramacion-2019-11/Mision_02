# Autor: José Isidro Sánchez Vázquez, A01748144
# Descripcion: Calculador de distancia entre dos puntos

# Escribe tu programa después de esta línea.

x1=float(input("Dime la coordenada x1:"))
y1=float(input("Dime la coordenada y1:"))
x2=float(input("Dime la coordenada x2:"))
y2=float(input("Dime la coordenada y2:"))
d=((x2-x1)**2+(y2-y1)**2)**.5
print("La distancia entre los puntos es:%.3f"%(d))