#Autor: Martha Margarita Dorantes Cordero 
#porcentajes 



m = int(input("Mujeres inscritas: "))
h = int(input("Hombres inscritos: "))
t = m+h;

print('Total de inscritos: ',t)
print('Porcentaje de mujeres: {0:.1f}%'.format(m/t*100))
print('Porcentaje de hombres: {0:.1f}%'.format(h/t*100))