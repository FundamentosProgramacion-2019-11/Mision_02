# Autor: José Isidro Sánchez Vázquez
# Descripcion: Calcular los ingredientes necesarios para galletas

# Escribe tu programa después de esta línea.

N=int(input("Cuantas galletas quieres:"))
A=(N*1.5)/48
M=(N*1)/48
H=(N*2.75)/48
print("La cantidad de tazas de azucar que necesitas son:%.2f"%(A))
print("La cantidad de tazas de mantequilla que necesitas son:%.2f"%(M))
print("La cantidad de tazas de harina que necesitas son:%.2f"%(H))