# Autor: Karla Ximena Rueda Ruiz, A01745943
# Descripcion: Cálculo de porcentaje de hombres y mujeres inscritos en una clase,así como el total de éstos.

# Escribe tu programa después de esta línea.

tm = int(input("Mujeres inscritas: "))
th = int(input("Hombres inscritos: "))

tot= (tm+th)
print("Total de inscritos:", tot)

pm=(tm*100/tot)
print("Porcentaje de mujeres:",pm)

ph=(th*100/tot)
print("Porcentaje de hombres:",ph)
