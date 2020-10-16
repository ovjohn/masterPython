#Definir una clase coche
class Coche:
    #atributos o propiedades
    color = "rojo"
    marca = "Fiat"
    modelo = "Uno"
    velocidad = 300
    caballaje = 1000
    plaza = 2

    soy_publico = "Hola soy una Variable Publica"
    __soy_privada = "Soy una variable privada"

    #Definiendo el Costructor
    def __init__(self,color,marca,modelo,velocidad,caballaje,plaza):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plaza = plaza

    #Metodos "Acciones que hace la clase"
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca
    
    def setModelo(self,modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def accelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad

    def getInfo(self):
        info = "----- La Informacion del Auto es:"
        info += "\n Marca: "+ self.getMarca()
        info += "\n Modelo: "+ self.getModelo()
        info += "\n Color: "+ self.getColor()
        info += "\n Velocidad: "+ str(self.getVelocidad())
        return info

    def getPrivada(self):
        return self.__soy_privada

    #Fin definicion de la clase