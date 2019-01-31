#Víctor Iván Morales Ramos a01377601
#analisis: Crear un algoritmo que calcule la cantidad porcentual de hombres y mujeres en una clase.

m = float(input("Cuantas mujeres hay en la clase: "))
h = float(input("Cuantos hombres hay en la clase: "))

t = m + h
pm = (m / t) * 100
ph = (h / t) * 100

print("El total de alumnos es:" , t)
print("El porcentaje de mujeres en el salon es: %" , pm )
print("El porcentaje de hombres en el salon es: %" , ph)
