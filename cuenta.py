# Autor: Karla Ximena Rueda Ruiz, A01745943
# Descripcion: Cálculo de total a pagar de una comida en un restaurante, incluyenndo propina e IVA.

# Escribe tu programa después de esta línea.

#ct=costo total
#pro=propina
#iva=iva
#tot=total a pagar

ct = int(input("Costo de su comida: "))

pro = (.13*ct)
print("Propina:", pro)

iva= (.16*ct)

tot= (ct+pro+iva)
print("Total a pagar:", tot) 
