#Programación orientada a objeto (POO o OOP)

#Definir una clase coche
class Coche:
    #atributos o propiedades
    color = "rojo"
    marca = "Fiat"
    modelo = "Uno"
    velocidad = 300
    caballaje = 1000
    plaza = 2

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
    #Fin definicion de la clase

coche = Coche() #Creacion del Objeto coche o Innstacion de Coche
print("*************Coche-1***********************")
print(coche.marca, coche.color)
print("La velocidad actual es: "+ str(coche.getVelocidad()))

coche.accelerar()#Usando el metodo acelerar
coche.accelerar()
coche.accelerar()
print("La velocidad Nueva es: ", coche.getVelocidad())

coche.frenar()#Usando el metodo frenar
print("La velocidad actual es: ", coche.getVelocidad())

print("El color Actual es: ", coche.getColor())
coche.setColor("Azul")
print("Ahora el color es: ", coche.getColor())

print("_________---------------------")

coche2 = Coche()
coche2.setColor("Azul")
coche2.setMarca("Toyota")
coche2.setModelo("Terio")
print("****+*******Coche-2***********")
print(coche2.getColor(), coche2.getMarca(), coche2.getModelo())

