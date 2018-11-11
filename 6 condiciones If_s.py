#!/usr/bin/python
#Python no tiene la función de switch o case, pero se puede emular con lo elif
#En python al igual que en otros lenguajes, existen las condiciones.
# Pass corresponde a lo que uno quiera que suceda, pass es una sentencia que no ejecuta nada
if () :
	pass
	#aquí el if sigue corriendo
#desde aquí ya no corre el if
if :
	pass
	#aquí el if sigue corriendo
#desde aquí ya no corre el if

#El if puede hacerse de las 2 maneras, con y sin parentesis.
#Hay que tener en cuenta que python no ocupa llaves ({}) como en otros lenguejes para abrir y
# cerrar sus condiciones, por lo que hay que tener mucho cuidado con las indencaciones, ya que
# python reconoce el cierre en donde termina su indentación



#Significado			Símbolo Matemático		  	  Python Symbols
#Menor que					    <							<
#Mayor que					    >							>
#Menor o igual que				≤							<=
#Mayor o igual queue			≥							>=
#Igual que						=							==
#No igual que					≠							!=

## Tipos de If ##

################################################################################################
# Pass corresponde a lo que uno quiera que suceda, pass es una sentencia que no ejecuta nada
# que podría ir ahí
if 3 in [1,2,3]: #Si el 3 está dentro de la lista entonces ocurre pass
	pass
else: 			 #Si no ocurre lo de arriba entonces ocurre este pass
	pass

################################################################################################

if 3 == 3: 		 #Si 3 es igual a 3 entonces ocurre pass, recordar que en las condiciones se usa == para ver si son iguales
	pass
else: 			 #Si no ocurre lo de arriba entonces ocurre este pass
	pass

################################################################################################
	
if lista == lista1: #Si los valores de lista son iguales a los de lista1 entonces ocurre pass
	pass
else: 		  		#Si no ocurre lo de arriba entonces ocurre este pass
	pass

################################################################################################

if 4<3: #Si 4 es menor a 3 ocurre pas
	pass
elif 4>=3:		  #Entonces si 4 es mayor o igual a 3 ocurre este pass. elif es como un else pero le puedes agregar una condición
	pass
else: 			  #Si no ocurrió nada de lo de arriba entonces ocurre este pass
	pass

################################################################################################

#Esto se llama anidación, se anidan 2 if
if 2==2:	   	  #Si 2 es igual a 2 ocurre lo de abajo
	if 3==3:	  #Si 3 es igual a 3 ocurre pass
		pass

################################################################################################

var = "asdasd"

#Primera opción
if var.isalpha(): #si var.isalpha()(si var tiene solo letras) es true se hace pass
	pass

#En este caso no comparamos nada dentro del if, esto se debe a que por default if compara con
# con false. Lo de arriba es igual a esto

if var.isalpha() != False: # Esto dice lo siguiente: Si VERDADERO es DISTINTO de FALSO se hace pass
	pass 				   # Siempre debería de escribirse como la primera opción

################################################################################################

if not var.isalpha(): 	   #En este caso usamos el Not para negar el TRUE y hacerlo FALSE
	pass
else:
	pass


#En este caso comparamos el TRUE negado (FALSE) con el FALSE
if False != False 		   #Aqui preguntamos si FALSO es DISTINTO de FALSO
	pass 				   #Como falso no es distinto de falso, esta linea no se ejecuta
else:
	pass 				   #En cambio esta sí, ya que si no s ejecuta lo de arriba, instantaneamente se ejecuta este

################################################################################################

#En los if tambien podemos hacer que cumplas mas de una condicion para ejecutar codigo

#Esta and o & que hace que se tengan que cumplir si o si ambas condiciones para ejecutar codigo

var = "asd"
var1 = " "


if var.isalpha() and var1.isalpha():
	print("Ambos tienen solo texto")
else:
	print("Uno tiene texto y el otro espacios en blanco") #Se ejecuta este

#Mismo codigo pero con &

if var.isalpha() & var1.isalpha():
	print("Ambos tienen solo texto")
else:
	print("Uno tiene texto y el otro espacios en blanco") #Se ejecuta este



#En este ejemplo vamos a negar var1.isalpha, ahora ambos van a ser TRUE

var = "asd"
var1 = " "


if var.isalpha() and not var1.isalpha():
	print("Ambos tienen solo texto") #Se ejecuta este
else:
	print("Uno tiene texto y el otro espacios en blanco")

#Mismo codigo pero con &

if var.isalpha() & not var1.isalpha():
	print("Ambos tienen solo texto") #Se ejecuta este
else:
	print("Uno tiene texto y el otro espacios en blanco")

## Descripcion muy gráfica de lo que está arriba

#	  (TRUE    != FALSE)  AND ((NOT(FALSE) = TRUE) != FALSE)
if var.isalpha() != False and not var1.isalpha() != False:
	print("Ambos tienen solo texto") # Como ambos son verdaderos, se ejecuta este
else:
	print("Uno tiene texto y el otro espacios en blanco")


################################################################################################

#Esta or o | que hace que con que una se cumple va a ejecupar el codigo


var = "asd"
var1 = " "
#Recorar que s.isalpha() retorna true si el string solo tiene letras

if var.isalpha() or var1.isalpha():
	print("Por lo menos uno tiene solo texto") #Se ejecuta este
else:
	print("ambos tienen espacios")

#Mismo codigo pero con |

if var.isalpha() | var1.isalpha():
	print("Por lo menos uno tiene solo texto") #Se ejecuta este
else:
	print("ambos tienen espacios")


################################################################################################
################################################################################################
################################################################################################
################################################################################################
