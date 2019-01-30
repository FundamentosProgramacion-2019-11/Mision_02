# Autor: Mariana Coria Rodríguez, A01374765
# Descripcion: Porcentaje hombres y mujeres

# Escribe tu programa después de esta línea.
mujeres = int(input("Mujeres inscritas: "))
hombres = int(input("Hombres inscritos: "))
total = mujeres + hombres
print("Total de inscritos:", total)
pmujeres = mujeres*100/total
print("Porcentaje de mujeres: %.1f" % (pmujeres))
phombres = hombres*100/total
print("porcentaje de hombres: %.1f" % (phombres))
#No supe como poner el signo de % para marcar que era un porcentaje :(
#lo encerre en comillas simples y me marcaba error 
