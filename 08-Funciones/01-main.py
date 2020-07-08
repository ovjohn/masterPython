"""
Una funcion es un conjunto de instrucciones agrupadas
bajo un nombre en concreto y que se puede reulitizar
tantas veces sea necesariio

ejemplo:

def nombrePersona(parametros)
    #Aquí el conjunto de instrucciones

#Para llamarla se hace así: nombrePersona(mi-parametro)
"""

#Ejemplo1
print("############ Ejemplo 1 - Funciones")

#Definiendo funcion
def muestraNombre():
    print("Juan")
    print("Perez")
    print("Almirca")
#Invocando o llamando la funcion
muestraNombre()


#Ejemplo2
print("############ Ejemplo 2 - Funciones")
#Funciones con parametros
def mostrarNombre(nom, edad):
    print(f"Tu monbre es: {nom}")
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres Menor de edad!")

name = input("Introduce tu nombre: ")
ege = int(input("Introduzca tu edad: "))

mostrarNombre(name,ege)

