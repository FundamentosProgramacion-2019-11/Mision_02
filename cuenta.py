# Autor: Ronaldo Estefano Lira Buendia
# Programa donde calcula el total de la cuenta

c=int(input("Introduce el total de la comida: "))

p=c*.13
i=c*.16
t=c+p+i

print("Costo de su comida: {0:.2f}".format(c))
print("Propina: {0:.2f}".format(p))
print("IVA: {0:.2f}".format(i))
print("Total a pagar: {0:.2f}".format(t))