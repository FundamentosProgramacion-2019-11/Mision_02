# Autor: Ronaldo Estefano Lira Buendia
# Programa donde calcule el porcentaje de hombres y mujeres inscritos

h=int(input("Ingresa el numero de hombres inscritos: "))
m=int(input("Ingresa el numero de mujeres inscritas: "))

t=h+m
ph=(h/t)*100
pm=(m/t)*100

print("Hombres inscritos: ", h)
print("Mujeres inscritas: ", m)

print("Total de inscritos: ", t)
print("Porcentaje de mujeres: {0:.1f}%".format(pm))
print("Porcentaje de hombres: {0:.1f}%".format(ph))