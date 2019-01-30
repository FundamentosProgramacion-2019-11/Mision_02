#Autor: Itzel Yanabany Castro Becerril
#Calcular el porcentaje de hombres y mujeres inscritos
mujeres=int(input("Mujeres inscritas: "))
hombre=int(input("Hombres inscritos: "))
total= mujeres+hombre
pmujeres=(mujeres*100) / total
phombres=(hombre*100)/ total
print("Total de inscritos: ", total)
print("Porcentaje de mujeres: %.1f" %(pmujeres)) 
print("Porcentaje de Hombres: %.1f" %(phombres))

