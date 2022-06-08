"""
Ejercicio 3
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuentaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Construye los siguientes métodos para la clase:
• Un constructor.
• Los setters y getters para el nuevo atributo.
• En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
• Además la retirada de dinero sólo se podrá hacer si el titular es válido.
• El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
Piensa los métodos heredados de la clase madre que hay que reescribir."""
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



class CuentaJoven(Cuenta):
    def __init__(self, bonificacion, titular, cantidad=0):
        super().__init__(titular, cantidad=cantidad)
        self.__bonificacion = bonificacion
    
    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion = bonificacion

    def retirar(self, cantidad):
        if(self.titular.edad >=18 and self.titular.edad <25):
            return super().retirar(cantidad)
        else:
            print("El usuario no és válido no se puede retirar dinero")

    def mostrar(self):
        print("Cuenta Joven - Bonificación:",self.bonificacion)

    def ingresar(self, cantidad):
        return super().ingresar(cantidad)
    

def esTitularValido(persona):
    if persona.edad >= 18:
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
        if esTitularValido(persona1):
            print("Persona Creada")
            cuenta = CuentaJoven(30,persona1,9999.99)
            cuenta.mostrar()
            cuenta.ingresar(1000)
            cuenta.ingresar(-20000)
            cuenta.mostrar()
            cuenta.retirar(2000)
            cuenta.mostrar()
        else:
            print("No puedes ser titular, no eres mayor de edad.")
        
else:
    print("Datos incorrectos")