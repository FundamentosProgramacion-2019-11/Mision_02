# Autor: Luis Fernando Duran Castillo, A01745792
# Descripcion: precio final de la comida

# Escribe tu programa después de esta línea.

p= int(input("Ponga el precio de la comida que pidio: "))

pr=p*.13

iva=p*.16

t=p+pr+iva

print("su subtotal es de: %.2f " % (p))

print("la propina es de: %.2f " % (pr))

print("el iva es de: %.2f " % (iva))

print("el total a pagar es de: %.2f " % (t))