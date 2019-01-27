#Autor: Guillermo De Anda Casas , A01375892
#Código que calcula el total de tazas de azúcar, mantequilla y harina para cierto número de galletas.

g = int(input("¿Cuántas galletas quiere preparar?: "))

ta = (g*1.5)/48
tm = (g*1)/48
th = (g*2.75)/48

print("Tazas de azúcar necesarias: ","{:.2f}".format(ta))
print("Tazas de mantequilla necesarias: ","{:.2f}".format(tm))
print("Tazas de harina necesarias: ","{:.2f}".format(th))
