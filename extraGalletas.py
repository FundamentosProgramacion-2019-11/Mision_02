#Francisco Javier González Molina A01748636
#Cuanto de ingredientes uso para "x" cantidad de galletas

galletasdeseadas=int (input("¿Cuantas galletas deseas preparar? : "))

azucargalleta=(1*1.5)/48
mantequillagalleta= (1*1)/48
harinagalleta=(1*2.75)/48

azucarnecesaria=azucargalleta*galletasdeseadas
mantequillanecesaria=mantequillagalleta*galletasdeseadas
harinanecesaria=harinagalleta*galletasdeseadas

print ("""La porcion necesaria para tus galletas son: 

Cantidad de azúcar: %.2f
Cantidad de mantequilla: %.2f
Cantidad de harina: %.2f
"""%(azucarnecesaria,mantequillanecesaria,harinanecesaria))