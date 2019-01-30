# Autor: Alan Giovanni Rodriguez Camacho A01748185
# Descripcion: Programa que calcula el porcentaje de hombres y mujeres en una clase

# Escribe tu programa después de esta línea.

hombres=int(input("Numero de hombres inscritos: "))
mujeres=int(input("Numero de mujeres inscritos: "))

total=hombres+mujeres
porHombre=(hombres*100)/total
porMujer=(mujeres*100)/total

print("Total de inscritos: {0}".format(total))
print("Porcentaje de mujeres: %.01f"%(porMujer))
print("Porcentaje de hombres: %.01f"%(porHombre))

