# Autor: Karimn Daniel Hernández Castorena
# Descripcion: Programa que cuenta cuantos alumnos hay en una clase y el porcentaje de mujeres y hombres

# Escribe tu programa después de esta línea.
print()

m = int(input("¿Cuántas mujeres hay en la clase? "))
h = int(input("¿Cuántos hombres hay en la clase? "))
print()
a = h + m
pm = m*100/a
ph = h*100/a

print("El total de alumnos es: ", (a))
print("El porcentaje de alumnas es: %.1f" % (pm),"%")
print("El porcentaje de alumnos es: %.1f" % (ph),"%")