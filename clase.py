# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.
# Autor: Sofía Daniela Méndez Sandoval, A01242259
# Descripcion: Calcula el porcentaje de hombres y mujeres en una clase

mujeres = int(input("¿Cuántas mujeres hay en la clase? "))
hombres = int(input("¿Cuántos hombres hay en la clase? "))

alumnos = mujeres + hombres

pm = mujeres*100/alumnos
ph = hombres*100/alumnos

print("Total de alumnos inscritos: ", alumnos)
print(("Porcentaje de mujeres: "), "%.1f" % pm, "%")
print(("Porcentaje de hombres: "), "%.1f" % ph, "%")
