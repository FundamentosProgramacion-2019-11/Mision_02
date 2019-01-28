#Autor: Eric Andrés Jardón Chao, A01376748
#Descripción: Calcula la distancia entre dos puntos dadas sus coordenadas en el plano (x,y).

x1=float(input("Inserta la coordenada x del primer punto: "))
y1=float(input("Inserta la coordenada y del primer punto: "))
x2=float(input("Inserta la coordenada x del segundo punto: "))
y2=float(input("Inserta la coordenada y del segundo punto: "))

distancia=((x2-x1)**2+(y2-y1)**2)**0.5

print("Las coordenadas del primer punto son: (",x1,",",y1,")")
print("Las coordenadas del primer punto son: (",x2,",",y2,")")

print("La distancia entre los dos puntos es de: %.3f" %(distancia)," unidades.")

#Fin del programa