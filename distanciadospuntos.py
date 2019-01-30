#Francisco Javier González Moluna A01748636
#Calcular la distancia de dos puntos

print ("Primer Punto")
x1=int (input("Dame coordenada de X1: "))
y1=int (input("Dame coordenada de Y1: "))

print("Segundo Punto")
x2=int (input("Dame coordenada de X2: "))
y2=int (input("Dame coordenada de Y2: "))

distancia= (((x2-x1)**2)+((y2-y1)**2))**0.5

print ("La distancia es: %.3f"%(distancia))