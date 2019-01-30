# Autor: Mario Hernández Cárdenas, A01375869
# Descripcion: Calcular el total de alumnos, y el porcentaje de hombres y mujeres.

# Escribe tu programa después de esta línea.

mujeres = int(input("Escriba el total de mujeres en la clase: "))
hombres = int(input("Escriba el total de hombres en la clase: "))

Total = mujeres + hombres
mujeresp = (mujeres / Total)*100
hombresp = (hombres / Total)*100

print("La cantidad total de alumnos son:",Total)
print("El porcentaje de mujeres es: %.1f"%mujeresp,"%")
print("El porcentaje de hombres es: %.1f"%hombresp,"%")

