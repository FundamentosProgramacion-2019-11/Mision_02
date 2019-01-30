# Autor: Aline Paulette Villegas Berdejo, A01375818
# Descripcion: Calcular IVA, propina y total a pagar de una cuenta

# Escribe tu programa después de esta línea.
tc=float(input("Costo de su comida: "))
p=tc*.13
iva=tc*.16
tp=p+iva+tc

print("Propina: $%.2f " % p)
print("IVA: $%.2f " % iva)
print("Total a pagar: $%.2f " % tp)
