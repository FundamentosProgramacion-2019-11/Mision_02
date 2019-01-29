# Autor: Maria Angelica Hernandez Parada, A01169796
# Descripcion: Calcular el porcentaje de hombres y mujeres

# Escribe tu programa después de esta línea.

mujeres = int(input("Mujeres inscritas: "))
hombres = int(input("Hombres inscritos: "))

total = (mujeres + hombres)
porcentajemujeres = (mujeres * 100 / total)
porcentajehombres = (hombres * 100 / total)

print ("Total de inscritos: " , total )
print ("Porcentaje de mujeres: %.1f" % (porcentajemujeres), "%")
print ("Porcentaje de hombres: %.1f" % (porcentajehombres), "%")