# Autor: José Isidro Sánchez Vázquez
# Descripcion: Calculador de hombres y mujeres inscritos

# Escribe tu programa después de esta línea.

h=int(input("Cantidad de hombres inscritos:"))
m=int(input("Cantidad de mujeres inscritas:"))
total=h+m
pm=(m/total)*100
ph=(h/total)*100

print("El total de alumnos inscritos es:",total)
print("El porcentaje de mujeres inscritas es:%.2f"%(pm))
print("El porcentaje de hombres inscritos es:%.2f"%(ph))
