#Autor: Yasmín Landaverde Nava, A01745725
#Descrpción: Este programa calcula los ingredientes necesarios para hornear cierta cantidad de galletas

cant = int(input("¿Cuántas galletas desea elaborar?: "))
az = (cant*1.5)/48
man = (cant*1)/48
har = (cant*2.75)/48
print("Para realizar", cant, "gatellas, va a necesitar: ")
print("Azúcar: ", "%.2f"% az, "tazas")
print("Mantequilla: ", "%.2f"% man, "tazas")
print("Harina: ", "%.2f"% har, "tazas")
