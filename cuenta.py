#Autor: Eric Andrés Jardón Chao, A01376748
#Descripción: Programa que calcula el costo total de la cuenta en un restaurante, tomando el subtotal, la propina, y el IVA.

subtotal=int(input("Teclea aquí el costo de la comida en MXN: "))
propina=subtotal*0.16
iva=subtotal*0.13
total=subtotal+propina+iva

print("El costo subtotal de la cuenta es de: $",subtotal)
print("El costo de la propina es de: $",propina)
print("El costo del IVA sobre el subtotal es de: $",iva)
print("El costo TOTAL de la cuenta es de $ %.2f" %(total))

#Fin del programa
