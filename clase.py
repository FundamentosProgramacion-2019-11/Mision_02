# Autor: Cecilia Daniela Olivares Hernández, A01745727
# Descripcion: calculo de el porcentaje total de hombres y mujeres inscritos en una clase.

# Escribe tu programa después de esta línea.

m = int(input("Inserta el numero de mujeres inscritas: "))

h = int(input("Inserta el numero de hombres inscritos: "))

total = m + h

ph = (h/total)*100

pm= (m/total)*100

print("El numero total de alumnos inscritos es: ",total)

print("El porcentaje de hombres es: " '%.1f' % ph,"%")

print("El porcentaje de mujeres es: " '%.1f' % pm,"%")