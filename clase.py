# Autor: Juan Carlos Flores García, A01376511
# Descripcion: Programa que calcula el total de alumnos inscritos y el porcentaje de hombres y mujeres.

# Escribe tu programa después de esta línea.
mujeresNumero = float(input("Teclea el número de mujeres incritas: "))
hombresNumero = float(input("Teclea el número de hombres inscritos: "))


total = mujeresNumero + hombresNumero
mujeresPorcentaje = mujeresNumero/total*100
hombresPorcentaje = hombresNumero/total*100


print("Mujeres Inscritas: ", mujeresNumero)
print("Hombres Inscritos: ", hombresNumero)
print("Total de inscritos: %d", total)
print("Porcentaje de Mujeres: %.1f %" % mujeresPorcentaje)
print("Porcentaje de Hombres: %.1f %" % hombresPorcentaje)
