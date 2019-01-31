# Autor: Luis Adrian Carmona Villalobos, A01748395
# Descripcion: Progama que calcula la cuenta
# Escribe tu programa después de esta línea.
Total = int(input("total de su comida"))
propina= Total*.87
IVA = Total*.84
TotalReal = Total+propina+IVA
print("Propina: ", propina)
print("IVA: ", IVA)
print("su Total fue: ", TotalReal)
