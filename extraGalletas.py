# Autor: Elizabeth Citlalli Zapata Cortes, A01746002
# Descripcion: Indica cantidad de ingredientes a utilizar dependiendo de la cantidad de galletas que desea elaborar.

#Entradas
galletas = int(input("Galletas: "))

#Calcular
azucar = (galletas * 1.5) /48
mantequilla = galletas / 48
harina = (galletas * 2.75) /48

#Imprimir
print("Azúcar: %.2f" %(azucar), "tazas")
print("Mantequilla: %.2f" %(mantequilla), "tazas")
print("Harina: %.2f" %(harina), "tazas")
