#!/usr/bin/python

# Hasta ahora hemo hecho lecturas estandar de datos a traves de
# input() # Permite el uso de simbolos
# raw_input() # No ejecuta los simbolos y los muestra textualmente
# Ahora veremos como realizar lecturas pero de archivos

# Primero que todo hay que importar la libreria io  y saber como abrir un archivo, para eso
# ejecutamos el comando open("dirección del archivo")
from io import * # Esto se explica en modulosYPquetes.py
file = open("dirección del archivo",[,modo de acceso][,buffering])

# modo de acceso indica de que forma queremos abrir el archivo
#	-Lectura sería r (read), el puntero se posiciona al comienzo del archivo
#	-Escritura sería w (write) el puntero se posiciona al comienzo del archivo y 
#	 sobreescribe un archivo si ya existe (borra y el contenido y escribe uno nuevo), en caso contrario si no existe lo crea
#	-Editar sería a (append) el puntero se posiciona al final del archivo. Si el archivo no existe lo crea

# Buffering no lo entiendo

# Algunos atributos de los objetos tipo file (file object)

file.closed() 		# Devuelve true si el archivo es cerrado y falso en cualquier otro caso
file.mode()			# Devuelve el modo de acceso con el cual fue abierto el archivo (r,w,a)
file.name()			# Devuelve el nombre del archivo
file.softspace()	# Devuelve falso si el espacio es requerido con print y verdadero de otra manera

# El Método close() es utilizado para cerrar la escritura o lectura de un archivo, una vez hecho ya no se puede editar
# hasta abrirlo de nuevo

# Python cierra automaitcamente el archivo cuando la referencia de un archivo es reasignado a otro archivo. Es una buena
# práctica cerrar los archivos con close()

file.close()

var = open("foo.txt", "w")
print (var.name())  # Imprime el nombre del archivo foo.txt
var.close()

### LECTURA Y ESCRITURA ###

# El método write() permite escribir cualquier texto en un archivo, es importante tener en cuenta que los string de python
# puede tener datos binarios y no solo texto.
# El método write() no añade un \n al final del texto, por lo cual no hace un salto de linea 

var = open("foo.txt","w")
var.write("Algo de texto")
var.close()


# El método read() permite leer cualquier texto en un archivo, al igual que la escritura hay que tener en cuenta que pueden
# haber string con datos binarios

var = open("foo.txt","r")
var.read(10)  # 10 corresponde al numero de bytes que serán leidos. Si el valor puesto no es encontrado o alcanzado, entonces
			  # va a proceder a leer la mayor cantidad de bytes hasta terminar el archivo completo
var.close()

# El método tell() te dice cuando bytes desde el comienzo del archivo hasta donde estas posicionado hay.

var.tell()

# El método seek(offset[,from]) cambia tu posicion actual. El valor de offset indica cuandos bytes quieres moverte desde donde
# estás actualmente.
# from puede ser:
	0 # inicio del archivo
	1 # posicion actual en el archivo
	2 # final del archivo

var.seek(0,0) # Desde el comienzo hasta el comienzo (0,0)


### MODULO OS DE PYTHON ###

# Este modulo provee a python el uso de comandos del sistema como cd,dir,mkdir,etc
# Ayuda a realizar operaciones en archivos

import os # De esta forma importamos paquetes en python, ya se hablará de eso

os.rename("nombreActual.txt","nuevoNombre.txt") # Con este método de os podemos editar el nombre de un archivo
os.remove("nombreActual.txt")					# Con este método podemos eliminar un archivo
os.mkdir("nuevoDirectorio")						# Con este método podemos crear un directorio
os.chdir("/home/nuevoDorectorio")				# Con este método cambias el directorio actual al que recibe como parámetro
os.getcwd()										# Este método muestra el directorio actual de trabajo
os.rmdir("directorio")							# Este método elimina un directorio
###########################

#### METODOS DE ARCHIVOS ####

file.close()  			# Cierra el archivo, este ya no puede ser leido o editado
file.flush()  			# libera la memoria utilizada por el buffer.
file.fileno() 			# Devuelve un entero que es usado para request de entrada y salida desde el sistema operativo
file.isatty() 			# Devuelve true si el archivo está conectado a tty device, de otra forma retorna falso
file.next()   			# Devuelve la siguiente linea del archivo cada vez que es llamado
file.read(tamaño) 		# Lee la cantidad de bytes de tamaño ingresado desde la posicion actual
file.readline(tamaño) 	# Lee una pura linea del archivo
file.readlines(tamaño)  # Lee hasta el final del archivo usando readline() y devuelve una lista conteniendo las lineas.
						# si el tamaño opcional es seteado, entonces lee hasta ese tamaño de bytes aproximadamente
file.seek(0,0)			# 0,1,2 setea la posicion actual en el archivo
file.tell()				# Devuelve la posicion actual en el archivo
file.truncate(tamaño)	# Trunca el tamaño del archivo, si se setea el tamaño va a tratar de truncarlo a ese valor
file.write(str)			# Escribe sobre el archivo y no devuelve ningun valor
file.writelines(seq)	# Escribe una secuencia de strings en el archivo. La secuencia puede ser cualquier objeto iterable
						# que produca strings, como una lista de strings

