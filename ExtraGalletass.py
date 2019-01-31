#Víctor Iván Morales Ramos A01377601
#analisis:  Crear un algoritmo que calcule todos los datos requeridos individualmente.

gd = float(input("Cuantas galletas vas a preparar: "))

ag = (1 * 1.5)/48
mg = (1 * 1)/48
hg = (1 * 2.750)/48

an = ag * gd
mn = mg * gd
hn = hg * gd

print("""La porcion necesaria para tus galletas son: 
Tasas de azúcar: %.2f
Tasas de mantequilla: %.2f
Tasas de harina: %.2f
"""%(an, mn, hn))
