# Autor: YadiraFuentesCalderón, A01745235
# Descripcion: Calcular los ingredientes que se necesitan para cierto numero de galletas

numero_de_galletas = int (input ("¿Cuantas galletas deseas elaborar?"))

#Para 48 galletas se requieren 1.5 tazas de azúcar, 1 taza de mantequilla, 2.75 tazas de harina.

tazas_de_azucar = (numero_de_galletas*1.5)/48
tazas_de_mantequilla = numero_de_galletas/48
tazas_de_harina = (numero_de_galletas*2.75)/48

print ("Se necesitan ", tazas_de_azucar, " tazas de azucar")
print ("Se necesitan ", tazas_de_mantequilla, " tazas de mantequilla")
print ("Se necesitan ", tazas_de_harina, " tazas de harina")