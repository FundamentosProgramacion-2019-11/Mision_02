# Jose Luis Mata Lomelí
# A01377205
# Programa que calcule el costo total de una comida de un restaurante (con 16% de IVA y 13% de propina)

#Entrada = Costo de la comida
Comida= int(input("Escriba el costo de la comida: "))

#E/S = Calcular IVA, Propina y total a pagar
Propina = Comida * 0.13
IVA = Comida * 0.16
Total_Pagar = Comida + Propina + IVA

#Salida = Imprimir Resultados de Operaciones
print("Costo de la Comida: $%.2f" % Comida)
print("Propina: $%.2f" % Propina)
print("IVA: $%.2f" % IVA)
print("Total a pagar: $%.2f " % Total_Pagar)
