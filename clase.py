#Rafael Romero Bello A01747730
#Este programa saca el porcentaje de un grupo conformado por hombres y mujeres
h=float(input("inserte el numero de hombres:"))
m=float(input("inserte el numero de mujeres:"))
t=h+m
ph=(h/t)*100
pm=(m/t)*100
print("el total de personas es:",t)
print("el porcentaje de hombres es de:%.2f"%(ph))
print("el porcentaje de mujeres es de :%.2f"%(pm))
