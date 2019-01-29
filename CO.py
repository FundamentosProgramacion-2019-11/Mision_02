#Sofía Trujillo Vargas
#Sacar las x del problema

a=int(input("Dame el coeficiente de a: "))
b=int(input("Dame el coeficiente de b: "))
c=int(input("Dame el coeficiente de c: "))

x1=(-b + (b*b-4*a*c)**0.5)/(2*a)
x2=(-b - (b*b-4*a*c)**0.5)/(2*a)

print("x1 =%.3f"%(x1))
print("x2 =%.3f"%(x2))