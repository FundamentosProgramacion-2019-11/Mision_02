#Víctor Iván Morales Ramos a01377601
#analisis: Crear un algoritmo que calcule el precio total de una comida, recibiendo datos bases

t = float(input("¿Cuál es el total de la comida en MXN?: "))

p = t * 0.13
iva = t * 0.16
st = t
tf = p + iva + st

print("Subtotal: " , st)
print("Propina: " , p)
print("Importe al valor agregado (IVA): " , iva)
print("Total: " , tf)

