"""
Modulos: Son funcionalidades ya hechas para reutilizar

En la documentacion de Python existen muchos modulos para ser consultadas y utilizadas.

Podemos conseguir modulos que ya vienen en el lenguaje,
modulos de internet o tambien podemos CREAR nuestros modulos
"""
#LLamando los Modulos
#import mimodulo #Importando mudolo propio
#from mimodulo import holaMundo
from mimodulo import *

#print(mimodulo.holaMundo("John")) #Utilizando el la funcion holaMundo del Modulo
#print(mimodulo.calculadora(2,4,False)) # Utilizando otra funcion
#print(holaMundo("Juan Jose"))

#Modulo fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.day)
print(fecha_completa.month)
print(fecha_completa.year)
print(fecha_completa.strftime("%d/%m/%Y, %H-%M-%S"))

#Modulo Matematica
import math
print("La Raiz cuadrada de 10 es:", math.sqrt(10))
print("Numero pi:", float(math.pi))
print("Rendondiar un numero:", math.ceil(12.457))

#Modulo Aleatorio
import random

print("Numero aleatorio entre 2 y 9 es:", random.randint(2,9))
