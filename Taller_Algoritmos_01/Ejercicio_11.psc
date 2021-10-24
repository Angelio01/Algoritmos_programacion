Algoritmo Nota_final
	Escribir "¿Cuanto sacaste en tu primer parcial?"
	Leer n_0
	Escribir "¿Cuanto sacaste en el segundo parcial?"
	Leer n_1
	Escribir "¿Cuanto Sacaste en el tercer parcial?"
	Leer n_2
	parciales = ((n_0+n_1+n_2)/3)*.55
	Escribir "¿Cuanto sacaste en el examen final?"
	Leer Ex_0
	examenf = Ex_0*.30
	Escribir "¿Cuanto sacaste en tu trabajo final?"
	Leer work 
	trabajof = work*.15
	Notaf = parciales+examenf+trabajof
	Escribir "tu nota final es " Notaf
FinAlgoritmo
