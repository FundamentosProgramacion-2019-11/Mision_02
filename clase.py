# Autor: Francisco Javier González Molina a01748636
# Algoritmo que de porcentaje de hombres y mujeres inscritos

no_hombres= int (input("Escribe el numero de hombres que se han inscrito: "))
no_mujeres= int (input("Escribe el numero de mujeres que se han inscrito: "))

total_inscritos=no_hombres+no_mujeres
porcentaje_mujeres=(no_mujeres*100)/total_inscritos
porcentaje_hombres=(no_hombres*100)/total_inscritos

print ("""Total de inscritos: %d
Porcentaje de mujeres: %.1f
Porcentaje de hombres: %.1f"""%(total_inscritos,porcentaje_mujeres,porcentaje_hombres))
