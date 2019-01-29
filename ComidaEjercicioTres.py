#A01748632 Michel Antoine Dionne Gutierrez
# Este programa calculara el iva y la propina de una cierta comida
comida=float(input("Cual fue el total de la comida"))
iva=comida*.16
propina=comida*.13
print("EL subtotal es de %.2f"%comida)
print("El iva es de %.2"%iva)
print("La propina es de %.2f"%propina)
print("El total de todo es de %.2f"%comida+iva+propina)