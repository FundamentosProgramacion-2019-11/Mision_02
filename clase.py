#Autor: Eric Andrés Jardón Chao, A01376748
#Descripción: Calcula el número total de aumnos inscritos, el porcentaje de alumnos varones y el porcentaje de alumnas.

muj=int(input("Teclea el número de mujeres inscritas: "))
hom=int(input("Teclea el número de hombres inscritos: "))

totalAlumnos= hom + muj
percentMuj= (muj/totalAlumnos)*100
percentHom= (hom/totalAlumnos*100)

print("Mujeres inscritas: ",muj)
print("Hombres inscritos: ",hom)
print("El número de alumnos inscritos en total es: ",totalAlumnos)
print("El porcentaje de mujeres es de: %.1f" %(percentMuj),"%")
print("El porcentaje de hombres es de: %.1f" % (percentHom),"%")

#Fin del programa