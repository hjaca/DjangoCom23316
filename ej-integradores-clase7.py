# Ejercicios integradores para revisar en la clase 7
#--------------------------------------------------------------------------------------------------------------------
# 1. Escribir una función que calcule el máximo común divisor entre dos números.
def mcd(x, y):
    from math import gcd  
    return gcd(x,y)  

x = int(input("Ingrese numero X: "))
y = int(input("Ingrese numero Y: "))
mcd_ = mcd(x, y)
print("El mcd entre {} y {} es {}\n".format(x, y, mcd_))  

#--------------------------------------------------------------------------------------------------------------------
# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números
def mcm(x, y):
    from math import gcd  
    mcd = gcd(x, y)  
    mcm = int(x * y / gcd(x, y))
    return mcm

x = int(input("Ingrese numero X: "))
y = int(input("Ingrese numero Y: "))
mcm_ = mcm(x, y)
print("El mcm entre {} y {} es {}\n".format(x, y, mcm_))  

#--------------------------------------------------------------------------------------------------------------------
# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene 
# y la cantidad de veces que aparece (frecuencia).
def diccionario_y_frecuencia(cadena):
    # variables
    palabras = cadena.split()
    diccionario = {}

    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra]  += 1
        else:
            diccionario[palabra] = 1

    return diccionario


cadena = input("Ingresar una cadena de caracteres: ")
diccionario = diccionario_y_frecuencia(cadena)

print(f"Diccionario:")
print(diccionario)

print(f"Frecuencia de palabras:")
for palabra in diccionario:
    print(f"'{palabra}': {diccionario[palabra]}")

#--------------------------------------------------------------------------------------------------------------------
# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene 
# y la cantidad de veces que aparece (frecuencia). Escribir otra función que reciba el diccionario generado 
# con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
def diccionario_y_frecuencia(cadena):
    # variables
    palabras = cadena.split()
    diccionario = {}

    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra]  += 1
        else:
            diccionario[palabra] = 1

 
    return diccionario

def tupla_y_frecuencia(diccionario):
    # variables
    tupla = []
    max_palabra = ""
    max_frecuencia = 0

    for palabra in diccionario:
        if diccionario[palabra] > max_frecuencia:
            max_frecuencia = diccionario[palabra]
            max_palabra = palabra
    tupla = (max_palabra, max_frecuencia)
    return tupla

cadena = input("Ingresar una cadena de caracteres: ")
tupla = tupla_y_frecuencia(diccionario_y_frecuencia(cadena))

print(f"Tupla con palabra mas frecuente: {tupla}" )

#--------------------------------------------------------------------------------------------------------------------
# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en 
# su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, 
# iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.
def get_int(valor):
    try:
        return int(valor)
    except ValueError:
        while True:
            return get_int(input("Ingresar un valor entero: "))

valor = input("Ingresar un valor entero: ")
print(f"el valor {get_int(valor)} es entero")

""" 
6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
- Un constructor, donde los datos pueden estar vacíos.
- Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
- mostrar(): Muestra los datos de la persona.
- Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad. 
"""
# clase Persona
class Persona:
    # atributos
    nombre = ''
    edad   = 0
    dni    = ''
 
    # constructor de la clase
    def __init__(self, nombre):
        self.nombre = nombre
    
    #Definimos los "setters"
    def setNombre(self, nombre):
        self.nombre = nombre
 
    def setEdad(self, edad):
        self.edad = edad
 
    def setDNI(self, dni):
        self.dni = dni
 
    #Definimos los "getters"
    def getNombre(self):
        return self.nombre
 
    def getEdad(self):
        return self.edad
 
    def getDNI(self):
        return self.dni
 
    #método en la clase para mostrar todos los datos de la persona por pantalla
    def mostrar(self):
        print('El nombre de la persona es: ' + self.nombre)
        print('La edad de la persona es: ' + str(self.edad))
        print('El DNI de la persona es: ' + self.dni)
    
    def Es_mayor_de_edad(self):
        return self.edad >= 18


# Definimos personas
persona1 = Persona("Alberto Spineta")
persona2 = Persona("Patricia Sosa")
persona3 = Persona("Soledad Pastorutti")
persona4 = Persona("Bizarrap")

# Con los setters cargamos los datos de las personas
persona1.setDNI("10000000")
persona2.setDNI("20000000")
persona3.setDNI("30000000")
persona4.setDNI("40000000")

persona1.setEdad(10)
persona2.setEdad(20)
persona3.setEdad(30)
persona4.setEdad(40)
 
# Usamos el método de la clase que muestra los datos de la persona por pantalla
persona1.mostrar()
persona2.mostrar()
persona3.mostrar()
persona4.mostrar()

print(persona1.Es_mayor_de_edad())
print(persona2.Es_mayor_de_edad())
print(persona3.Es_mayor_de_edad())
print(persona4.Es_mayor_de_edad())

#------------------------------------------------------------------------------------------------------------
"""
7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase: 
- Un constructor, donde los datos pueden estar vacíos.
- Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero. 
- mostrar(): Muestra los datos de la cuenta. 
- ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. 
- retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos. 
"""

"""
8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase: 
- Un constructor. 
- Los setters y getters para el nuevo atributo. 
- En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
- Además, la retirada de dinero sólo se podrá hacer si el titular es válido. 
- El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
"""

