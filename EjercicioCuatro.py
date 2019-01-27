h=int(input("Cuantos hombres estan inscritos"))
m=int(input("Cuantas mujeres hay inscritas"))
total=m+h
ph=(h*100)/total
pm=(m*100)/total
print("El total de alumnos inscritos son ",total)
print("EL porcenaje de hombre es de ",ph,"%")
print("EL porcenaje de mujeres es de ",pm,"%")