"""
Entradas: ----

Salidas: El numero de terminos nesesarios para que la exprexión se acerque a 1000

Terminos --> int --> N
Sumatoria --> int --> B

"""
# Caja negra
e = 1
B = 0
N = 0
while True:
    d = ((e**2)+1)/e
    B = B + d
    N += 1
    if B > 1000:
        d = ((e**2)+1)/e
        B = B - d
        N -= 1 
        break
    else: 
        e += 1
        print(N)
# Salidas
print("\nEl numero de terminos necesarios es:",N)
print("El resultado de la sumatoria cuando N es:",N,"\nEs:",B,"\n")


         
        
         
        