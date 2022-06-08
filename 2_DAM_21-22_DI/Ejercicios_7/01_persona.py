"""Ejercicio 1
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
• Un constructor, donde los datos pueden estar vacíos.
• Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
• mostrar(): Muestra los datos de la persona.
• esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad."""
class Persona():
    def __init__(self,nombre="",edad=0,dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,edad):
        self.__edad = edad

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self,dni):
        self.__dni = dni

    def mostrar(self):
        print("Nombre:",self.__nombre,"- Edad:",self.__edad,"- DNI:",self.__dni)

    def esMayorDeEdad(self):
        if(self.__edad >=18):
            return True
        else:
            return False



def comprobarDni(dni):
    dni_correcto = False
    if(len(dni)==9 and isinstance(dni, str)):
        parte_numerica = int((dni[0:8]))
        parte_letra = (dni[-1:])
        if(isinstance(parte_numerica, int) and isinstance(parte_letra, str)):
            dni_correcto = True
    
    return dni_correcto
    
def comprobarDatos(nombre, edad, dni):
    nombre_correcto = isinstance(nombre, str)
    edad_correcto = isinstance(edad, int)
    dni_correcto = comprobarDni(dni)
    if(nombre_correcto and edad_correcto and dni_correcto):
        return True
    else:
        return False


nombre_proba = "Jorge Val Gil"
edad_prueba = 24
dni_prueba = "35587918H"
datos_correctos = comprobarDatos(nombre_proba,edad_prueba,dni_prueba)

if(datos_correctos):
        persona1 = Persona(nombre_proba,edad_prueba,dni_prueba)
        print("Persona Creada")
        persona1.mostrar()
        mayor_de_edad = persona1.esMayorDeEdad()
        if(mayor_de_edad):
            print(persona1.nombre,"es mayor de edad.")
        else:
            print(persona1.nombre,"es menor de edad.")

else:
    print("Datos incorrectos")