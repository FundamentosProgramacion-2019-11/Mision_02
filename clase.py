# Autor: Ivana Olvera Mérida, A01746744
# Descripcion: Misión 2- Ejercicio 4: Hombres y mujeres inscritos

# Escribe tu programa después de esta línea.

mujeres = int (input ("numMujeres: "))
hombres = int (input ("numHombres: "))

totalDeAlumnos = mujeres+hombres
porcentajeDeMujeres = mujeres/totalDeAlumnos*100
porcentajeDeHombres = hombres/totalDeAlumnos*100

print ("Total de alumnos inscritos: %.1f" % (totalDeAlumnos))
print ("Porcentaje de mujeres: %.1f" % (porcentajeDeMujeres))
print ("Porcentaje de hombres: %.1f" % (porcentajeDeHombres))


