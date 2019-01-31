# Autor: José Isidro Sánchez Vázquez, A01748144
# Descripcion: Calculador de distancia recorrida en un vehiculo

# Escribe tu programa después de esta línea.
#v=d/t

v= int(input("Dame la velocidad del vehiculo en Km/h:"))
t=6
d=v*t
print("La distancia recorrida en 6h con la velocidad  ingresada es:",d,"Km")
t2=3.5
d=v*t2
print("La distancia recorrida en 3.5h con la velocidad ingresada es:",float(d),"Km")
d=485
t=d/v
print("El tiempo que tardo en recorrer 485Km a la velocidad ingresada es:%.2f"%(t),"h")
