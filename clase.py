# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.

# Autor: Santiago España Vázquez, A01748311
# Descripcion: Entregar porcentaje de hombres-mujeres en una clase

#Entradas
men=float(input("Por favor introduzca el número de hombres inscritos a la clase: "))
women=float(input("Por favor introduzca el número de mujeres inscritas a la clase: "))

#Calculo
plus=men+women

#Salidas
print("El total de alumnos en la clase es de: %.1f" %plus)
print("El porcentaje de hombres en la clase es de: %.1f" %((men*100)/plus), "%")
print("El porcentaje de mujeres en la clase es de: %.1f" %((women*100)/plus), "%")

