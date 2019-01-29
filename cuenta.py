#Autor: Martha Margarita Dorantes Cordero 
#imprime: costo comidas



costo = float(input("Costo de su comida: $"))
print('Propina: $%.2f'%(costo*.13))
print('IVA: $%.2f'%(costo*.16))
print('Total a pagar: $%.2f'%(costo+costo*.13+costo*.16))
