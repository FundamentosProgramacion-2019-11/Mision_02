# Autor: tu Michel Antoine Dionne Gutierrez, A01748632
# Descripcion: Nos determinara la distancia y la hora para ciertos problemas de velocidad.

# Escribe tu programa después de esta línea.
v=int(input("Dame la velocidad en km/h"))
print("La distancia dentro de 6 horas es %.1f"%(v*6))
print("La distancia dentro de 3.5 horas es %.1f"%(v*3.5))
horas=485/v
print("El tiempo es de %.1f"%horas,"y el tiempo en minutos es de %.1f"%horas*60)
