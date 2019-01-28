# Autor: Daniela Estrella, A017457543
# Descripción: Dada la cantidad de galletas que se quieren cocinar, se dará la cantidad de ingredientes
# requeridos.

# Empieza a escribir tu código a partir de esta línea.

nGalleta= int(input("Teclea la cantidad de galletas que deseas preparar:"))
azucar= nGalleta*1.5 /48
mantequilla= nGalleta*1 /48
harina= nGalleta*2.75/48

print("Necesitarás", azucar,"tazas de Azúcar")
print(mantequilla,"tazas de Mantequilla")
print("y", harina,"tazas de Harina")
