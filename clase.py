# Autor: Roberto Emmanuel González Muñoz A01376803
# Elabora un algoritmo y escribe un programa que calcula
# el porcentaje de hombres y mujeres inscritos en una clase.


def main():
    mujeresInscritas = int(input("Mujeres Inscritas: "))
    hombresInscritos = int(input("Hombres inscritos: "))

    totalDeInscritos = mujeresInscritas + hombresInscritos
    porcentajeMujeres = mujeresInscritas * 100 / totalDeInscritos
    porcentajeHombres = hombresInscritos * 100 / totalDeInscritos
    print("Total Inscritos: %d" % totalDeInscritos)
    print("Porcentaje mujeres: %.1f" % porcentajeMujeres)
    print("Porcentaje hombres: %.1f" % porcentajeHombres)

main()