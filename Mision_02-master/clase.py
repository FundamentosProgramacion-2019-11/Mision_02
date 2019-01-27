# Autor: Guillermo De Anda Casas, A01375892
# Descripcion: Calcular total de alumnos y porcentaje por sexo.

# Escribe tu programa después de esta línea.

m = int(input("Escriba el número de mujeres: "))
h = int(input("Escriba el número de hombres: "))

t = m+h

pm = (m/t)*100

ph = (h/t)*100

print("Mujeres inscritas: ",m)
print("Hombres inscritos: ",h)
print("Total de alumnos: ",t)
print("Porcentaje de mujeres: ","{:.1f}".format(pm),"%")
print("Porcentaje de hombres: ","{:.1f}".format(ph),"%")
