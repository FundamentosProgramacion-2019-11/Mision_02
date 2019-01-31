# Autor: Rosalía Serrano Herrera, A01374781
# Descripcion: Calcula el total de alumnos inscritos así como el porcentaje de hombres y mujeres.

# Escribe tu programa después de esta línea.
mujeres = int(input("Teclea el número de mujeres inscritas: "))
hombres = int(input("Teclea el número de hombres inscritos: "))
total = mujeres + hombres
porcentajeM = mujeres/total*100
porcentajeH = hombres/total*100
print("El total de alumnos inscritos es", total)
print("El porcentaje de mujeres inscritas es: %.1f" % (porcentajeM), "%")
print("El porcentaje de hombres inscritos es: %.1f" % (porcentajeH), "%")