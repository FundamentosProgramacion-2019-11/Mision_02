# Autor: David Yair Fernández Salas, Matricula: A01747088
# Descrpcion: Este programa te dice cuanto tiene que pagar una persona en un restaurante

# Escribe tu programa después de esta línea.

subtotal =float(input("Costo de su comida: "))
iva = 16/100
propina =13/100
ivareal=subtotal*iva
propinareal=subtotal*propina
costototal=subtotal+ivareal+propinareal
print("Propina: ","$",propinareal)
print("IVA","$",ivareal)
print("Total a pagar: ","$",costototal)