# Autor: Luis Fernando Duran Castillo, A01745792
# Descripcion: obtener el porcentaje de hombres y de mujeres en una salon de clase

# Escribe tu programa después de esta línea.

h= int(input("ponga la cantidad de hombres que hay en la clase: "))
m= int(input("ponga la cantidad de mujeres que hay en la clase: "))

t=h+m

ph=(h*100)/t
pm=(m*100)/t

print ("el total de alumnos es de: ", (t))
print ("el porcentaje de hombres inscritos es de: ",(ph))
print ("el porcentaje de mujeres inscritas es de :", (pm))