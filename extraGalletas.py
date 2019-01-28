#Autor: Eric Andrés Jardón Chao, A01376748
#Descripción: Calcula la cantidad de ingredientes necesarios para hacer x número de galletas.

galletas=int(input("Teclea el número de galletas enteras a elaborar: "))
azucar= galletas*(1.5/48)
manteq=galletas*(1/48)
harina=galletas*(2.75/48)

print("Para hacer",galletas,"galletas:")
print("se requieren %.2f" %(azucar),"tazas de azúcar,")
print("se requieren %.2f"%(manteq),"tazas de mantequilla,")
print("y se requieren %.2f" %(harina),"tazas de harina.")

#Fin del programa