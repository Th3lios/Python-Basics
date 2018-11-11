#!/usr/bin/python
# En python los arrays son esos tipos de cosas que no las necesitar usar si no sabes como o
# en que se podría usar. La mayoria de las veces, los arrays se utilizan en conjunto con codigo
# en lenguaje C.

# Listas
#	-Son flexibles (no se requiere redimensión de tramaño)
#	-Son heterogeneas (pueden almacenar ditintos tipos de datos)
#
# Arrays
#	-Son homogeneos (haceptan un tipo de dato)
#	-Son compactos en tamaño
#	-Son eficientes (en funcionalidad y velocidad)
#	-convenientes

# Los arrays son mas eficientes que las listas en algunos casos. Si necesitas alojar un array
# que sabes que no va a cambiar, entonces los arrays pueden ser mas rápidos y usan menos memoria
#
# Se recomienda la utilización de arrays en caso de utilizar alguna interface del lenguaje C o
# para una optimización de codigo

############################ LISTAS #######################################

# La lista es el tipo de dato mas versátil de python, el cual se puede escribir como elementos
# separados con comas (,) entre corcetes ([]).
# Lo importante de las listas es que soportan varios tipos de datos dentro de sus espacios.
# El primer valor de la lista parte con el indice 0

# Ejemplo de lista
lista = ['hola',23,'23',33]
# Valores |'hola'|23|'23'|33| 
# Indices |	0	 |1 | 2	 |3 |

## Creación de listas ##

# Así se crean las listas
lista = ['hola',23,'23',33]
lista1 = [1,2,3,4,5]
lista2 = ["a","b","c","d"]

print(lista) 			#esto muestra ['hola', 23, '23', 33]
print(lista[0]) 		#esto muestra hola
print(lista[0:2]) 		#esto muestra ['hola',23]. Muestra desde el elemento de indice 0 hasta el anterior al indice 2.
print(lista[:])  		#esto muestra ['hola',23,'23',33]
print(lista[0:]) 		#esto muestra ['hola',23,'23',33]
print(lista[:4]) 		#esto muestra ['hola',23,'23',33]
#No poner un valor antes y después de los 2 puntos (:) hace que tome desde el primer valor hasta el último
#(0:) desde 0 al último
#(:4) desde el inicio hasta antes del indice 4 (el 3)
#(:) de inicio a fin
#########################

### Actualizar lista ###
lista[0] = 'adios'
print(lista) 		    #['adios',23,'23',33]
#Los valores se sobre-escriben de forma directa, igual que definir variables.
########################

## Eliminación listas ##
## Forma 1 ##
del lista[0]
print(lista) 			#Esto muestra [23,'23',33]. Elimina un desde un indice en específico

## Forma 2 ##
lista2= [23,33,23,33,23,33]
lista2.remove(33)
print(lista2) 			#Esto muestra [23,23,33,23,33]. Significa que solo borra la primera ocurrencia
########################

## Añadir a la lista ##

lista.append("ola")
print(lista)			#Esto muestra ['hola', 23, '23', 33,'ola']. Append añade al final de la lista

#######################

## Otros comandos ##
len(lista) 				#Entrega el tamaño de la lista
['a'!]*4				#Crea una lista con 4 a's ['a','a','a','a']
lista.count(obj) 		#Entrega la cantidad de veces que un valor se repite dentro de la lista
lista.extend(lista2)	#Lista se fusiona con lista2. Ahora lista además de tener sus propios parámetros también tiene los de lista2
fusion = lista+lista2 	#En este caso la variable fusion sería lo mismo que lo de arriba
lista.index(obj) 		#Entrega el indice de la primera ocurrencia del obj que se busca en la lista
lista.insert(index,obj) #Se inserta en lista un parámetro en la posicion que se quiera, moviendo el valor que ocupa es espacio
#un espacio a la derecha (lo que implica que mueve todos los valores siguientes un espacio a la derecha tambien)
#Ejemplo: lista = ['hola', 23, '23', 33]; lista.insert(1,'ola'); print(lista) #esto muestra ['hola','ola',23,'23',33]
lista.pop(indice) 		#Elimina el valor con ese indice y lo retorna
lista.reverse() 		#Esto voltea la lista
lista.sort() 			#Ordena la lista según el valor de la variable en la tabla ASCII
#Ejemplo: lista = ["a","c","z","b"]; lista.sort(); print(lista) #esto muestra ["a","b","c","z"]

####################

#################################################################################  



