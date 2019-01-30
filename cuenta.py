#Autor:Itzel Yanabany Castro Becerril
#Costo total de la cuenta
cuenta=int(input("Costo de tu cuenta: "))
propina=cuenta*0.13
iva= cuenta*0.16
total=cuenta+propina+iva
print("Propina: %.2f"%(propina))
print("IVA: %.2f" % (iva))
print("Total a pagar: %.2f" % (total))

