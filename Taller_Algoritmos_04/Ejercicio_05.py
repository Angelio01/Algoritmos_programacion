"""
Entradas: ----

Salidas: El numero de terminos nesesarios para que la exprexión se acerque a 1000

Terminos --> int --> N
Sumatoria --> int --> B

"""
# Caja negra
N = 1
B = 0
while B != 1000:
    B = (((N**2) + 1)/N)
    if B < 1000: 
        print(N)
        N += 1
    else:
        N -= 1
        B = (((N**2) + 1)/N)
        break

# Salidas
print("\nPara que la sumatoria sea cercana a 1000 \nK tiene que tener valor de:",N)
print(f"El resultado de la sumatoria es {B}\n")


         
        
         
        