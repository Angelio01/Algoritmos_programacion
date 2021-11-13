frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
      

lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
for i in frutas:
      lista_frutas.append(i)
# print(lista_frutas)

 
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in numeros:
      lista_numeros.append(i)
# print(lista_numeros)


#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas: lista(str) --> list --> lista_frutas 
          caracter --> str --> caracter
Salidas: lista(str) --> list --> lista_frutas con los elementos sin un caracter
"""
"""
def eliminar_un_caracter_de_toda_la_lista(lista: list, caracter:  str):
      listan = []
      for i in lista:
        a = i.replace(caracter, "")
        listan.append(a)
      return listan
if __name__ == "__main__":
  As = eliminar_un_caracter_de_toda_la_lista(lista_frutas, "\n")
  print(As)
"""


#Realizar una funcion que retorne la copia de una funcion que pasa por parametro 
"""
Entradas: lista --> list --> lista_frutas
Salidas:  copia de la lista --> list --> listo
"""
"""
def copia_lista(lista: list):
  return lista.copy() 
if __name__ == "__main__":
    As = copia_lista(lista_frutas)
    print(As,"\n")
    print(lista_frutas,"\n")
"""


#Realizar una funcion que retorne una lista de numeros enteros   
"""
Entradas: lista --> list --> listo
Salidas:lista --> list --> As lista con solo numeros enteros y pares
"""  
"""
def numeros_pares(lista: list):
      lista3 = []
      for i in range(0,len(lista)-1):
                if float(lista[i]) % 2 == 0:
                    lista3.append(lista[i])
      return lista3#RetornaUnaLista
if __name__ == "__main__":
  As = numeros_pares(lista_numeros)
  print(As)
"""


#Realizar una funcion que elimine un elemento de una lista
"""
Entradas: elemento --> str --> elemento
          lista --> list --> lista_frutas
Salidas: lista --> list --> As
"""  
"""
def elimina_elemento_lista(lista: list,elemento: str):
      lista_0 = []
      for i in lista:
            if i == elemento:
                  pass
            else: 
              lista_0.append(i)
      return lista_0

if __name__ == "__main__":
      As = elimina_elemento_lista(lista_frutas, "Arandano\n")
      print(As)   
"""


#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas: lista --> list --> lista_frutas
          letra --> str --> letra
Salidas: lista --> list --> lista_frutas2
"""  
"""
def letra(lista: list,letra: str):
    listaq = []
    lista_frutas2 = []
    for i in lista:
          if i[0] == letra:
                lista_frutas2.append(i)
          else: 
            listaq.append(i)
    lista_frutas2.extend(listaq)
    return lista_frutas2
if __name__ == "__main__":
    As = letra(lista_frutas, "C")
    print(As)
"""    


#Realizar una funcion que retorne el tamano de una lista   
"""
Entradas:lista --> list --> lista_numeros
Salidas: tamaño --> int --> tamaño
"""  
"""
def tamano_lista(lista: list):
    return len(lista)
if __name__ == "__main__":
      tamaño = tamano_lista(lista_numeros)
      print(tamaño)
"""  
        

#Retorna el tamano de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:lista --> list --> lista_numeros
Salidas: tamaño --> int --> tamaño
         tipo de dato --> str --> tipo
"""  
"""
def informacion_lista(lista: list):
      tamaño = len(lista)
      tipo = type(lista[0])
      return tamaño, tipo
if __name__ == "__main__":
  print(informacion_lista(lista_frutas))
"""


#Retornar una lista con los numero negativos  
"""
Entradas:lista(float) --> list --> Listas_numeros
Salidas: As --> list --> As
"""  
"""
def numeros_negativos(lista):
      l0 = []
      for i in lista: 
        l0.append(int(float(i)))
      l1 = l0.copy()
      for i in l0: 
        if i < 0:
            l0 = l0
        elif i >= 0: 
          l1.remove(i)
        else: 
          l0 = l0
      return l1
if __name__ == "__main__":
      print(numeros_negativos(lista_numeros))
"""
  
  
#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
"""
def posicion_elemento(elemento):
      n = 0
      for i in lista_frutas:
            if elemento == i:
                  n +=1
                  break
            else: 
              n+= 1
      return n
if __name__ == "__main__":
  print(posicion_elemento("Zarzamora\n"))
"""


#realizar una funcion que agregue al final de archivo frutas una fruta
"""
def frutas1(elemento):
      A = open("frutas.txt","a")
      A.write(f"\n{elemento}")
      A.close()
      pass
if __name__ == "__main__":
      frutas1("Zipote")
"""


#Realizar una funcion que cuente el numero de veces que se repite un elemento  
"""
def repetir(elemento):
      veces = 0
      for i in lista_numeros:
            if i == elemento:
                  veces += 1
      return veces
if __name__ == "__main__":
     print(repetir("-2\n"))
"""

"""
if __name__ == "__main__":
  lista=[1,2,3,4,4]
  copy=copia_lista(lista)
  print(copy)
"""
frutas.close()
numeros.close()