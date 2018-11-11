#!/usr/bin/python


# Las funciones son variables que resumen código y pueden ser usador de forma repetida
# sin necesidad de escribir el código de nuevo varias veces, resumiendolo en una variable
# (Esto mantiene el ordenado el código)
# Así se define una función

def function():
	pass

def 							# Para definir una variable como función
function 						# Corresponde al nombre de la función
(parámetro1,parámetro2,...): 	# Corresponden al espacio donde pueden ir o no variables
pass							# Corresponde al código que se ejecutará

# Ejemplo de funciones

def sumar(a,b):
	resultado = a + b
	return resultado # Return corresponde al resultado final de la función que queremos retornar

return # Es una función especial que puede o no devolver un parámetro de una función

# En este ejemplo podemos ver que la función no retorna ningún parámetro ya que no lo necesita.
# Solo muestra el contenido de la variable a

def mostrar(a):
	print(a)

# Como nos hemos dado cuenta, las funciones reciven un valor. Este valor es un valor de referencia al
# valor original. Ejemplo

a = "hola" # Esta variable es el valor original
mostrar(a) # Esta a sigue siendo el valor original
# Ahora ¿Que hace mostrar?
#

def mostrar(valorRef): # Si nos fijamos mostrar al recivir un valor, se lo asocia a valorRef
	print(valorRef)	   # el cual corresponde al valor de referencia, ya que no cambia el valor
			           # original de la variable
# En el ejemplo anterior no se retornó nada. Las funciones en python siempre retornan algo, si
# no ponemos return, este retornara nulo pero aún asi ejecutara el codigo.
# Las funciones que no retornan nada se denominan SUBRUTINAS

# Las funciones en python pueden retornar mas de un valor. Ejemplo

def segundos(seg):
	hora = (seg/3600)
	minutos = (seg/60) % 60
	segundos = seg % 60
	return hora,minutos,segundos

h,m,s = variables(9999) 

