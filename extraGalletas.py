# Jose Luis Mata Lomelí
# A01377205
# Programa que indique la cantidad de indegrirntes que se requieren segun la cantidad de galletas que quiera el usuario

# Sabemos que para 48 galletas se necesita:
# 1.5 tazas de azucar,
# 1 taza de mantequilla y
# 2.75 tazas de harina

#Entrada = Cantidad de Galletas
cantidadGalletas = int(input("Teclea la cantidad deseada de galletas a elaborar: "))

# E/S = Regla de 3
azu = (cantidadGalletas * 1.5) / 48
mante = (cantidadGalletas * 1) / 48
hari = (cantidadGalletas * 2.75) / 48

#Salida = Resultados
print("Galletas: ", cantidadGalletas)
print("Azucar: %.2f" % azu, "taza(s)")
print("Mantequilla: %.2f" % mante, "taza(s)")
print("Harina: %.2f" % hari , "taza(s)")
