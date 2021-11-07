archivo = open('paises.txt', 'r')

""""""" NOTA: RECORDAR UTILIZAR EL.TXT QUE TIENE LOS PAISES SIN SIGNOS DE PUNTUACIÓN """""""

#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogota\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la latra M  

"""
lista=[]
ciudad=[]
n = 0
print()
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="M"):
    n += 1
print("La cantidad de ciudades que inician con M es de",n,"\n")
"""

#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
print("\nPaises que empiezan con U:\n")
lista=[]
paises=[]
lista1=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  b=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
  for e in range(b+2,len(i)):
    lista1.append(i[e])
  b="".join(lista1)
  ciudad.append(b)
  lista1=[]
for i in paises:
  if(i[0]=="U"):
    print(i)
print("\nCiudades que empiezan con U:\n")
for i in ciudad:
  if(i[0]=="U"):
    print(i, end = "") 
print()
"""
#Cuente e imprima cuantos paises que hay en el archivo
"""
n = 0
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  n += 1
  print(f"{n}. {a}")
  lista=[]
print("\nLa cantidad de paises es:",n,"\n")
"""

#Busque e imprima la ciudad de Singapur
"""
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(a[0] == "S" and a[7] == "r"):
    B = a.index(":")
    lista = []
    break
  lista = []
for i in range(B+2,len(a)):
  lista.append(a[i])
a ="".join(lista)
print(f"\n{a}")
"""

#Busque e imprima el pais de Venezuela y su capital
"""
lista=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  if(a[0] == "V" and a[8] == "a"):
    print(f"\n{a}")
    lista = []
    break
  lista = []
"""

#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
lista=[]
paises=[]
for i in archivo:
  a=len(i)
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
n = 0
print()
for i in paises:
  if(i[0]=="E"):
    a=i.index(":")
    n += 1
    for r in range(a+2,len(i)):
      lista.append(i[r])
    a="".join(lista)
    print(f"{n}. {a}", end="")
  lista=[]
print("La cantidad de ciudades cuyo país empieza por la letra E es:",n,"\n")
"""

#Busque e imprima la Capiltal de Colombia

"""
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(a=="Colombia: Bogota\n"):
    B = a.index(":")
    lista = []
    break
  lista = []
for i in range(B+2,len(a)):
  lista.append(a[i])
a ="".join(lista)
print(f"\n{a}")
"""

#imprima la posicion del pais de Uganda
"""
lista=[]
n = 0
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  n += 1
  if(a[0]=="U" and a[4]=="d"):
    B = a.index(":")
    lista = []
    break
  lista = []
print(f"\nLa posición de Uganda es {n}\n")
"""

#imprima la posicion del pais de Mexico
"""
lista=[]
n = 0
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  n += 1
  if(a[0]=="M" and a[2]=="x"):
    B = a.index(":")
    lista = []
    break
  lista = []
print(f"\nLa posición de Mexico es: {n}\n")
"""

"""
El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de paises.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
"""

"""
lista = []
for i in archivo:
    lista.append(i)
archivo1 = open("paises.txt","w")
for i in lista:
      if (i == "Madagascar: rey julien\n"):
            archivo1.write("Madagascar: Antananarivo\n")
      else:
            archivo1.write(i)
archivo1.close()
"""

#Agregue un pais que no este en la lista 
"""
archivo2 = open("paises.txt","a")
archivo2.write("\nZuolandia: Zuo")
archivo2.close()
"""
archivo.close()