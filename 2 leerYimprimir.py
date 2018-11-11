#!/usr/bin/python
##########################################################################################################
####################################### LECTURA DE VARIABLES #############################################
##########################################################################################################

# Para leer u/o obtener una variable por teclado se usa el siguiente comando

# Para variables números como int/float

numero = input()

# Para char/strings
string = raw_input()


# También podemos poner texto para decorar la lectura
# Ejemplo:

numero = input("Ingrese un valor: ")
string = raw_input("Ingrese texto: ")

# Esto va a arrojar por consola algo parecido a esto

---------- CONSOLA ------------
"""
Ingrese un valor: 5
Ingrese texto: Hola mundo

"""
-------------------------------

##########################################################################################################
################################# MOSTRAR POR PANTALLA (IMPRIMIR) ########################################
##########################################################################################################

# Para mostrar algun valor por pantalla usamos el siguiente comando

print("Hola mundo") # Esta linea muestra por consola Hola mundo
print(123) 			# Esta linea muestra por consola 123

print(dasdasd) # Si hacemos esto, nos tirará un error de que dasdasd no está definido

-------------- EL ERROR ----------------- 
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# NameError: name 'asdasd' is not defined
-----------------------------------------

# Para poder imprimir variables de distinto tipo que ya han sido definidas,
# hay que hacer ciertos cambios. Ejemplo:

nombre = 'Elías A. Díaz' 	# string
edad = 23 					# int
altura = 1.73 				# float

# Estas variables por si solas si pueden imprimirse Ejemplo:

print(nombre) #	Esto arrojaría Elias A. Díaz

# Ahora si queremos imprimir alguna variable junto con algo de texto, hay que 
# añadir ciertas cosas Ejemplo:

print("Mi nombre es %s" %nombre) # Esto imprime Mi nombre es Elías A. Díaz
# En este caso añadí %s, esto identifica en que parte del texto va a
# ir mi variable de tipo String. %s la s es de string

#Ejemplo con números

print("Mi edad es %d años" %edad) 		   # Esto imprime Mi edad es 23 años
										   # En este caso usé %d de digit p dígito
print("Mi altura es de %f metros" %altura) # Esto imprime Mi altura es de 1.33000000 metros
										   # En este caso usé %f de float, para que muestre los decimales.
print("Mi altura es de %d metros" %altura) # En este caso como usé %d, solo imprimiría Mi altura es de 1 metros

#También podemos combinarlos en un solo print

print("Mi nombre es %s, mi edad es de %d años y mi altura es de %f metros" %(nombre,edad,altura))






