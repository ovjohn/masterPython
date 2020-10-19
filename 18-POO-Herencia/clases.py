#Herencia. Es la capacidad de compartir atributos y metodos entre 
#clases y que las diferentes clases heredan entre ellas¡¡

class Persona:
    """
    nombre
    apellidos
    altura
    edad
    """
    def setNombre(self,nombre):
        self.nombre = nombre

    def setApellidos(self,apellidos):
        self.apellidos = apellidos
    
    def setAltura(self,altura):
        self.altura = altura
    
    def setEdad(self,edad):
        self.edad = edad

    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos
    
    def getAltura(self):
        return self.altura 
    
    def getEdad(self):
        return self.edad

    def caminar(self):
        return("Estoy Caminando")

    def dormir(self):
        return("Estoy durmiendo")

    def hablar(self):
        return("Estoy Hablando")

#Creando una nueva Clase que va a heredar de la clase Persona
class Informatico(Persona):
    """
    Lenguajes
    Experiencia
    """
    def __init__(self):
        self.lenguajes = "HTML5, CCS"
        self.experiencia = 1
    
    def getLenguajes(self):
        return self.lenguajes

    def getExperiencia(self):
        return self.experiencia

    def aprender(self,lenguaje):
        self.lenguajes += ", "+ lenguaje
        return self.lenguajes
    
    def programar(self):
        return("Estoy programando")

    def repararPC(self):
        return("Estoy Programando")

class Tecnico(Informatico):
    def __init__(self):
        super().__init__()#Con el metodo super() accedo al constructor del la clase padre "Informatico"
        self.dominioRedes = "Experto"
        self.experienciaRedes = 15

    def auditandoRedes(self):
        return ("Estoy auditando redes")

    def auditoria2(self):
        return("Estoy auditando 2")



    
