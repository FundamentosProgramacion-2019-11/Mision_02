# Autor: Katia Hernández Barrera
# Descripcion: Programa quew calcula porcentaje de hobres y mujeres así como total de alumnos inscritos

# Escribe tu programa después de esta línea.
M = int (input("escriba el número de mujeres"))

H = int (input("escriba el número de hombres"))

Total = M+H

print ("Total de alumnos", Total)

PorcentajeM = (M*100)/Total

print ("Mujeres inscritas", PorcentajeM)

PorcentajeH = (H*100)/Total

print ("Hombres inscritos", PorcentajeH)
