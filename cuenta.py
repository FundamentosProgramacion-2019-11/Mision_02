# Autor: Diego Raul Elizalde Uriarte, a01748756
# Descripcion: Calcule el costo total de una comida en un restaurante

# Escribe tu programa después de esta línea.

#Lecturas
tc = int(input("Dame el total de la comida: "))

#Calculo de resultados
p = tc*.13
IVA = tc*.16
tp = tc+p+IVA

#Imprimir resultados
print("Costo de su comida: ",tc)
print("Propina: %.2f" %(p))
print("IVA: %.2f" %(IVA))
print("Total a pagar: %.2f" %(tp))




