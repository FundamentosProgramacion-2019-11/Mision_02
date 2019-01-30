# Autor: Elizabeth Citlalli Zapata Cortes, A01746002
# Descripcion: Calcular el porcentaje de mujeres y hombres inscritos en una clase.

# Escribe tu programa después de esta línea.

#Entradas
mujeres = int(input("Mujeres inscritas: "))
hombres = int(input("Hombres inscritos: "))

#Calculo
total = mujeres + hombres
porcentajeMujeres = (mujeres * 100) / total
porcentajeHombres = (hombres * 100) / total

#Imprimir
print("Total de inscritos: ", (total))
print("Porcentaje de mujeres: %.1f" %(porcentajeMujeres), "%")
print("Porcentaje de hombres: %.1f" %(porcentajeHombres), "%")