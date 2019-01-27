# Autor: tu Michel Antoine Dionne Gutierrez, A01748632
# Descripcion: Nos determinara la distancia y la hora para ciertos problemas de velocidad.

# Escribe tu programa después de esta línea.
v=int(input("Dame la velocidad en km/h"))
print("La distancia dentro de 6 horas es ",(v*6))
print("La distancia dentro de 3.5 horas es ",(v*3.5))
horas=485/v
print("El tiempo es de ",horas,"y el tiempo en minutos es de",horas*60)
