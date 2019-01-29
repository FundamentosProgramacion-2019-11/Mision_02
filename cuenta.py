# Autor: Roberto Emmanuel González Muñoz A01376803
# Elabora un algoritmo y escribe un programa
# que calcula el costo total de una comida en un restaurante.


def main():
    costoComida = float(input("Costo de su comida: "))
    propina = costoComida * 13/100
    IVA = costoComida * 16/100
    totalaPagar = costoComida + propina + IVA
    print("Propina: $%.2f" % propina)
    print("IVA: $%.2f" % IVA)
    print("Total a pagar: $%.2f" % totalaPagar)
    print("____________________________________")

main()