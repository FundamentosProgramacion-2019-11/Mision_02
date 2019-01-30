#Rafael Romero Bello A01747730
#Este programa te pone la cuenta total en un restaurante, incluyendo la propina y el iva.
sub=float(input("inserte la cuenta inicial:"))
iva=.16*sub
prop=.13*sub
total=(iva+prop)+sub
print("el total es de: %.2f"%(total),"pesos")

