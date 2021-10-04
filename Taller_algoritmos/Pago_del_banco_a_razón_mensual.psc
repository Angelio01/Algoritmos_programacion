
Algoritmo Pago_del_banco_a_razón_mensual
	Escribir "Hola cuanto desesas de positar en el banco"
	Leer dato_1
	Escribir "¿Qué deseas saber? 1 = mi dinero 2 = mi dinero en algun mes"
	Leer Accion_1
	Si Accion_1== 1 Entonces
		Escribir "Tu dinero es:" dato_1
	SiNo
		Escribir "¿Cuantos meses vas a depositar el dinero?"
		Leer dato_2
		dato_3<-0.02
		dato_4<-(dato_3*dato_1)
		dato_5<-(dato_4*dato_2)+dato_1
		Escribir "tu dinero sera " dato_5
	Fin Si	
	
FinAlgoritmo
