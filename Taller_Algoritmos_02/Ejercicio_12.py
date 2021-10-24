"""
Entradas: 11 valores flotantes entre notas de tareas y examentes finales

Examen Matematicas --> float --> exM
Nota 1 matematicas --> float --> M1 
Nota 2 matematicas --> float --> M2 
Nota 3 matematicas --> float --> M3 

Examen Física --> float --> exF
Nota 1 física --> float --> F1
Nota 2 física --> float --> F2 

Examen Química --> float --> exQ
Nota 1 química --> float --> Q1 
Nota 2 química --> float --> Q2 
Nota 3 química --> float --> Q3 

Salidas: 4 valores flotantes correspondientes a la nota de cada asignatura, y al promedio general 

Nota en matematicas --> float --> Matematicas 
Nota en Física --> float --> Física 
Nota en Química --> float --> Química 
Promedio genetal --> float --> Prom

"""

# Entradas
exM = float(input("\nDime la nota de tu examen final de Matemáticas ")) 
M1 = float(input("\nDime las notas de tus 3 tareas de Matemáticas\n"))
M2 = float(input()) 
M3 = float(input())
exF = float(input("\nDime la nota de tu examen final de Física ")) 
F1 = float(input("\nDime las notas de tus 2 tareas de Física\n"))
F2 = float(input()) 
exQ = float(input("\nDime la nota de tu examen final de Química ")) 
Q1 = float(input("\nDime las notas de tus 3 tareas de Química\n"))
Q2 = float(input()) 
Q3 = float(input())

# Caja negra
Matematicas = (exM * 0.90) + ((M1+M2+M3)/3)*0.10
Física = (exF * 0.80) + ((F1+F2)/2)*0.20
Química = (exQ * 0.85) + ((Q1+Q2+Q3)/3)*0.15
Prom = (Matematicas + Física + Química)/3

# Salida	
print("\nEn Matematicas tu nota es de: ",Matematicas,"\nen Física tu nota es de: ",Física,"\n en Química tu nota es de: ",Química,"\n Y tu promedio general en",Prom)
	