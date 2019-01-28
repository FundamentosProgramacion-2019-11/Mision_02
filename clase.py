# Autor: Luis Alberto Zepeda Hernandez, A01328616
# Descripcion: calcular el porcentaje de hombres y mujeres inscritos en una clase.

# Escribe tu programa después de esta línea.

mujeres = int(input("Mujeres inscirtas: "))
hombres = int(input("Hombres inscritos: "))

total = hombres + mujeres
porcentajeMujeres = mujeres / total * 100
porcentajeHombres = hombres / total * 100

print("Total inscritos: ", total, "alumnos")
print("Porcentaje de mujeres inscritas: ", "{0:.1f}".format(porcentajeMujeres),"%")
print("Porcentaje de hombres inscritos: ", "{0:.1f}".format(porcentajeHombres),"%")
