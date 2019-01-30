# Jose Luis Mata Lomelí
# A01377205
# Programa que calcule el porcentaje de hombres y mujeres inscritos en una clase


#Entrada = Cantidad de alumnos femeninos y masculinos
Femm= int(input("Escriba la cantidad de alumnas inscritas: "))
Masc= int(input("Escriba la cantidad de alumnos inscritos: "))

#E/S = Calcular total de alumnos y porcentajes
Total= Femm + Masc
Porcentaje_Femm= (Femm*100)/Total
Porcentaje_Masc= (Masc*100)/Total

#Salida = Resultado de calculos
print("Total de inscritos: ", (Total))
print("Porcentaje de Alumnas: %.1f" % Porcentaje_Femm, "%")
print("Porcentaje de Alumnos: %.1f" % Porcentaje_Masc, "%")

