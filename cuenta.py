#Francisco Javier González Molina A01748636
#Algoritmo que calcula el costo total de la comida

subtotal= int (input("Inserte el precio total de los platillos: $"))

propina=subtotal*.13
iva=subtotal*.16
totalapagar=subtotal+iva+propina

print ("""Costo de la comida: $%.2f
Propina: $%.2f
IVA: $%.2f
Total a pagar: $%.2f"""% (subtotal,propina,iva,totalapagar))
