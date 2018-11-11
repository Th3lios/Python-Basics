#!/usr/bin/python

# Trabajar con módulos es útil para mantener un programa ordenado y además para la reutilización de código más
# sencilla

# Para utilizar un Módulo hay que utilizar "import"

import nombreMódulo



################################ IMAGINA QUE ESTE ES OTRO ARCHIVO ###### NBRE DEL ARCHIVO : MODULO.py  ################

def suma():
	pass

def resta():
	pass

def multiplicación():
	pass

def división():
	pass

#######################################################################################################################


# Ahora si queremos utilizar esas funciones que estan en otro archivo llamado modulo hay que usar import

import modulo

# Ahora para usar las funciones utilizamos la nomeclatura del punto

modulo.suma()
modulo.resta()
modulo.multiplicación()
modulo.división()

# Cuando el código es mas extenso, esta forma se vuelve poco eficiente, por lo que existe otra manera de utilizar este modulo
# y es usando "from"

from modulo import suma

# Ahora podemos usar la funcion de forma directa

suma()

# De esta forma importamos la función suma del archivo modulo. Así se hace con todas las funciones.
# Si quieres importar todas las funciones de una sola vez, se hace lo siguiente

from modulo import * # El asterisco significa "todo"

suma()
resta()
multiplicación()
división()

# Como vez, ya no hay que poner modulo detrás de cada función
# Con ese import *, importamos todas las funciones de modulo (suma,resta,división,multiplicación)

# ¿Por que no utilizar siempre el asterisco?
# porque al utilizar el asterisco estamos cargando todas las funciones de un módulo y a veces esas funciones
# son muy extensas y ocupan mucho espacio en memoria, haciendo lento el programa. Entonces cuando un programa
# muy grande utiliza * lo transforma en un programa mas lento, debido a esto es mejor cargar la función exacta que
# se va a utilizar

# Los módulos a parte de almacenar funciones, pueden almacenar Clases , variables , etc

############################################ IMAGINA QUE ESTE ES OTRO ARCHIVO ### NOMBRE DE ARCHIVO: MODULO2.py #############

class Persona():
	def __init__(self, nombre,apellido,edad):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad

class Madre(Persona):
	def __init__(self,nombre,apellido,edad):
		super().__init__(nombre,apellido,edad)

	def crearHijo(self):
		nombre = input()
		edad = 0
		hijo = Hijo(nombre,self.apellido,edad)
		return hijo

class Hijo(Persona):
	def __init__(self,nombre,apellido,edad):
		super().__init__(nombre,apellido,edad)

		

############################################################################################################################# 

from modulo2 import *

p1 = Persona("Elias","Araya Diaz",22)
p2 = Madre("Adriana","Diaz",0)
p3 = Hijo("Pablo","Araya Diaz",23)

p2.crearHijo()

# Como se puede apreciar, aún pueden utilizarce las clases y las funciones de las clases
# Hay que tener en cuenta que python va a buscar el módulo en el mismo lugar o directorio 
# donde está el script, y si no lo encuentra lo va a buscar en syspath
# Para utilizar un módulo sea donde se encuentre, se utizarán paquetes

#############################################################################################################################
################################################ PAQUETES ###################################################################
#############################################################################################################################

# Un paquete es un directorio donde se almacenan módulos relacionados entre sí
# Sirven para organizar y reutilizar módulos
# Para crear un paquete, se tiene que crear una carpeta con un archivo __init__.py (que está vacio) parecido al constructor

# Ahora como llamar a este paquete desde otro archivo

from carpeta.modulo import funcion/clase/variable # De esta forma se llama un modulo desde una carpeta

# Tambien para ordenar mejor el código se pueden crear subPaquetes, los cuales igual deberían tener el __init__.py
# y para llamar un modulo de un subPaquete se hace lo siguiente

from carpeta.subcarpeta.modulo import funcion/clase/variable

#############################################################################################################################
#############################################################################################################################
#############################################################################################################################


#############################################################################################################################
############################################## PAQUETES DISTRIBUIBLES #######################################################
#############################################################################################################################

# Esto se hace para que cualquiera pueda utilizar nuestros paquetes
# Para esto el paquete se instalará dentro de python

# Hay que hacer lo siguiente, crear un archivo llamado setup.py con este contenido

from setuptools import setup

setup(
	name="paquteEjemplo",
	version="1.0",
	description="Asi se hace un paquete distribuible",
	author="Elias",
	author_email="earayad@hotmail.cl",
	url="github.com",
	packages=["carpeta","subcarpeta.modulo"] # Aquí se indica donde se encutra el paquete o el subpaquete que se quiere empaquetar
	)

# Después desde la consoloa ir a donde se encuentra el archivo setup.py y escribir 
# python setup.py sdist para crear un paquete distribuible
# Esto creaara un archivo .tar con el nombre del paquete
# Y para instalar el paquete, tienes que ir donde esta el archivo.tar y escribir
# pip3 install nombredelarchivo (truco: escribir las primeras letras del archivo y apretar tab)
# Para desinstalar el paquete y sin importar donde estés escribes
# pip3 unistall nombredelpaquete
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################

