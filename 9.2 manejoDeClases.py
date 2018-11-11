#!/usr/bin/python

# Cuando hablamos de clases, nos empezamos a dirigir a otra parte de la programación, denominada
# programación orientada a objetos o POO.
# Hay que tener claro que la programación orientada objetos tiene ciertos principios, los cuales son:
# 	-Encapsulamiento
# 	-Herencia
# 	-Polimorfismo
# 	-Abstracción
# Cada Uno de estos términos se van a ir definiendo en los siguientes archivos

#############################################################################################################################
#########################################################  CLASES ###########################################################
#############################################################################################################################

# Cada clase se considerará un objeto y como todo objeto estas clases tienen propiedades Ejemplo:
# Pensemos en una persona como Objeto
# Una persona tiene propiedades como : Nombre, Apellido, Edad, Direccion, Correo, etc
# Y una persona tambien puede realizar acciones, las cuales se denominan MÉTODOS
# Una persona tiene métodos como : Saludar, Despedirse, Dormir, Correr, etc
# Hay que tener en cuenta que las clases SOLO estan compuesta de MÉTODOS
# Creemos una clase Persona

class Persona():
	nombre 	  = "Elias"
	apellidos = "Araya Diaz"
	edad 	  = 23

# Esta es una persona y como habíamos dicho antes, cada persona tiene
# un nombre, apellidos y edad. En este caso le dimos un nombre un
# apellido y edad a esa persona de forma directa, esto significa que al
# crear una persona, esta tendrá esas propiedades Ejemplo

persona1 = Persona() # Aquí estamos creando a la persona1, la cual va a
					 # tener las propiedades de la Clase Persona

# Esto en programación se llama "INSTANCIACIÓN" ejemplo
# persona1 es una "INSTANCIA" de Persona
# Hagamos otra "INSTANCIA"

persona2 = Persona() # Esta es otra instancia de la Clase Persona, que tiene las mismas propiedades de la clase persona

# Para acceder a las pripiedades de persona1 o persona2 hay que hacerlo con un "punto" y luego la propiedad

print(persona1.nombre) # Esto imprime Elias
print(persona2.nombre) # Esto imprime Elias

#############################################################################################################################
#############################################################################################################################

# Perfecto, ya sabemos crear una clase y realizar instancias de esa clase, pero faltan una cuantas cosas más.
# Por ejemplo ¿y si no queremos que los nombres de cada instancia sean los mismos? en este caso, las instancias persona1 y
# persona2 se llaman Elias, ya que la Clase Persona tiene esas propiedades.
# Para eso tenemos que crear un método el cual en programación se denomina constructor y en python se define como
# __init__() Ej


class Persona():
	def __init__(self):
		self.nombre    = "Elias"
		self.apellidos = "Araya Diaz"
		self.edad      = 23

# Ahora a aparecido el concepto de "self". "Self" hace referencia a la instancia actual, ¿a que me refiero con esto? observa lo
# siguiente

persona1 = Persona() # Se crea una isntancia de Persona llamada persona1

# Ahora self hace referencia a la instancia que hemos creado (persona1)
# Debido a esto cuando hacemos persona1.nombre, este nos arroja el nombre Elias
# Puedes imaginar lo siguiente, cambiar el self por el nombre de la instancia, en este caso persona1

class Persona():
	def __init__(persona1):
		persona1.nombre    = "Elias"
		persona1.apellidos = "Araya Diaz"
		persona1.edad      = 23

# Entonces cuando hacemos
print(persona1.nombre) # Este entra al CONSTRUCTOR(__init__) DE PERSONA y muestra el valor de persona1.nombre, en este caso Elias

# Por cada instancia que creemos, hay que pensar en lo anterior.
# Creemos otra instancia

persona2 = Persona()
print(persona2.apellidos) # Aqui mostraría Araya Diaz

# Ahora tenemos 2 instancias de la Clase Persona, persona1 y persona2. En este caso el self ayuda a diferenciar las propiedades
# de cada clase, ya que como habiamos dicho antes, el self hace referencia a su propia instancia, asi no cambia las propiedades
# de otras instancias Ejemplo:

persona1.nombre = "Javier" # Ahora el nombre de persona1 ya no es Elias, sino Javier, ¿pero que pasa con persona2?
print(persona2.nombre) # Esto sigue arrojando Elias, esto se debe gracias al self, ya que cada instancia tiene sus propias
					   # propiedades gracias al CONSTRUCTOR DE PERSONA(__init__(self)) que tiene self adentro.

#############################################################################################################################
#############################################################################################################################

# Entonces mas gráficamente podemos imaginar lo siguiente por cada instancia que creamos

persona1 = Persona() # Para esta instancia imaginamos esto

class Persona():
	def __init__(persona1):
		persona1.nombre    = "Javier"
		persona1.apellidos = "Araya Diaz"
		persona1.edad      = 23

perosna2 = Persona() # Para esta instancia imaginamos esto

class Persona():
	def __init__(persona2):
		persona2.nombre    = "Elias"
		persona2.apellidos = "Araya Diaz"
		persona2.edad      = 23

# Por lo mismo esto se resume para cada instancia con

class Persona():
	"""docstring for Persona"""
	def __init__(self):
		self.nombre    = "Elias"
		self.apellidos = "Araya Diaz"
		self.edad      = 23		

# Con los Métodos ocurre lo mismo. Creemos un método de la clase persona

class Persona():

	def __init__(self):
		self.nombre    = "Elias"
		self.apellidos = "Araya Diaz"
		self.edad      = 23		

	def saludar(self): # Acá pusimos el self para poder hacer referencia al nombre de la instancia
		print("Hola ", self.nombre)

# Creamos una instancia

persona1 = Persona()

# Ahora persona1 también tiene el método de saludar

persona1.saludar() # Así usamos los métodos, al igual que las propiedades usamos un "punto" y después el nombre del método
				   # con paréntesis al final ()
				   # Esto imprime Hola Elias

# Creemos otra instancia y cambiemosle el nombre

persona2 = Persona()
persona2.nombre = "Adriana"
persona.saludar() # ¿Que muestra esto? : _____________

#############################################################################################################################
#############################################################################################################################

# Hasta ahora hemos visto clases pero con puras propiedades estáticas, hagámoslo más dinámico
# para poder nosotros mismos agregarle los nombres, apellidos y edades a los objetos hay que hacer lo siguiente
# Creamos la clase Persona con su CONSTRUCTOR (__init__)

class Persona():
	def __init__(self, nombres, apellidos, edades): # Aquí definimos las variables que va a aceptar la clase al momento de
		self.nombre = nombres                       # hacer una instancia
		self.apellido = apellidos
		self.edad = edades

	def saludar(self): 			   # Acá pusimos el self para poder hacer referencia a las propiedades de la instancia
		print("Hola", self.nombre) # En este caso accedimos al nombre de la instancia actual

# Ejemplo

persona1 = Persona("Elias","Araya Diaz",23)
persona2 = Persona("Javier","Araya Valenzuela",53)

# Entonces si hacemos lo siguiente

persona1.saludar() # Que muestra? Hola ______
persona2.saludar() # Que muestra? Hola ______

#############################################################################################################################
#############################################################################################################################


#############################################################################################################################
######################################################## HERENCIAS ##########################################################
#############################################################################################################################

# Al igual que en la vida real, los objetos igual pueden heredar propiedades y métodos
# Una persona puede heredar los colores de ojos de sus padres o el tipo de cabello e incluso algún tipo de gestos
# Ejemplo de herencia

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

# Aquí entra el método "super()". Este método lo único que hace es hacer una referencia al padre de ese objeto, por ejemplo
# el padre del objeto Madre es Persona, el padre del objeto Hijo es Persona y Pesona no tiene ningun padre
# super() hace que los hijos hereden las pripiedades o métodos del padre
# Si nos damos cuenta el método __init__() contiene las propiedades de cada objeto
# entonces si hacemos super().__init__() el hijo hereda las propiedades que están en la funcion __init__ del padre Ej

class Persona():
	def __init__(self, nombre,apellido,edad):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad

class Hijo(Persona):						# Se crea la clase hijo que hereda el constructor y métodos de persona
	def __init__(self,altura,peso): 		# Se define el constructor de Hijo
		super().__init__("Elias","Araya",23)# Se hace referencia al constructor del padre de Hijo y se le asignan variables
		self.altura = altura				# Propiedad específica de Hijo
		self.peso = peso

# Entonces Hijo tiene sus propias variables de su propio constructor y además tiene las variables del constructor de Persona
# Todo eso gracias al super()

# Ahora analicemos a la Clase Madre(Persona)

class Madre(Persona):							# Se crea la clase Madre que hereda Persona
	def __init__(self,nombre,apellido,edad):	# Se definen las variables que aceptará la clase
		super().__init__(nombre,apellido,edad)	# Se hace referencia al constructor del padre de Madre y se le asignan las variables

	def crearHijo(self):						# Se define un método para crear hijos
		nombre = input()						# Se definen las variables
		edad = 0
		hijo = Hijo(nombre,self.apellido,edad)	# Se crea un hijo con las variables
		return hijo                             # La funcion retorna un hijo con las variables


#############################################################################################################################
###################################################### POLIMORFISMO #########################################################
#############################################################################################################################

# El polimorfismo significa muchas(poli) formas(morfismo), significa que una clase puede tomar muchas formas. Ejemplo
# En la vida real las personas tiene el método saludar ¿cierto?, ya pero no todas las personas saludan de la misma manera
# Unos se saludan con un beso, otros con la mano, otros con reverencias, etc. De eso exactamente trata el polimorfismo
# Que una clase como la de "persona" tenga un mismo método como "saludar", pero que se realize de diferentes formas, Ejemplo:

### SIN POLIMORFISMO ###
class Chino(Persona):
	def saludar(self):
		print("Hace una reverencia")

class Frances(Persona):
	def saludar(self):
		print("Da un beso")

class Chileno(Persona):
	def saludar(self):
		print("Saluda con la mano")

p1 = Chino()
p2 = Frances()
p3 = Chileno()

p1.saludar()
p2.saludar()
p3.saludar()
##########################

### CON POLIMORFISMO #####
class Chino(Persona):
	def saludar(self):
		print("Hace una reverencia")

class Frances(Persona):
	def saludar(self):
		print("Da un beso")

class Chileno(Persona):
	def saludar(self):
		print("Saluda con la mano")

def saludarPersona(personas): # Se define una función genérica que llama a cada objeto y identifíca su función saludar
	personas.saludar()		  # Este saludar identifica automatícamente que saludar usar dependiendo la clase de objeto

p1 = Chino()
p2 = Frances()
p3 = Chileno()

saludarPersona(p1)
saludarPersona(p2)
saludarPersona(p3)

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################



		











	


		


























class Persona(object):
	"""docstring for Persona"""
	#__init__ es un método especial que se ejecuta de manera inmediata en python al crear una instancia de una clase
	# El parámetro self es utilizado para que cada instancia de la clase tenga una copia de única
	# de los métodos y no puedan ser editados por otras instancias al ser llamadas.
	def __init__(self, nombre,apellido,edad,direccion,correo):# Este método corresponde al Denominado Constructor, este almacena
															  # todas las propiedades de la clase
		super(Persona,self).__init__()
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.direccion = direccion
		self.correo = correo

	def saludar():
		print("Hola")

super(Persona,self).__init__() # En breve se explicará este linea, primero hay que hablar de HERENCIAS

# Al igual que en la vida real, las personas pueden tener descendencia. Pasa lo mismo con los objetos, estos pueden
# tener descendientes que heredan las cualidades de los padres, por ejemplo una madre que le hereda su cabello ondulado
# a su hijo, o el color de ojos, etc

class Madre(object): # Se crea un objeto madre con su propio color de ojos y tipo de cabello
	def __init__(self,altura,edad)
		super(Madre,self).__init__()
		self.colorOjos = "azul"
		self.tipoCabello = "ondulado"
		self.altura		 = altura
		self.edad 		 = edad

class Hijo(Madre): # Se crea un hijo que hereda a madre
	"""docstring for hijo"""
	def __init__(self,altura,peso): # Estas son las propiedades del hijo, tiene 2 más que la madre
		super(Hijo, self).__init__(colorOjos,tipoCabello) # En esta linea, el hijo obtiene las propiedades de la madre
		self.altura = altura # Estas son propiedades específicas del hijo
		self.peso   = peso   # Si te das cuenta el hijo no hereda la propiedad de altura ni de edad, ya que son propias del hijo
		





