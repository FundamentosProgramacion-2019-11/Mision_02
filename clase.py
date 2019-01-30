# Autor: Aline Paulette Villegas Berdejo
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.
m=int(input("Mujeres inscritas: "))
h=int(input("Hombres inscritos: "))

ta=m+h
pm=(m*100)/ta
ph=(h*100)/ta

print("Total de inscritos: ", ta)
print("Porcentaje de mujeres: %.1f" % pm,"%")
print("Porcentaje de hombre: %.1f" % ph, "%")
