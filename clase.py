# Autor: Mariana Teyssier Cervantes
# Descripcion: Calcular el numero total de alumnos y el porcentaje de hombres y mujeres incritos.

# Escribe tu programa despues de esta linea.

Mujeres = int(input("Teclea el numero de mujeres inscritas: "))
Hombres = int(input("Teclea el numero de hombres inscritos: "))

Total = Mujeres + Hombres
Porcentaje1 = Mujeres*100/Total
Porcentaje2 = Hombres*100/Total

print "Total de alumnos inscritos: ", (Total)
print "Porcentaje de mujeres: ", format(Porcentaje1, ".1f")
print "Porcentaje de hmbres: ", format(Porcentaje2, ".1f")

