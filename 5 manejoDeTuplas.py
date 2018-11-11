#!/usr/bin/python


# Las tuplas son identicas a las listas, la única diferencia es que se usan
# () y las listas usan []

a = ('hola',"mundo",200,200) # Esto es una Tupla
a = ['hola',"mundo",200,200] # Esto es una lista

# Otro aspecto de las tuplas es que no pueden ser cambiadas como las listas

# Para definir una sola variable en una tupla, se debe incluir una coma

a = ('hola',)

# El acceso a las variables se hace igual que en las listas

print(a[0]) # Esto muestra hola
print(a[:]) # Esto muestra todo el contenido de a

#### ACTUALIZAR TUPLA ######

# Las tuplas no pueden ser editables, pero se pueden crear otras tuplas a base de las tuplas existentes. EJ

tup1 = (1,2,3,4)
tup2 = ('c','b','a')
tup3 = tup1+tup2

print(tup3) # Esto va mostrar (1,2,3,4,'c','b','a')

#############################

### ELIMINAR TUPLAS #####

# Eliminar un valor especifico de una tupla es imposible, solo se puede eliminar una tupla completa Ej:

del tup1

#########################

#### FUNCIONES DE TUPLAS ####

len(tup1)  	  # Entrega el tamaño de la tupla
tup + tup1 	  # Une o concatena estas 2 tuplas 
('tup'!)*4 	  # Crea una tupla con 4 strings tup ('tup','tup','tup','tup')
3 in tup   	  # Retorna true si el valor está en la tupla y false si no está
cmp(tup,tup2) # Compara 2 tuplas, retonando true si son iguales y false si no lo son
max(tup)	  # Retorna el valor mas grande de la tupla
min(tup)	  # Entrega el valor mas chico de la tupla
tuple(lista)  # Convierte una lista en una tupla

#############################
