# Autor: Yasmín Landaverde Nava, A01745725
# Descripcion: Este programa calcula el porcentaje de hombres y mujeres en una clase

m = int(input("¿Cuántas mujeres se inscribieron a la clase: " ))
h = int(input("¿Cuántos hombres se inscribieron a la clase?: "))
tt = m + h
m2 = m*100/tt
h2 = h*100/tt
print("Mujeres inscritas: ", m)
print("Hombres incritos: ", h)
print("Total de inscritos", tt)
print("Porcentaje de mujeres: ", "%.1f" % m2, "%")
print("Porcentaje de hombres: ", "%.1f" % h2, "%")
