# Autor: Roberto Castro Barrios, A01748559
# Descripcion: Programa que calcula el porcentaje de hombres y mujeres inscritos en un programa.

# Escribe tu programa después de esta línea.
h = int(input("¿Cuántos hombres hay? "))
m = int(input("¿Cuántas mujeres hay? "))

tot = m+h
perH = (h*100)/tot
perM = (m*100)/tot

print("El total de estudiantes inscritos es de: ", tot)
print("El porcentaje de hombres en el curso es de: %.1f"%(perH), "%")
print("El porcentaje de mujeres en el curso es de: %.1f"%(perM), "%")
