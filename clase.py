# Autor: Marianela Contreras Domínguez, A01374769
# Descripcion: Problema para calcular el porcentaje de hombres y mujeres de una clase. 

# Escribe tu programa después de esta línea.

mujeres = float(input("Mujeres inscritas:"))

hombres = float(input("Hombres inscritos:"))

total = int (mujeres + hombres)
porcentajeMujeres = (mujeres*100)/total
porcentajeHombres = (hombres*100)/total

print ("Total de alumnos inscritos:",(total))
print ("Porcentaje de mujeres: %.1f"% (porcentajeMujeres),"%")
print ("Porcentaje de hombres: %.1f" % (porcentajeHombres),"%")

