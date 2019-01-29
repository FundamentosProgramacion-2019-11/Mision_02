# Autor: tuNombreCompleto, tuMatricula
# Descripcion: Texto que describe en pocas palabras el problema que estás resolviendo.

# Escribe tu programa después de esta línea.
-------------------------------------------------------------------------------------------
# Autor: Santiago España Vázquez, A01748311
# Descripcion: Entregar distintos datos dependiendo de la velocidad que se indica

#Entradas
velocity=(int(input("Por favor introduzca la velocidad a la que viaja el auto en Km/H: ")))

#Salidas
print("La distancia que recorre el vehiculo en 6 horas es: %.1f" %(velocity*6))
print("La distancia que recorre el vehiculo en 3.5 horas es: %.1f" %(velocity*3.5))
print("El tiempo que tardara en recorrer 485 km es de: %.1f" %(485/velocity))
