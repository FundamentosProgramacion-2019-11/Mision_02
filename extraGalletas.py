# Autor: Diego Raul Elizalde Uriarte, a01748756
#Descripcion: preguntar cuántas galletas se elaboraran e indique la cantidad de ingredientes que se requieren.

#Lecturas
ge = int(input("¿Cuantas galletas se elaboraran?: "))

#Calculo de resultados
ta = 1.5/48
tm = 1/48
th = 2.75/48
tat = ge*ta
tmt = ge*tm
tht = ge*th

#Imprimir resultados
print("Se necesitaran: ",tat," tazas de azucar")
print("Se necesitaran: ",tmt," tazas de mantequilla")
print("Se necesitaran: ",tht," tazas de harina")
