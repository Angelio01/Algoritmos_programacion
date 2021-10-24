"""
Entradas: 3 valores flotantes 

Lote naranjas --> float --> X 
Decena de naranajas --> float --> Y 
Obtenido --> float --> K 

Salidas: 1 valor flotante 

pocentaje --> float --> P

"""
# Entradas 
X=int(input("Dimé el precio del lote de naranjas "))
Y=float(input("Dimé el precio por decena de las naranjas "))
K=float(input("Dimé el dinero de la venta de naranjas "))
# Caja negra
Dec = (X/12)
G = Y * Dec
ganancia = K - G
P = (ganancia / G)*100
# Salida
print(f"El porcentaje es de {P}%")