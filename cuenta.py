# Autor: Sofía Trujillo Vargas A01747320
# Se dará la cuenta total de una comida incluyendo el IVA y la propina.

s=float(input("¿Cuál es el subtotal de tu comida?: "))
i=s*.16
p=s*.13
t=s+i+p
print("Tu subtotal es igual a: ",s)
print("Tu propina es de: ",p)
print("El IVA es de: ",i)
print("Tu total es de: ",t)
