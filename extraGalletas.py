# Autor: Cesar Guzman Guadarrama, A01748918
# Descripcion: Este programa te indicara la cantidad de ingredientes que necesitas


G = int(input("¿Cuantas Galletas quieres hacer?"))

A = (G * 1.5) / 48
M = (G * 1) / 48
H = (G * 2.75) / 48

print("Necesitas ",A, "tazas de azucar")
print("Necesitas ",M, "tazas de mantequilla")
print("Necesitas ",H, "tazas de harina")