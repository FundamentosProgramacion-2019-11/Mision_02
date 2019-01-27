# Autor: Bruno Omar Jiménez Mancilla A01748931
# Descripcion: Un programa que calcule IVA, propina y el total de una comida

# Escribe tu programa después de esta línea.
c=float(input("Ingresa el total de tu comida: "))
p=c*.13
i=c*.16
t=c+p+i
str(print("Costo de su comida: $",round(c,2),
      "Propina: $",round(p,2),
      "IVA: $",round(i,2),
      "Total a pagar: $",round(t,2),))
