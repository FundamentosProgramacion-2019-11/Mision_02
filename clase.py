# Autor: María Fernanda García Gastélum, A01376181
# Descripcion: Porcentaje de personas en una clase

# Escribe tu programa después de esta línea.

mujeres= int(input("Escribe el número de mujeres: "))
hombres= int(input("Escribe el número de hombres: "))
total= mujeres + hombres
porcentajedemujeres= (mujeres/total)*100
porcentajedehombres= (hombres/total)*100

print("Total de inscritos: ", total)
print("Porcentaje de mujeres: %.1f" %(porcentajedemujeres), "%")
print("Porcentaje de hombres: %.1f" % (porcentajedehombres), "%")
