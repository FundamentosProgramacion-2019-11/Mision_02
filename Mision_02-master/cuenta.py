# Autor: Guillermo De Anda Casas, A01375892
# Descripcion: Calcula propina, IVA y total a pagar.

# Escribe tu programa después de esta línea.

C = int(input("Escriba el costo de la comida: "))

p = C*0.13
IVA = C*0.16
t = C+p+IVA

print("Costo de su comida: $","{:.2f}".format(C))
print("Propina: $","{:.2f}".format(p))
print("IVA: $","{:.2f}".format(IVA))
print("Total a pagar: $","{:.2f}".format(t))
