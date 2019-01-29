# Autor: Roberto Emmanuel González Muñoz A01376803
# Elabora un algoritmo y escribe un programa
# que muestre en la pantalla la siguiente información:
# Nombre completo, matrículo, carrera, escuela de procedencia y descripción.


def imprimir(n,m,c,e,d):
    print("Nombre: ")
    print(n)
    print("___________________________________________________________________________")
    print("Matrícula: ")
    print(m)
    print("___________________________________________________________________________")
    print("Carrera: ")
    print(c)
    print("___________________________________________________________________________")
    print("Escuela de procedencia: ")
    print(e)
    print("___________________________________________________________________________")
    print("Descripción: ")
    print(d)
    print("___________________________________________________________________________")



def main():
    nombre = "Roberto Emmanuel González Muñoz"
    matricula = "A01376803"
    carrera = "ISDR"
    escuelaProcedencia = "PrepaTec, programa Multicultural"
    description = "Tengo 20 años, una de mis pasiones es la musica y me intriga mucho la fotografía y la filosofía."

    imprimir(nombre,matricula,carrera,escuelaProcedencia,description)

main()