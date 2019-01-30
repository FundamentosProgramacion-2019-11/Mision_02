#Autor: Sara Delgado G.
#Descripción: Calcula porcentaje de hombres y mujeres

hombres= int(input("Número de hombres inscritos: "))
mujeres= int(input("Número de mujeres inscritas: "))

total= hombres+mujeres
h= (hombres*100)/total
m= (mujeres*100)/total

print("Total inscritos: ", total)
print("Porcentaje de hombres: %.1f "% h)
print("Porcentaje de mujeres: %.1f" % m)