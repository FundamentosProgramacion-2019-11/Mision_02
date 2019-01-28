# Autor: Daniela Estrella, A01745753
# Descripcion: Calcular el porcentaje de hombres y mujeres dentro de un salón de clase.

# Escribe tu programa después de esta línea.
nMujeres= int(input("Ingresa el número de mujeres:"))
nHombres= int(input("Ingresa el número de hombres:"))

total= nMujeres+nHombres
pMujeres= (nMujeres*100)/total
pHombres= (nHombres*100)/total

print("En total hay", total,"alumnos en la clase")
print("Hay un", pMujeres,"% de mujeres")
print("y un", pHombres, "%de hombres")
