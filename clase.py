# Autor: Diego Raul Elizalde Uriarte, a01748756
# Descripcion: Calcula el porcentaje de hombres y mujeres inscritos en una clase.

# Escribe tu programa después de esta línea.

#Lecturas
m = int(input("Dame el numero de mujeres inscritas: "))
h = int(input("Dame el numero de hombres inscritos: "))

#Calculo de resultados
ti = m+h
pm = (m*100)/ti
ph = (h*100)/ti

#Imprimir resultados
print("Mujeres inscritas: ",m)
print("Hombres inscritos: ",h)
print("Total de inscritos: ",ti)
print("Porcentaje de mujeres: %.1f" %(pm,"%"),"%")
print("Porcentaje de hombres: %.1f" %(ph),"%")