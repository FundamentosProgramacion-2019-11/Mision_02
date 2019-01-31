# Autor: José Isidro Sánchez Vázquez, A01748144
# Descripcion: Programa para calcular el costo total en un restaurante

# Escribe tu programa después de esta línea.

c=float(input("Costo de la comida: "))
p1=c*.13
p2=c*.16
ct=p1+p2+c
print("El valor de la propina es:%.2f"%(p1))
print("El valor del IVA es:%.2f"%(p2))
print("El valor total es:%.2f"%(ct),"pesos")
