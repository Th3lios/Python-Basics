#!/usr/bin/python

#En python tenemos 2 tipos de loos
#While 
#For


########### WHILE LOOP #################
#Recordad que pass es una sentencia que no ejecuta nada
#Así se define un while, al igual que el if el parentesis es opcional

while ():
	pass

while :
	pass

#Un while (mientras) ejecuta un codigo (en este caso el pass) repetitivamente
#Ejemplo

i = 0 				#definimos i como 0

while i <= 10: 		#Mientras que "i" sea "menor o igual" a "10" que ejecute el codigo de abajo
	print("hola") 	#Se imprime hola
	i = i + 1 		# i aumenta en 1

#Va a llegar un punto en que i va a aumentar tanto que va a superar el 10 y en ese instante
#el while se detendrá

#Al igual que el if el while tambien tiene por default el !=False

while ()!=False:
	pass

#Esto significa que si hacemos lo siguiente

while True:
	pass

#El loop será infinito, ya que no hay ninguna condicion que lo detenga
#Debido a esto podemos anidarle un if y detenerlo con alguna condicion. Ejemplo

i = 0
while True:		#Mientras True sea distinto de False
	if i == 10:	#Si i es igual a 10
		break 	#Romper el ciclo (Su explicación mas abajo)
	else:		#Sino
		i+=1 	#Incrementar i en 1. Esto es la abreviacion de i = i + 1
				# i+=1 es distinto de i=+1
				# en i+=1, i aumenta en 1 (i = i + 1)
				# en la segunta, i = (+1), significa que se le asigna el unario "+" a 1
				# Mini ej i=+(-1) / i seria igual a -1, porque + por - es igual a menos

#En este ejemplo conocimos el BREAK, este comando especial detiene cualquier ejecución, en
#este caso la ejecución del while

#Hay otro comando que se llama CONTINUE. Este comando lo que hace es saltarse una ejecución
#sin detener la ejecucion por completo como el break. En el caso del while, se saltaría una vuelta

i = 0
while True:				#Mientras True sea distinto de False
	if i < 10:			#Si i es menor a 10
		i+=1			#i aumenta en 1
		continue 		#Saltarse esta vuelta (implica que lo de abajo no se ejecutará aún)
else:					#El while también puede tener else (se comporta igual que el del if)
	print("Ya terminó") #Cuando i sea mayor o igual a 10, se imprimirá Ya terminó
	break 				#Se rompe el ciclo while
	
########################################

################## FOR LOOP #######################

#Un for se define asi:

for x in xrange(1,10): # x funciona como un auxiliar que recore el rango o lista, xrange genera su propio tipo de dato xrange
	pass               # Ejecuta esta sentencia según el recorrido de x

#Ejemplo

for x in range(0,10):  # range retorna una lista de los parametros que se le da range(0,n) e imprime hasta n-1
	print(x)		   # Esto imprime x en cada ciclo del for 0,1,2,3,4,5,6,7,8,9

#El for igual tiene un else

for x in xrange(1,10): 
	pass
else:				   # Trabaja igual que el del while
	pass

###################################################