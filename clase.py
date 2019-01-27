# Autor: David Yair Fernández Salas, Matricula A01747088
# Descripcion: Este programa te dice cuantos hombres y mujeres hay en una clase

# Escribe tu programa después de esta línea.

mujeres = int(input("Mujeres inscritas: "))
hombres = int(input("Hombres inscritos: "))
totalalumnos = hombres+mujeres
porcentajemujeres = (mujeres*100)/totalalumnos
porcentajhombres = (hombres*100)/totalalumnos

print("Total de inscritos: ",totalalumnos)
print("Porcentaje de mujeres: ",porcentajemujeres,"%")
print("Porcentaje de hombres: ",porcentajhombres,"%")