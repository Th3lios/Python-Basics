#!/usr/bin/python

# Se puede definir un string con doble comillas "" o con comillas simples ''

nombre = 'Elias'
apellido = "Araya"
edad = 23

# Para concatenar strings usamos +

print(nombre + apellido) 					   # Esto arroja EliasAraya
print(nombre + " " + apellido) 				   # Esto arroja Elias Araya
print("%s %s"%(nombre,apellido)) 			   # Esto tambien arroja Elias Araya
print("%d %s"%(edad, nombre + " " + apellido)) # Esto arroja 23 Elias Araya

# Tambien podemos definir un string como "raw", esto significa que todo el
# contenido de la variable va a ser string, sin importar si en el contenido
# de la variable hay algún simbolo.

# Ejemplos de simbolos:
# \n corresponde a un salto de linea (enter)
# \t corresponde a un tab o 8 espacios

variable = r'Hola \n \t mundo' 
print(variable) 				# Esto imprime Hola \n \t mundo

# Ahora sin la r

variable2 = 'Hola \n \t mundo'
print(variable2) 				# Esto imprime:

########## CONSOLA #############
#~1 Hola
#~2 		mundo
################################

####### Simbolos ###############
"""
\a	0x07	Bell or alert
\b	0x08	Backspace
\cx	 	Control-x
\C-x	 	Control-x
\e	0x1b	Escape
\f	0x0c	Formfeed
\M-\C-x	 	Meta-Control-x
\n	0x0a	Newline
\nnn	 	Octal notation, where n is in the range 0.7
\r	0x0d	Carriage return
\s	0x20	Space
\t	0x09	Tab
\v	0x0b	Vertical tab
\x	 	Character x
\xnn	 	Hexadecimal notation, where n is in the range 0.9, a.f, or A.F
"""
##################################

# Como vimos en 1 variables.py los strings largos se hacen con """string""". Esto puede
# se asociado a una variable Ejemplo:

lString = """ asdsa
asdsad
asdsa
asdas
"""
print(lString) 

########## CONSOLA #############
#~1 asdsa
#~  asdsad
#~	asdsa
#~	asdas
################################

############# METODOS SOBRE STRINGS ##############

# s.lower(), s.upper() -- retorna el string s como minúscula(lower) o mayúscula(upper)

print(nombre.lower())	# Imprime elias
print(nombre.upper())	# Imprime ELIAS

# s.strip() -- retorna el string s sin espacios en blanco

print((nombre+" "+apellido).strip())	# Imprime EliasAraya

# s.isalpha()(solo letras)/s.isdigit()(solo números)/s.isspace()(solo espacios)
# ... -- retorna true o false si cumple con alguna de las condiciones

test = "asss"
test1 = "123"
test2 = "  "
print(test.isalpha()) 	# Imprime true
print(test1.isdigit()) 	# Imprime true
print(test2.isspace()) 	# Imprime true

# s.startswith('other'), s.endswith('other') -- retorna true o false si el string comienza o termina con otro string

print(nombre.startswith('Eli')) # imprime true
print(nombre.endswith('as')) 	# imprime true

# s.find('other') -- busca en s el caracter o el string y retorna el indice que ocupa dentro del string nombre. 
# Si no se encuentra retorna -1
# Recordar que retorna el indice de la primera ocurrencia!

print(nombre.find('Eli')) 	#imprime 0
print(nombre.find('E')) 	#imprime 0
print(nombre.find('l')) 	#imprime 1
print(nombre.find('as')) 	#imprime 3
print(nombre.find('s')) 	#imprime 4

# |E|L|I|A|S|
# |0|1|2|3|4|


#s.replace('old', 'new') -- retorna un string donde lo viejo se cambio por lo nuevo

print(nombre.replace('Eli', 'as')) 	#Imprime asas

#s.split('delim') -- retorna una lista de la cadena dividida por el delimitador que elegiste. Si dejas vacío el split, entonces divide por
#espacios en blanco

ejemplo = 'aaa,bbb,ccc'
print(ejemplo.split(',')) 	#Retorna -> ['aaa','bbb','ccc']

# |aaa|bbb|ccc|
# | 0 | 1 | 2 |

value = ejemplo.split(',')

# s.join(list) -- Es lo contrario al split, une una lista como ['aaa','bbb','ccc'] pero el delimitador es el string s

print('---'.join(value)) 	#Imprime -> aaa---bbb---ccc


# Hay que recordar que un string se comporta como un array pero de char's

new = 'hola mundo'

#|h|o|l|a| |m|u|n|d|o|
#|0|1|2|3|4|5|6|7|8|9|

print(new[0]) 			#Imprime h
print(new.find('h')) 	#Imprime 0

#Hay muchas funciones más pero estas son las básicas