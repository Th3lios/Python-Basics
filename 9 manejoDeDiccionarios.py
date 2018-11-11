#!/usr/bin/python

# Un diccionario es como una lista la cual en vez de tener un numero como indice, este tiene una clave (key)
# Ejemplo

# valor | "hola" |  "adios"  | "Mundo"| "Marte" |
# clave |"Saludo"|"Despedida"|"Tierra"|"Planeta"|

# Siempre trata de que el nombre de la clave parta con MAYÚSCULAS
# Todas la claves de un diccionario son disintas, pero sus valores pueden ser los mismos
# Así se define un diccionario

# Primero, se define la variable, en este caso dic
# Segundo, se iguala a {}
# Tercero, dentro de {} entre comillas simples o dobles se escribe el nombre de la clave.
# la clave tambien puede ser un número, el cual no es necesario que esté entre comillas
# Cuarto, seguido de la clave, se pone : (dos puntos)
# Quinto, seguido de los : se pone el valor, el cual puede ser de cualquier tipo (string,int,bolean,etc)

dic = {'Clave':'variable','Saludo':'hola',7:'adios', 1:'mundo','Planeta':True}

# Para acceder a una variable se hace lo siguiente

print(dic['Clave']) # Esto muestra variable
print(dic['Saludo']) # Esto muestra hola

#### ACTUALIZAR DICCIONARIO ####

# Para actualizar un diccionario solo hay que añadir un nuevo valor a una clave del diccionario Ej:

dic['Clave'] = 'nuevaClave'
dic['Saludo'] = 'hello'

################################

#### ELIMINAR DICCIONARIO ####

# Asi se elimina una clave en específico

del dic['Clave']

# Asi se limpian todas las entradas en un diccioanrio

dic.clear() # Esto deja el diccionario vacío, {}

# Esto elimina el diccionario por completo

del dic


##############################

### PROPIEDADES DE LAS CLAVES (KEYS) ###

# Hay 2 puntos importantes que recordar sobre las claves de los diccionarios
# - A una clave no se le pueden asociar 2 valores Ej dic = {'Key':valor,'Key':valor2} (Esto no puede pasar)
# si hacemos print(dic['Key']:)
# - Las claves tienen que ser únicas. Oueden ser strings, numeros e incluso tuplas, pero algo como ['key'] como clave
# no está permitido Ej dic = {['key']:'clave'} esto arroja error, en cambio dic = {('key'):'clave'} si puede ser una clave
# Esto se debe a que la primera forma corresponderia a una lista y las listas pueden cambiar, en cambio las tuplas son inmutables

########################################

# RECORDAR

# Las FUNCIONES son distintos a los MÉTODOS
# Las FUNCIONES se hacen sobre algun tipo de dato (son más generales)
# Los MÉTODOS son funciones de un tipo de dato (son específicos de algún tipo de dato)

### FUNCIONES SOBRE DICCIONARIOS ###

cmp(dic1,dic2) # Retorna true si son iguales y false si son distintos
len(dic) 	   # Retorna el tamaño de un diccionario
str(dic)	   # Retorna un string del diccionario completo
type(variable) # Entrega el tipo de datos de una variable, en caso de un diccionario, su tipo de dato es dict

###########################################

# Vamos a definir un diccionario como dic

### MÉTODOS DE UN DICCIONARIO ###

dic.clear() 	# Este método elimina el contenido del diccionario, dejando solo las llaves {}
dic.copy()		# Este método retorna una copia superficial del diccionario dic
-------------------------------
seq = ('uno','dos','tres')
dic.fromkeys()    		# Crea un nuevo diccionario a partir de una secuencia pre definida como una tupla
dic.fromkeys(seq) 		# Esto muestra {'uno': None, 'dos': None, 'tres': None}
dic.fromkeys(seq,10)	# Esto muestra {'uno': 10, 'dos': 10, 'tres': 10}
-------------------------------
dic.get(key,default=None) # Esto a través de la clave, devuelve un valor o default si la clave no está en el diccionario
dic[key] 				  # Esto es lo mismo de arriba, solo que no devuelve none al poner una clave que no existe
dic.has_key(key)		  # Esto devuelve true si la clave está en el diccionario, de otra forma devuelve falso
dic.items()				  # Esto devuelve una lista de de tuplas pares con la clave y el valor Ej: [(clave,valor),(clave1,valor1),(clave2,valor2)]
dic.keys()				  # Esto devuelve una lista de las claves del diccionario
dic.values()			  # Esto devuelve una lista de los valores del diccionario
dic.setdefault(key,default=None) # Esto es similar al get, pero en caso de que no exista la clave, la va a crear con un valor none
dic.update(dic2)		  # Esto añade los datos del dic2 a dic1

#################################
