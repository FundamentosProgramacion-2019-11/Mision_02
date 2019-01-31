# Autor: Bernardo Mondragon Ramirez, A01022325
# Descripcion: Calcular distancia de puntoA a puntoB
#
# Escribe tu programa después de esta línea

x1 = int(input("cordenada x1: "))
y1 = int(input("cordenada y1: "))
x2 = int(input("cordenada x2: "))
y2 = int(input("cordenada y2: "))

d=((x2-x1)**2 + (y2-y1)**2)**0.5

print("Distancia entre punto a y B: %.3f"%(d))