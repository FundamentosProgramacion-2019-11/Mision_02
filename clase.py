# Autor: tuNombreCompleto, A01745235
# Descripcion: Calcular el total de alumnos inscritos en una clase y el porcentaje de su genero.

# Escribe tu programa después de esta línea.

mujeres = int (input("¿Cuantas mujeres hay inscritas en tu clase?"))
hombres = int (input("¿Cuantos hombres hay inscritos en tu clase?"))

total_de_alumnos = mujeres+hombres

porcentaje_mujeres = ((mujeres*100)/total_de_alumnos)
porcentaje_hombres = ((hombres*100)/total_de_alumnos)

print ("El total de alumnos es de ",total_de_alumnos)
print ("Hay: %.1f"% porcentaje_mujeres, " % de mujeres")
print ("Hay: %.1f"% porcentaje_hombres, " % de hombres")