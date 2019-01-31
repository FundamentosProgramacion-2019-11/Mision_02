# Autor: Bernardo Mondragon Ramirez, A01022325
# Descripcion: Clacular numero de alumnos inscritos, procentaje de hombre y mujeres
#
# Escribe tu programa después de esta línea

m = int(input("Mujeres que hay en clase: "))

h = int(input("Hombres que hay en clase: "))

t = h+m

pm = (m*100)/t

ph = (h*100)/t

print("total de alumnos en clase: ",t)

print("porcentaje de Mujeres en clase: %.01f" %(pm))

print("porcentaje de Hombres en clase: %.01f" %(ph))


