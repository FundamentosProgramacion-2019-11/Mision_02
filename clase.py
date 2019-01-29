# Autor: Sofía Trujillo Vargas A01747320
# En este problema se calculará el total de alumnos de un grupo y se obtendra el porcentajde hombres y mujeres.

m=float(input("¿Cuantas mujeres hay en tu salón?: "))
h=float(input("¿Cuantos hombres hay en tu salón?: "))
t=m+h
pm=(m*100)/t
ph=(h*100)/t
print("El total de alumnos es: ",round(t,0))
print("El porcentaje de mujeres es: ",round(pm,0))
print("El porcentaje de hombre es: ",round(ph,0))