"""Ejercicio 2
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
• Un constructor, donde los datos pueden estar vacíos.
• Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, solo ingresando o retirando dinero.
• mostrar(): Muestra los datos de la cuenta.
• ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
• retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos."""
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

class Cuenta():
    def __init__(self,titular, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self,titular):
        self.__titular = titular

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad = cantidad
    
    def mostrar(self):
        print("Nombre:",self.titular.nombre)
        print("Nombre:",self.titular.nombre,"- Edad:",self.titular.edad,"- DNI:",self.titular.dni)
        print("Cantidad cuenta:",self.__cantidad,"€\n")

    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
        else:
            print("\nLa cifra es negativa.\n")
    
    def retirar(self,cantidad):
        self.__cantidad = self.__cantidad - cantidad


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
        cuenta = Cuenta(persona1,5555.6)
        cuenta.mostrar()
        cuenta.ingresar(1000)
        cuenta.ingresar(-20000)
        cuenta.mostrar()
        cuenta.retirar(2000)
        cuenta.mostrar()
        
else:
    print("Datos incorrectos")
