#Autor: Marianela Contreras Domínguez

#Descripción: Programa para indicarle al usuario la cantidad de harina, mantequilla y azúcar que necesita.


galletas = float(input ("Introduzca el número de galletas que quiere preparar:"))

azucar = (galletas *1.5)/48
mantequilla= (galletas*1)/48
harina = (galletas*2.75)/48

print("Necesitas:%.2f"% azucar,"tazas de azucar")
print("Necesitas:%.2f"% mantequilla,"tazas de mantequilla")
print("Necesitas:%.2f"% harina,"tazas de harina")


