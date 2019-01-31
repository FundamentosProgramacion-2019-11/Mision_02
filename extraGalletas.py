# Autor: Roberto Castro Barrios, A01748559
# Descripción: Programa que calcula la cantidad de ingredientes a usar dependiendo del numero de galletas solicitadas.
# Para 48 galletas, se requiere: 1.5 tazas de azúcar, 1 taza de mantequilla, 2.75 tazas de harina.
galle = int(input("Ingresa el número de galletas: "))

A = (1.5/48)*galle
M = (1/48)*galle
H = (2.75/48)*galle

print("La cantidad de tazas de azucar para %d galletas es de: %.3f"%(galle, A))
print("La cantidad de tazas de mantequilla para %d galletas es de: %.3f"%(galle, M))
print("La cantidad de tazas de harina para %d galletas es de: %.3f"%(galle, H))