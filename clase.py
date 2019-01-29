# Autor: Cesar Guzman Guadarrama, A01748918
# Descripcion: Este programa te dice el total de alumnos que hay y el porcentaje que hay de hombres y mujeres.


m = int(input("¿Cuantas mujeres hay?"))
h = int(input("¿Cuantos hombres hay?"))

total = m + h
print("Ha un total de ", total, "alumnos")

pm = round((m*100) / total,1)
print("El porcentaje de mujeres es de %",pm)

ph = round((h*100) / total,1)
print("El porcentaje de hombres es del %",ph)

