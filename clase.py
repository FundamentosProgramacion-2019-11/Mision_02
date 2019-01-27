# Autor: Bruno Omar Jiménez Mancilla
# Descripcion: Calcular el porcentaje de hombre y mujeres en una clase

# Escribe tu programa después de esta línea.
y=float(input("Número de mujeres inscritas: "))
x=float(input("Número de hombres inscritos: "))
t=x+y
p1=(y/t)*100
p2=(x/t)*100
print("Total de inscritos: ",round(t),
      "Porcentaje de mujeres",round(p1,1),"%",
      "Porcentaje de hombres: ",round(p2,1),"%")
