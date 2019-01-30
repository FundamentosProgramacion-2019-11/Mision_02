# Autor: YadiraFuentesCalderón,     a01745235
# Descripcion: Calcular la distancia entre dos puntos

x1 = int (input("Introduce el punto x de la primera cordenada"))
y1 = int (input("Introduce el punto y de la primera cordenada"))

x2 = int (input("Introduce el punto x de la segunda cordenada"))
y2 = int (input("Introduce el punto y de la segunda cordenada"))

distancia = (((x2-x1)**2)+((y2-y1)**2))**.5

print ("La distancia entre ambos puntos es de %.3f"% distancia)